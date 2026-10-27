"""Ngày 76: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 76
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(76, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Báo metric theo plan và region, kèm support.
    # 2. Thử bootstrap theo customer_id với seed và ghi giới hạn mẫu nhỏ.
    # 3. Chỉ ra một nhóm chưa đủ mẫu để khẳng định hơn/kém.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
