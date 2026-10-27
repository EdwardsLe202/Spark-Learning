"""Ngày 139: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 139
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(139, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Thêm trace vào RAG thật gồm model/prompt/index revision và usage.
    # 2. Gây lỗi parser/model timeout, tìm bước lỗi theo request_id.
    # 3. Viết policy che/xóa PII và giới hạn người xem log.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
