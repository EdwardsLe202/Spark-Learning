"""Ngày 124: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 124 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(124, exercise=False)
    from rag_support import generate_text
    result = generate_text("Trích xuất JSON duy nhất với order_id và amount_vnd; thiếu thì null.", "Đơn A01 có giá 120000 đồng.", max_new_tokens=64)
    print(result)


if __name__ == "__main__":
    main()
