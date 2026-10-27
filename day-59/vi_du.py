"""Ngày 59: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 59 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(59, exercise=False)
    frames = {name: snapshot_pd(day) for name, day in [("train", "2025-02-01"), ("validation", "2025-04-01"), ("test", "2025-06-01")]}
    for name, frame in frames.items():
        print(name, frame.shape, frame["snapshot_date"].unique().tolist())
    print("Hash nguồn:", data_hash())


if __name__ == "__main__":
    main()
