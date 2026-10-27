"""Ngày 100: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 100
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(100, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Build/up services/spark.compose.yml theo hướng dẫn.
    # 2. Submit cluster_smoke, xem UI có worker/executor và đọc kết quả.
    # 3. Dừng một worker trong thí nghiệm, ghi điều thực quan sát; phân biệt mô phỏng container với nhiều máy thật.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
