"""Ngày 150: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 150
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(150, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tự chấm theo bằng chứng, sửa lỗi nghiêm trọng trước khi gọi hoàn thành.
    # 2. Demo sạch 10 phút có file lỗi, retry, rollback, thiếu bằng chứng và sai quyền.
    # 3. Trả lời câu hỏi Spark/ML/MLOps/API/RAG và ghi năm hướng học sâu tiếp theo.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
