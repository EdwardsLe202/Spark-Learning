"""Ngày 98: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 98 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(98, exercise=False)
    print((ROOT / "services/compose.yml").read_text())
    print("Chuẩn bị model bằng services/pipeline.py trước khi up.")
    print("Lab: docker compose -f services/compose.yml up --build")


if __name__ == "__main__":
    main()
