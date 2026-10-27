"""Ngày 61: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 61 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(61, exercise=False)
    train = snapshot_pd()
    print(train[FEATURES + ["label"]].head(3).to_string(index=False))
    print("Số nhãn:", train["label"].value_counts().to_dict())
    assert "customer_id" not in FEATURES
    assert "label" not in FEATURES


if __name__ == "__main__":
    main()
