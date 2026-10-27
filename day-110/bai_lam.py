"""Ngày 110: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 110
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(110, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Chạy tests API, bổ sung request có role tự nhận admin và trường thừa.
    # 2. Thêm payload/rate limit cho bản bài làm hoặc gateway, test 413/429 theo policy.
    # 3. Viết quyền tối thiểu và giới hạn API key demo.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
