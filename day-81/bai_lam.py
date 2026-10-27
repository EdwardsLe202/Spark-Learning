"""Ngày 81: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 81
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(81, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tách hàm build_features vào module riêng có import an toàn.
    # 2. Tạo CLI nhận --snapshot-date và --output, chạy từ terminal mới.
    # 3. Ghi commit, code hash và trạng thái chưa commit khi có.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
