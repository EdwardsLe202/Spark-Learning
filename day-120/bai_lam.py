"""Ngày 120: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 120
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(120, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Hoàn thiện checklist dự án 2 và hướng dẫn clean run.
    # 2. Demo ba lỗi và rollback, truy một prediction về model/run/data/code.
    # 3. Lưu báo cáo tải/monitoring, đánh dấu rõ local, container và phần cloud chỉ thiết kế.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
