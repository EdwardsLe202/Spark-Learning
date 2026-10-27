"""Ngày 80: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 80 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(80, exercise=False)
    from sklearn.metrics import average_precision_score
    model, train, val = fit_sklearn()
    test = snapshot_pd("2025-06-01")
    score = model.predict_proba(test[FEATURES])[:, 1]
    report = {"test_ap": float(average_precision_score(test.label, score)), **metric_counts(test.label, score), "source": "synthetic", "threshold": 0.5}
    write_json(out / "test_report.json", report)
    print(report)


if __name__ == "__main__":
    main()
