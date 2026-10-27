"""Ngày 117: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 117
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(117, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Chạy API model thật và warm-up 10 request.
    # 2. Gửi ít nhất 100 request cho mỗi concurrency 1/2/4 bằng load_test.py.
    # 3. Lưu mọi status/timeout, p50/p95/throughput và cấu hình máy.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
