"""Ngày 122: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 122
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(122, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Viết prompt v2 với hai ví dụ và trường thiếu.
    # 2. Tạo 10 văn bản có nhãn gồm thiếu/mơ hồ/chỉ dẫn nhiễu.
    # 3. Giữ dataset cố định để so hai prompt ở ngày 125.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
