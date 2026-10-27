"""Ngày 124: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 124
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(124, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tải generator nếu chưa có bằng script, ghi model card/license/revision.
    # 2. Nối validator ngày 123, test lỗi/timeout và retry hữu hạn.
    # 3. Thêm deadline cứng bằng subprocess timeout trong bản bài làm, ghi cách hủy worker.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
