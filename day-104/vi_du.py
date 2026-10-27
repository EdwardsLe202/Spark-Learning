"""Ngày 104: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 104 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(104, exercise=False)
    model, train, val = fit_sklearn()
    current = val.copy()
    current["spend_30d"] *= 3
    print({"reference_mean_spend": float(val.spend_30d.mean()), "current_mean_spend": float(current.spend_30d.mean())})
    print("Có thay đổi phân bố; chưa đủ để kết luận performance nếu chưa có nhãn current.")


if __name__ == "__main__":
    main()
