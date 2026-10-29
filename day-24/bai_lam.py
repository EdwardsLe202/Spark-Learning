"""Ngày 24: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 24
"""
import os
import sys
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "beginner"
spark = SparkSession.builder.master("local[2]").appName("beginner-day-24").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tự viết hàm nhận day và output_root làm tham số.
    # 2. Chạy ngày 2025-01-03 và 2025-01-05 vào đích exercise của bạn.
    # 3. Kiểm tra mỗi ngày có 2 đơn, tổng cả hai ngày 520000.
    # 4. Thử ngày không có dữ liệu; ghi lỗi có chủ đích, không tạo báo cáo trống rồi báo thành công.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
