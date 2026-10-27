"""Ngày 126: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 126
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(126, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Vẽ riêng hai luồng và input/output từng bước.
    # 2. Chỉ ra artifact nào cần version và phần nào cập nhật khi sửa doc.
    # 3. Ghi quyền sử dụng corpus và ranh giới trust của nội dung tài liệu.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
