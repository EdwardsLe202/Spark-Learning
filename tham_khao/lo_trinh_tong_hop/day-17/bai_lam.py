"""Ngày 17: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 17
"""
from spark_lab import ROOT, DATA, output_dir

from datetime import date
steps = ["validate", "features", "train", "evaluate", "score"]
snapshot = date.fromisoformat("2025-02-01")
for step in steps:
    print({"step": step, "snapshot_date": snapshot.isoformat(), "status": "planned"})
# TODO: thay bản kế hoạch bằng các lời gọi CLI ngày 16, kiểm tra returncode từng bước.

# Bài tự làm hôm nay:
# TODO Dùng module/CLI ngày 16, viết run_pipeline(snapshot_date) gọi đúng thứ tự và dừng ngay nếu validate lỗi.
# TODO Cho features thất bại một lần có chủ ý. Thêm retry tối đa 2 lần cho lỗi tạm thời; schema lỗi phải dừng, không retry mù.
# TODO Backfill snapshot cũ hai lần; kiểm tra cùng số dòng, cùng khóa và cùng hash nội dung đã chuẩn hóa thứ tự.
# TODO Ghi metadata từng bước vào JSON: run_id, interval, input_hash, output_path, status, duration. Không truyền DataFrame qua cơ chế metadata.
# TODO Viết runbook (hướng dẫn vận hành) cho nguồn thiếu ngày và feature lỗi. Nếu học sâu Airflow, chuyển workflow sang DAG theo docs/CAI_DAT.md và kiểm chứng retry trên UI.
