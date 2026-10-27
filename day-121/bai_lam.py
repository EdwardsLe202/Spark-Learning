"""Ngày 121: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 121
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(121, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Dùng tokenizer thật đếm hai đoạn tiếng Việt và so số ký tự/từ/token.
    # 2. Đặt max input/output, thử request vượt budget bị chặn.
    # 3. So do_sample=false với sampling trên tập prompt cố định, ghi không coi ngẫu nhiên là độ đúng.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
