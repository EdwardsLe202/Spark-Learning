"""Ngày 114: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 114
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(114, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. So train mode và eval với dropout trên cùng input.
    # 2. Load trong tiến trình mới, so allclose.
    # 3. Nếu tiếp tục training, lưu thêm optimizer/epoch và giải thích vì sao.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
