"""Ngày 118: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 118 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(118, exercise=False)
    import hashlib
    def cache_key(model_version, body):
        payload = json.dumps({"model_version": model_version, "input": body}, sort_keys=True, allow_nan=False)
        return hashlib.sha256(payload.encode()).hexdigest()
    body = {"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"}
    assert cache_key("v1", body) != cache_key("v2", body)
    print("Cache key đổi khi model đổi.")


if __name__ == "__main__":
    main()
