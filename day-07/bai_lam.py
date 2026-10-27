"""Ngày 07: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 07
"""
import os
import sys
from pathlib import Path
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "beginner"
spark = SparkSession.builder.master("local[2]").appName("beginner-day-07").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Chọn customer_id, order_date, amount từ bảng nguồn.
    # 2. Đổi tên amount thành money_vnd trong kết quả này.
    # 3. In tên cột và số dòng của cả nguồn lẫn kết quả; giải thích phần nào đổi.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
