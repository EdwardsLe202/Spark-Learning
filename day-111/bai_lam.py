"""Ngày 111: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 111
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(111, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Phân loại load file, gọi network và predict CPU thành nhóm công việc.
    # 2. Thiết kế job queue với limit/status/timeout cho batch dài.
    # 3. Test queue đầy và worker lỗi; ghi dữ liệu nào tồn tại qua restart.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
