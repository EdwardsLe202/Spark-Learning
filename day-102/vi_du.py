"""Ngày 102: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 102 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(102, exercise=False)
    from services.release import promote, rollback
    from services.pipeline import run_step
    for version in ["release-v1", "release-v2"]:
        run_step("train", version=version)
        run_step("evaluate", version=version)
        print("Promote:", promote(version))
    print("Rollback:", rollback())


if __name__ == "__main__":
    main()
