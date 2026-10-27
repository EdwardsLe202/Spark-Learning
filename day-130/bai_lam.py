"""Ngày 130: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 130
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(130, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Ghi toàn corpus bằng embedding thật và UUID ổn định từ chunk_id.
    # 2. Sửa/xóa một doc, xóa cả chunk cũ không còn hoạt động.
    # 3. Test filter public/internal trước context; lưu collection version và model manifest.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
