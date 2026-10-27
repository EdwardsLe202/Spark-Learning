"""Ngày 116: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 116
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(116, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Cài requirements-ai, tải generator bằng script của repo khi đủ dung lượng.
    # 2. Dùng AutoTokenizer.from_pretrained trên đường dẫn cache trong manifest; xem input_ids/token count.
    # 3. Chạy generate tối đa 64 token trên CPU, ghi model revision và tài nguyên, không gọi mock là model thật.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
