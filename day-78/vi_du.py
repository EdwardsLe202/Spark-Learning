"""Ngày 78: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 78 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(78, exercise=False)
    import joblib
    model, train, val = fit_sklearn()
    path = out / "model.joblib"
    joblib.dump(model, path)
    loaded = joblib.load(path)
    a = model.predict_proba(val[FEATURES].head(3))
    b = loaded.predict_proba(val[FEATURES].head(3))
    assert np.allclose(a, b)
    write_json(out / "metadata.json", {"model_version": "sklearn-demo-v1", "features": FEATURES, "data_hash": data_hash()})
    print("Đã lưu và load pipeline sklearn.")


if __name__ == "__main__":
    main()
