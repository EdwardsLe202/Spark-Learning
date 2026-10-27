"""Ngày 146: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 146
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(146, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Chọn một lỗi thật trong eval và trace.
    # 2. So ba hướng sửa bằng dữ liệu, chi phí và tiêu chí thành công.
    # 3. Chốt chưa train nếu lỗi không nằm ở hành vi model cần học.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
