"""Ngày 108: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 108 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(108, exercise=False)
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from services.churn_api import PredictionInput
    app = FastAPI()
    @app.post("/validate")
    def validate(body: PredictionInput):
        return {"status": "validated", "features": body.model_dump()}
    with TestClient(app) as client:
        ok = client.post("/validate", json={"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"})
        bad = client.post("/validate", json={"events_30d": -1})
        print(ok.status_code, bad.status_code)


if __name__ == "__main__":
    main()
