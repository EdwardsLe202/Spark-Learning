"""Ngày 109: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 109 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(109, exercise=False)
    from fastapi.testclient import TestClient
    from services.churn_api import app
    path = ensure_demo_model()
    os.environ["COURSE_MODEL_PATH"] = str(path)
    os.environ["COURSE_API_KEY"] = "fixture-only-key"
    with TestClient(app) as client:
        print("Health:", client.get("/health").status_code)
        print("Ready:", client.get("/ready").json())
        body = {"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"}
        print(client.post("/predict", json=body, headers={"x-api-key": "fixture-only-key"}).json())


if __name__ == "__main__":
    main()
