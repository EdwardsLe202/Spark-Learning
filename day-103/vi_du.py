"""Ngày 103: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 103 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(103, exercise=False)
    frame = snapshot_pd("2025-04-01")
    report = {"rows": len(frame), "snapshot": "2025-04-01", "missing_rate": frame[FEATURES].isna().mean().to_dict(), "duplicate_keys": int(frame[["customer_id", "snapshot_date"]].duplicated().sum())}
    write_json(out / "quality_report.json", report)
    print(report)


if __name__ == "__main__":
    main()
