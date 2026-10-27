"""Ngày 43: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 43
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(43, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Chạy PostgreSQL bằng services/postgres.compose.yml và file SQL nguồn đi kèm.
    # 2. Dùng spark.read.format("jdbc") với PostgreSQL driver, URL và user/password từ biến môi trường theo docs/CAI_DAT_NANG_CAO.md.
    # 3. So số dòng/tổng tiền với nguồn; ghi quyền tối thiểu và phần object storage mới thiết kế.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
