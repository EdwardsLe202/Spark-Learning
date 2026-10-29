"""Ngày 19: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 19
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-19").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tạo báo cáo theo khách nhưng chỉ tính completed.
    # 2. Left join với tất cả customers và điền tổng 0 cho người không có đơn hoàn tất.
    # 3. Kiểm tra C003=120000, C005=0 và tổng báo cáo=1100000.
    # 4. Dùng anti join tìm khách không có đơn bất kỳ; so với bảng báo cáo.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
