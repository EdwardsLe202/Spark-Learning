"""Ngày 74: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 74 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(74, exercise=False)
    from sklearn.metrics import average_precision_score
    from time import perf_counter
    rows = []
    for C in [0.1, 1.0]:
        start = perf_counter()
        model, train, val = fit_sklearn(C)
        ap = average_precision_score(val.label, model.predict_proba(val[FEATURES])[:, 1])
        rows.append({"C": C, "validation_ap": float(ap), "seconds": perf_counter() - start})
    print(rows)


if __name__ == "__main__":
    main()
