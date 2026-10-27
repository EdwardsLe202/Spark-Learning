"""Ngày 66: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 66
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(66, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tạo validation có spend rất lớn và kiểm tra mean train không đổi.
    # 2. Cố tình fit lại scaler trên validation ở nhánh sai để thấy khác.
    # 3. Viết test phát hiện việc pipeline.fit bị gọi khi inference.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
