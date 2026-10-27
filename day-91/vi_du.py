"""Ngày 91: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 91 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(91, exercise=False)
    from graphlib import TopologicalSorter
    parents = {"validate": set(), "features": {"validate"}, "train": {"features"}, "evaluate": {"train"}, "score": {"evaluate"}}
    print(list(TopologicalSorter(parents).static_order()))
    print("Đây là kiểm tra đồ thị local; chưa chạy scheduler Airflow.")


if __name__ == "__main__":
    main()
