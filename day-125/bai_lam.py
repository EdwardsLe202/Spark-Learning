"""Ngày 125: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 125
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(125, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Chạy v1/v2 trên 10 mẫu đã gán nhãn ngày 122.
    # 2. Chấm schema, từng trường, latency/usage và lỗi không trả lời.
    # 3. Phân tích ít nhất ba lỗi bằng raw output và nguồn, giữ test khác tập sửa prompt.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
