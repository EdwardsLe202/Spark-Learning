"""Ngày 62: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 62
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(62, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tính tay baseline luôn 0 trên nhãn 0,0,0,1.
    # 2. So most_frequent với stratified có random_state cố định.
    # 3. Lưu bảng baseline, split và số mẫu mỗi lớp.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
