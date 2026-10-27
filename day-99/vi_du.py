"""Ngày 99: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 99 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(99, exercise=False)
    path = ROOT / ".github/workflows/course-integration.yml"
    print(path.read_text())
    print("Chạy tương đương local: python -m pytest tests -q")


if __name__ == "__main__":
    main()
