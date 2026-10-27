"""Ngày 137: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 137
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(137, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Đọc code từng bước, chạy câu có nguồn và câu không có nguồn.
    # 2. Chấm tay mỗi phát biểu có citation hỗ trợ không.
    # 3. Chọn min_score trên dev, ghi trade-off từ chối quá mức và bịa.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
