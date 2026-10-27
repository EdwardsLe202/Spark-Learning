"""Ngày 143: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 143
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(143, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Test args không phải object và role tự nhận.
    # 2. Giả lập tool timeout, retry tối đa 1 nếu policy cho phép.
    # 3. Kiểm tra mọi tool result có schema và giới hạn kích thước.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
