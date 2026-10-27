"""Ngày 84: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 84 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(84, exercise=False)
    from services.pipeline import run_step
    version = "integration-demo"
    for step in ["validate", "features", "train", "evaluate", "score"]:
        result = run_step(step, version=version)
        print(step, result.get("rows", result.get("accepted", "done")))
    run_step("score", version=version)
    print("Rerun cùng snapshot/version ghi thay đúng đích.")


if __name__ == "__main__":
    main()
