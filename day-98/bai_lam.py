"""Ngày 98: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 98
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(98, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tạo model, đặt COURSE_API_KEY trong terminal, up Compose.
    # 2. Kiểm tra health/ready và healthcheck container.
    # 3. Down rồi up lại, xác nhận artifact còn và không tự train lại model.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
