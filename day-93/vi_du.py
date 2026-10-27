"""Ngày 93: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 93 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(93, exercise=False)
    from services.pipeline import run_step
    version = "rejected-demo"
    run_step("train", version=version)
    try:
        run_step("evaluate", version=version, min_ap=1.1)
    except ValueError as error:
        print("Candidate bị từ chối:", error)
    try:
        run_step("score", version=version)
    except ValueError as error:
        print("Score bị chặn:", error)


if __name__ == "__main__":
    main()
