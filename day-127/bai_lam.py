"""Ngày 127: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 127
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(127, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Đọc năm chunk ở hai cấu hình và đánh dấu mất/ngắt ý.
    # 2. Thử parser với văn bản bảng/Unicode và ghi lỗi.
    # 3. Chọn một cấu hình trên dev, lưu chunking version.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
