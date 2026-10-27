"""Ngày 106: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 106 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(106, exercise=False)
    payload = {"events_30d": 2, "spend_30d": 300000, "recency_days": 12, "region": "HN", "plan": "basic"}
    serialized = json.dumps(payload)
    assert json.loads(serialized) == payload
    print({"method": "POST", "path": "/predict", "body": payload, "expected_fields": ["score", "prediction", "model_version", "request_id"]})


if __name__ == "__main__":
    main()
