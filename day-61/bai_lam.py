"""Ngày 61: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 61
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(61, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Viết một câu mô tả mỗi feature và đơn vị.
    # 2. Chỉ ra vì sao label hoặc giao dịch tương lai không là feature.
    # 3. Đổi mục tiêu thành số tiền tháng sau, nêu vì sao cần metric khác.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
