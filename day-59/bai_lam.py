"""Ngày 59: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 59
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(59, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Ghi bảng khoảng feature/label của ba snapshot.
    # 2. Viết test thêm tiền tương lai và bản đến muộn không đổi feature cũ.
    # 3. Giải thích khi nào việc cùng customer xuất hiện nhiều tập phù hợp hoặc không phù hợp.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
