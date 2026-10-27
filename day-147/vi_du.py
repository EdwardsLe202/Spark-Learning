"""Ngày 147: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 147 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(147, exercise=False)
    import hashlib
    rows = [{"group_id": "g1", "instruction": "Trả JSON", "input": "Đơn A01", "output": '{"order_id":"A01"}'}, {"group_id": "g1", "instruction": "Trả JSON", "input": "Đơn A01", "output": '{"order_id":"A01"}'}]
    keys = [hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest() for r in rows]
    print({"rows": len(rows), "unique_exact": len(set(keys))})
    write_json(out / "dataset_example.json", rows[:1])


if __name__ == "__main__":
    main()
