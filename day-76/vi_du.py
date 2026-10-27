"""Ngày 76: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 76 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(76, exercise=False)
    model, train, val = fit_sklearn()
    val = val.copy()
    val["score"] = model.predict_proba(val[FEATURES])[:, 1]
    for region, group in val.groupby("region"):
        print(region, {"n": len(group), "positives": int(group.label.sum()), **metric_counts(group.label, group.score)})


if __name__ == "__main__":
    main()
