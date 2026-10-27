"""Ngày 113: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 113
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(113, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. In shape xb/yb/prediction trước loss.
    # 2. Thử batch_size=1 và đếm số optimizer step.
    # 3. Giải thích điều gì xảy ra nếu quên zero_grad.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
