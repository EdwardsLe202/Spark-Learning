"""Ngày 107: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 107 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(107, exercise=False)
    from pydantic import ValidationError
    from services.churn_api import PredictionInput
    body = {"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"}
    print(PredictionInput(**body).model_dump())
    for bad in [{**body, "events_30d": -1}, {**body, "extra": 1}, {**body, "spend_30d": float("inf")}]:
        try:
            PredictionInput(**bad)
        except ValidationError as error:
            print("Bị chặn:", error.error_count())


if __name__ == "__main__":
    main()
