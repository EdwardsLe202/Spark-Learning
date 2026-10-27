"""Ngày 64: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 64 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(64, exercise=False)
    from sklearn.metrics import roc_auc_score, average_precision_score
    y = [0, 0, 1, 1]
    scores = [0.1, 0.4, 0.35, 0.8]
    print("ROC AUC:", roc_auc_score(y, scores))
    print("Average precision:", average_precision_score(y, scores))


if __name__ == "__main__":
    main()
