"""Ngày 63: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 63
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(63, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tính tay precision/recall trước khi chạy.
    # 2. Đổi threshold=0.15 và đối chiếu từng mẫu.
    # 3. Chốt policy khi không có mẫu dự đoán dương.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
