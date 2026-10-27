"""Ngày 107: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 107
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(107, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Thử thiếu spend, category mới, số âm và trường thừa.
    # 2. Chốt policy strict/coerce bằng test, không đoán.
    # 3. Đối chiếu schema API với input model ngày 78.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
