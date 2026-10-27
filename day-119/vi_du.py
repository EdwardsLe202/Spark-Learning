"""Ngày 119: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 119 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(119, exercise=False)
    attempts = []
    for attempt in range(3):
        attempts.append(attempt + 1)
        try:
            if attempt < 2:
                raise TimeoutError("fixture timeout")
            result = "ok"
            break
        except TimeoutError:
            if attempt == 2:
                raise
    print({"attempts": attempts, "result": result})


if __name__ == "__main__":
    main()
