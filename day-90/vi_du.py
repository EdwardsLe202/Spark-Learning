"""Ngày 90: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 90 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(90, exercise=False)
    mlflow = setup_tracking()
    experiment = mlflow.get_experiment_by_name("spark-course-150")
    print({"tracking_uri": mlflow.get_tracking_uri(), "artifact_location": experiment.artifact_location})
    record = {"customer_id": "C001", "snapshot_date": "2025-07-01", "model_version": "fill-resolved-version", "run_id": "fill-real-run", "data_hash": data_hash()}
    write_json(out / "prediction_lineage_template.json", record)
    print("Template chưa đủ nghiệm thu cho tới khi điền run/version thật.")


if __name__ == "__main__":
    main()
