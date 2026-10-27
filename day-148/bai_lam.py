"""Ngày 148: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 148
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(148, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Hoàn thiện kế hoạch cùng dataset ngày 147 và baseline ngày 146.
    # 2. Nếu đủ máy, cài requirements-finetune, chạy script, load adapter tiến trình mới.
    # 3. So held-out quality/latency/RAM; nếu không train, ghi thiết kế/chưa thực thi, phần này là mở rộng.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
