"""Ngày 82: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 82 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(82, exercise=False)
    frame = snapshot_pd()
    required = set(FEATURES + ["customer_id", "snapshot_date", "label"])
    assert required <= set(frame.columns)
    assert not frame[["customer_id", "snapshot_date"]].duplicated().any()
    assert (frame.spend_30d >= 0).all()
    print({"rows": len(frame), "missing_recency": int(frame.recency_days.isna().sum()), "valid": True})


if __name__ == "__main__":
    main()
