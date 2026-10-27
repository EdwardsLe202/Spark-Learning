"""Ngày 145: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 145
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(145, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Hoàn thiện dự án 3, chạy/chấm đủ eval, phân tích năm lỗi.
    # 2. Demo câu thiếu nguồn, sai quyền, injection, update/delete và đổi index.
    # 3. Viết clean run và chính sách budget/timeout/rollback.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
