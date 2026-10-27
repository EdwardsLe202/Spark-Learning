"""Ngày 128: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 128
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(128, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Sửa doc thành v2, so ID/hash và tập chunk cũ cần gỡ.
    # 2. Xóa một doc trên bản sao, rebuild và kiểm tra tìm kiếm không còn thấy.
    # 3. Viết manifest active versions để tránh lẫn v1/v2.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
