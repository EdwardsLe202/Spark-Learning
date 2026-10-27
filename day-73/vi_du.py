"""Ngày 73: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 73 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(73, exercise=False)
    model, train, val = fit_sklearn()
    scores = model.predict_proba(val[FEATURES])[:, 1]
    rows = []
    for threshold in [0.3, 0.5, 0.7]:
        report = metric_counts(val.label, scores, threshold)
        rows.append({"threshold": threshold, **report, "cost": report["fp"] + 5 * report["fn"]})
    print(rows)


if __name__ == "__main__":
    main()
