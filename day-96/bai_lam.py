"""Ngày 96: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 96
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(96, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Build image bằng lệnh trên.
    # 2. Chạy services/pipeline.py all trong container với volume artifacts/full theo hướng dẫn.
    # 3. Xóa container thử, xác nhận model/prediction trong volume còn và score khớp local.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
