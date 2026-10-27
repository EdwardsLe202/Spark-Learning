"""Ngày 63: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 63 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(63, exercise=False)
    y = [1, 0, 1, 0]
    scores = [0.9, 0.8, 0.2, 0.1]
    report = metric_counts(y, scores, threshold=0.5)
    print(report)
    assert report["tp"] == report["fp"] == report["fn"] == report["tn"] == 1


if __name__ == "__main__":
    main()
