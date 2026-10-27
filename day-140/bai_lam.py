"""Ngày 140: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 140
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(140, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Test keyword/dense/Qdrant đều không đưa doc-internal vào context public.
    # 2. Thử query tự nhận admin, kiểm tra role vẫn public.
    # 3. Chấm 6 câu forbidden và bổ sung ca internal hợp lệ ở file riêng.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
