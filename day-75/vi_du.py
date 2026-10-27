"""Ngày 75: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 75 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(75, exercise=False)
    folds = [{"train": ["2025-02-01"], "validation": "2025-04-01"}]
    protocol = {"selection_folds": folds, "final_test": "2025-06-01", "label_horizon_days": 30}
    write_json(out / "protocol.json", protocol)
    print(protocol)


if __name__ == "__main__":
    main()
