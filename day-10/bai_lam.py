"""Ngày 10: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 10
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-10").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tự viết lại báo cáo theo khách mà không nhìn ví dụ.
    # 2. Làm một báo cáo khác theo status gồm số đơn và tổng tiền.
    # 3. Kiểm tra completed có 7 đơn/1100000, cancelled có 1 đơn/300000.
    # 4. Giải thích một dòng của mỗi báo cáo đang biểu diễn điều gì.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
