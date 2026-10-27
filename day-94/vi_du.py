"""Ngày 94: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 94 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(94, exercise=False)
    from services.pipeline import run_step
    for _ in range(2):
        print(run_step("validate", snapshot_date="2025-04-01", version="backfill-demo"))
        print(run_step("features", snapshot_date="2025-04-01", version="backfill-demo")["rows"])


if __name__ == "__main__":
    main()
