"""Ngày 119: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 119
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(119, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Thử API timeout và input sai, kiểm tra policy retry khác nhau.
    # 2. Chạy hai version local với route thử canary hoặc shadow, ghi tỷ lệ và score.
    # 3. Rollback, restart đúng worker và xác nhận version cũ ở response.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
