"""Ngày 112: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 112
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(112, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tạo x shape [4,3] và dự đoán output trước chạy.
    # 2. Thử sai chiều [4,2], đọc lỗi rồi sửa.
    # 3. Ghi CPU/MPS khả dụng trên máy và giữ ví dụ nhỏ.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
