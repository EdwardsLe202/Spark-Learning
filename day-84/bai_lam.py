"""Ngày 84: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 84
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(84, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Viết test pipeline trong tmp_path cho code dự án của bạn.
    # 2. Kiểm tra rerun không tăng khóa và score trước/sau load bằng nhau.
    # 3. Thêm test Spark tiny cho cutoff đúng biên và ingested_at đến muộn.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
