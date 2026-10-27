"""Ngày 86: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 86 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(86, exercise=False)
    mlflow = setup_tracking()
    with mlflow.start_run(run_name="parameter-demo") as run:
        mlflow.log_param("C", 1.0)
        mlflow.log_param("train_snapshot", "2025-02-01")
        mlflow.set_tag("source_hash", data_hash())
        mlflow.log_artifact(str(ROOT / "data/raw/manifest.json"))
        print("Run:", run.info.run_id)


if __name__ == "__main__":
    main()
