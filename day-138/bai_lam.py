"""Ngày 138: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 138
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(138, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Chạy services/rag_eval.py --strategy dense --generation trên 40 câu sau khi tải model.
    # 2. Chấm correctness/groundedness/citation và hành vi theo từng nhóm.
    # 3. So hai cấu hình chọn bằng dev; giữ test cho chấm cuối và phân tích năm lỗi.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
