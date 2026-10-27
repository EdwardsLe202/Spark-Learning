"""Ngày 75: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 75
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(75, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Vẽ các cửa sổ nhãn trên trục thời gian và kiểm tra không chồng.
    # 2. Thiết kế thêm fold trên dữ liệu giả lập mở rộng, kiểm tra observed_until.
    # 3. Giải thích khác biệt random CV và temporal CV, đọc CrossValidator foldCol nhưng không tin nó tự kiểm tra thời gian.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
