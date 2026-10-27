"""Ngày 149: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 149
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(149, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Hoàn thiện README/data dictionary/model card/runbook của ba dự án.
    # 2. Clean run ở môi trường và output mới; thử lỗi và phục hồi.
    # 3. Ghi mọi bước cần thao tác miệng rồi bổ sung vào hướng dẫn.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
