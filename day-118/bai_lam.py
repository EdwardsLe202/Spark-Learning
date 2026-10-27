"""Ngày 118: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 118
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(118, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Đo API một worker rồi hai worker, ghi RAM và p95.
    # 2. Thêm batch endpoint có max batch size và kiểm tra score tương đương từng mẫu.
    # 3. Test queue đầy/rate limit trả lỗi có kiểm soát, không crash.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
