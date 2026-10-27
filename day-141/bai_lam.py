"""Ngày 141: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 141
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(141, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Retrieve doc-injection trong ca thử, kiểm tra không thi hành chỉ dẫn giả.
    # 2. Gây model timeout/index lỗi, test retry/abstention/error rõ.
    # 3. Giữ ca injection và quyền như regression tests sau mỗi thay đổi.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
