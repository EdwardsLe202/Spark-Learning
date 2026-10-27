"""Ngày 115: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 115
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(115, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Theo dõi shape qua qk transpose/softmax/value.
    # 2. Thử ba token, dự đoán shape trước chạy.
    # 3. Viết luồng text→tokenizer→embedding→Transformer→output và phần nào cần pretrained weights.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
