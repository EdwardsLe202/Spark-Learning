"""Ngày 136: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 136
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(136, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. So dense với hybrid hoặc reranker thật trên dev, giữ cùng nhãn/ACL.
    # 2. Chốt cấu hình rồi chấm test, tách câu không relevant.
    # 3. Phân tích ít nhất năm lỗi/ca khó theo parser→chunk→retrieve→rank.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
