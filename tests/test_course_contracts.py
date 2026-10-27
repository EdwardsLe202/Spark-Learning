"""Kiểm tra hành vi có mốc tính tay cho ví dụ, không chấm bài làm của người học."""
from pathlib import Path
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import metric_counts, snapshot_pd, FEATURES


@pytest.mark.parametrize("threshold,expected", [(0.5, (1, 1, 1, 1)), (0.15, (2, 1, 0, 1))])
def test_metric_threshold_boundaries(threshold, expected):
    result = metric_counts([1, 0, 1, 0], [0.9, 0.8, 0.2, 0.1], threshold)
    assert tuple(result[k] for k in ["tp", "fp", "fn", "tn"]) == expected


def test_snapshot_label_requires_complete_future():
    with pytest.raises(ValueError, match="quan sát đủ"):
        snapshot_pd("2025-07-15")


def test_snapshot_features_require_source_coverage_even_without_labels():
    with pytest.raises(ValueError, match="tới cutoff"):
        snapshot_pd("2025-08-02", include_labels=False)


def test_snapshot_keeps_all_entities_and_feature_contract():
    frame = snapshot_pd()
    assert len(frame) == 120
    assert not frame[["customer_id", "snapshot_date"]].duplicated().any()
    assert "label" not in FEATURES and "customer_id" not in FEATURES


def test_api_auth_validation_and_model_equivalence(tmp_path, monkeypatch):
    import joblib
    from fastapi.testclient import TestClient
    from course_support import fit_sklearn, write_json
    from services.churn_api import app
    model, train, val = fit_sklearn()
    path = tmp_path / "model.joblib"
    joblib.dump(model, path)
    write_json(path.with_suffix(".json"), {"features": FEATURES, "model_version": "test-only", "threshold": 0.5})
    monkeypatch.setenv("COURSE_MODEL_PATH", str(path))
    monkeypatch.setenv("COURSE_API_KEY", "fixture-only-key")
    body = {"events_30d": 2, "spend_30d": 300000, "recency_days": 12, "region": "HN", "plan": "basic"}
    with TestClient(app) as client:
        assert client.get("/ready").status_code == 200
        assert client.post("/predict", json=body).status_code == 401
        assert client.post("/predict", json={**body, "events_30d": -1}, headers={"x-api-key": "fixture-only-key"}).status_code == 422
        response = client.post("/predict", json=body, headers={"x-api-key": "fixture-only-key"})
        assert response.status_code == 200
        import pandas as pd
        expected = float(model.predict_proba(pd.DataFrame([body])[FEATURES])[:, 1][0])
        assert response.json()["score"] == pytest.approx(expected)
        assert response.json()["model_version"] == "test-only"


def test_rejected_candidate_blocks_scoring(monkeypatch, tmp_path):
    from services import pipeline
    monkeypatch.setattr(pipeline, "FULL", tmp_path)
    pipeline.run_step("train", version="candidate")
    with pytest.raises(ValueError, match="không đạt"):
        pipeline.run_step("evaluate", version="candidate", min_ap=1.1)
    with pytest.raises(ValueError, match="chưa được chấp nhận"):
        pipeline.run_step("score", version="candidate")
