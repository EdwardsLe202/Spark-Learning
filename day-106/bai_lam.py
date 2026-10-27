"""Ngày 106: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 106
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(106, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Viết request/response mẫu và đơn vị mỗi feature.
    # 2. Phân loại thiếu trường, sai key và model chưa ready thành status phù hợp.
    # 3. Giải thích vì sao label không có trong request.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
