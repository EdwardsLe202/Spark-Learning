"""Ngày 66: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 66 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(66, exercise=False)
    model, train, val = fit_sklearn()
    scale = model.named_steps["preprocess"].named_transformers_["numeric"].named_steps["scale"]
    before = scale.mean_.copy()
    model.predict_proba(val[FEATURES])
    assert (before == scale.mean_).all()
    print("Mean học từ train:", before.tolist())


if __name__ == "__main__":
    main()
