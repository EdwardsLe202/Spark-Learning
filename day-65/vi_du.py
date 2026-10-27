"""Ngày 65: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 65 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(65, exercise=False)
    pipeline = sklearn_pipeline()
    train = snapshot_pd()
    pipeline.fit(train[FEATURES], train.label)
    print("Các bước:", list(pipeline.named_steps))
    print("Ba score:", pipeline.predict_proba(train[FEATURES].head(3))[:, 1].tolist())


if __name__ == "__main__":
    main()
