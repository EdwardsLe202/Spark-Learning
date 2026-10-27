"""Ngày 144: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 144
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(144, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Nối proposal JSON của generator vào dispatcher, không eval text.
    # 2. Test lặp, tool lạ, timeout, sai args và thiếu dữ liệu.
    # 3. So task success/số bước/latency/quyền giữa workflow và loop trên 10 ca.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
