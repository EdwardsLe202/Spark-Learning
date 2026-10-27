"""Ngày 101: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 101
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(101, exercise=True)
    print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
    # 1. Vẽ nguồn/đích/network/service account cho môi trường bạn chọn.
    # 2. Đặt budget/quota và kế hoạch tắt dịch vụ trước nhánh cloud.
    # 3. Nếu không có tài khoản, nghiệm thu deployment ở Standalone; ghi cloud mới thiết kế. Nếu có, thử quyền đọc/ghi được phép và bị từ chối ngoài prefix.

    # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
