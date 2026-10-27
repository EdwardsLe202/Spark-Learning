"""Ngày 89: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 89 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(89, exercise=False)
    import mlflow.sklearn
    from mlflow import MlflowClient
    mlflow = setup_tracking()
    model, train, val = fit_sklearn()
    with mlflow.start_run() as run:
        mlflow.sklearn.log_model(model, artifact_path="model")
        version = mlflow.register_model("runs:/" + run.info.run_id + "/model", "course-churn-sklearn")
    client = MlflowClient()
    client.set_registered_model_alias("course-churn-sklearn", "candidate", version.version)
    print({"version": version.version, "run_id": version.run_id})


if __name__ == "__main__":
    main()
