"""Ngày 133: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 133
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(133, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Thử query chứa mã 422 và query paraphrase không có từ trùng.
    # 2. So dense cùng top-k trên dev, ghi lỗi từng phương pháp.
    # 3. Bổ sung BM25 nếu cần, giữ cách tokenize/normalization rõ ràng.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
