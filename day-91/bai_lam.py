"""Ngày 91: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 91
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(91, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Vẽ DAG dự án của bạn và ghi input/output metadata từng node.
    # 2. Cố ý tạo chu trình để kiểm tra không hợp lệ.
    # 3. Gắn node với các CLI thật trong services/pipeline.py.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
