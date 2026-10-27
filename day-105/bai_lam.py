"""Ngày 105: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 105
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(105, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Chạy một candidate không đạt để thấy hệ thống giữ previous.
    # 2. Điền checklist projects/03-mlops-serving bằng log thực tế.
    # 3. Viết runbook cho schema lỗi và metric giảm khi nhãn tới.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
