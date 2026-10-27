"""Ngày 82: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 82
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(82, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tạo ba fixture sai: thiếu cột, khóa trùng, spend âm.
    # 2. Viết validate chặn đúng từng lỗi, giữ thông báo rõ.
    # 3. Chứng minh bước train không chạy khi validate thất bại.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
