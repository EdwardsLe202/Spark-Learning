"""Ngày 74: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 74
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(74, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tính trước số fit của grid 3×2 với 4 fold.
    # 2. Viết hai cấu hình Spark regParam bằng ParamGridBuilder nhưng đánh giá theo split thời gian tường minh.
    # 3. Lưu budget và lý do dừng tuning.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
