"""Ngày 125: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 125 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(125, exercise=False)
    truth = [{"order_id": "A01", "amount_vnd": 120000}, {"order_id": "B02", "amount_vnd": None}]
    predictions = [{"order_id": "A01", "amount_vnd": 120000}, {"order_id": "B02", "amount_vnd": 0}]
    correct = sum(pred.get(key) == true[key] for true, pred in zip(truth, predictions) for key in true)
    print({"field_accuracy": correct / 4, "source": "fixture_not_llm_benchmark"})


if __name__ == "__main__":
    main()
