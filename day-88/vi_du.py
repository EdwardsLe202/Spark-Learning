"""Ngày 88: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 88 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(88, exercise=False)
    import mlflow.sklearn
    from mlflow.models import infer_signature
    mlflow = setup_tracking()
    model, train, val = fit_sklearn()
    example = train[FEATURES].head(3)
    with mlflow.start_run(run_name="model-contract") as run:
        mlflow.sklearn.log_model(model, artifact_path="model", signature=infer_signature(example, model.predict(example)), input_example=example)
        uri = "runs:/" + run.info.run_id + "/model"
        loaded = mlflow.sklearn.load_model(uri)
        assert np.allclose(model.predict_proba(example), loaded.predict_proba(example))
        print(uri)


if __name__ == "__main__":
    main()
