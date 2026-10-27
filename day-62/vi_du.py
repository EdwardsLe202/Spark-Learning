"""Ngày 62: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 62 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(62, exercise=False)
    from sklearn.dummy import DummyClassifier
    from sklearn.metrics import accuracy_score, recall_score
    train, val = snapshot_pd(), snapshot_pd("2025-04-01")
    baseline = DummyClassifier(strategy="most_frequent").fit(train[["events_30d"]], train["label"])
    pred = baseline.predict(val[["events_30d"]])
    print({"accuracy": accuracy_score(val.label, pred), "recall": recall_score(val.label, pred, zero_division=0)})


if __name__ == "__main__":
    main()
