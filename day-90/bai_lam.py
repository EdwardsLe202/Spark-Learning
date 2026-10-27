"""Ngày 90: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 90
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(90, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tạo prediction thật và điền run/version từ ngày 89.
    # 2. Backup SQLite và artifact vào vùng thử khi không có writer, restore rồi load model.
    # 3. Viết chính sách quyền đọc/ghi và retention.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
