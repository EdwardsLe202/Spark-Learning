"""Ngày 92: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 92
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(92, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tạo .venv-airflow với Airflow 3.0.0 và constraints đúng Python 3.11.
    # 2. Đặt COURSE_ROOT/COURSE_PYTHON/DAGS_FOLDER rồi chạy airflow standalone.
    # 3. Trigger churn_pipeline, kiểm tra năm task gọi CLI thật và có prediction 120 dòng.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
