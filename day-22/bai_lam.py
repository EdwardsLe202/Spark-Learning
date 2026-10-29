"""Ngày 22: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 22
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-22").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Viết lại ví dụ với cửa sổ tăng dần.
    # 2. Xem riêng C002; tự tính previous_amount và running_amount.
    # 3. Kiểm tra O003: NULL/50000; O005: 50000/200000.
    # 4. Giải thích vì sao running total của C002 không cộng đơn C001.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
