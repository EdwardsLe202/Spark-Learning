"""Ngày 100: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 100 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(100, exercise=False)
    print((ROOT / "services/spark.compose.yml").read_text())
    print("Lab chạy spark-submit bên trong container master với --master spark://master:7077.")
    print("Script:", ROOT / "services/cluster_smoke.py")


if __name__ == "__main__":
    main()
