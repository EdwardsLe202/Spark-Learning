"""Ngày 123: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 123
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(123, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Thêm trường thừa, thiếu trường, sai kiểu và nội dung đúng schema nhưng sai tiền.
    # 2. Tạo trạng thái parse_error/refusal/content_mismatch rõ ràng.
    # 3. Chốt retry tối đa 2, test dừng khi model luôn sai.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
