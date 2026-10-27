"""Ngày 147: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 147
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(147, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Tạo ít nhất 20 ví dụ tự có quyền, nguồn/nhãn/group_id rõ.
    # 2. Dedup exact và gần giống, chia train/validation theo nhóm, giữ test khóa.
    # 3. Kiểm tra không ví dụ train nào được tạo từ test hoặc đáp án test.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
