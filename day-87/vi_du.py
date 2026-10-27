"""Ngày 87: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 87 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(87, exercise=False)
    from sklearn.metrics import average_precision_score
    mlflow = setup_tracking()
    for C in [0.1, 1.0]:
        with mlflow.start_run(run_name="churn-C-" + str(C)):
            model, train, val = fit_sklearn(C)
            ap = float(average_precision_score(val.label, model.predict_proba(val[FEATURES])[:, 1]))
            mlflow.log_param("C", C)
            mlflow.log_metric("validation_ap", ap)
            mlflow.set_tag("source_hash", data_hash())
            print(C, ap)


if __name__ == "__main__":
    main()
