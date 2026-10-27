"""Ngày 96: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 96 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(96, exercise=False)
    path = ROOT / "services/Dockerfile"
    print(path.read_text())
    print("Lab: docker build -f services/Dockerfile -t spark-course-api:local .")
    print("Đọc .dockerignore trước khi build; ví dụ này chưa build image.")


if __name__ == "__main__":
    main()
