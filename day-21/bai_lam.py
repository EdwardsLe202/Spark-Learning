"""Ngày 21: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 21
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-21").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tự viết chọn đơn mới nhất như mẫu.
    # 2. Đổi desc thành asc ở cả hai cột để chọn đơn sớm nhất mỗi khách.
    # 3. Kiểm tra C001→O001, C002→O003, C003→O004, C004→O007.
    # 4. Ghi sự khác nhau giữa giữ mới nhất và loại bản trùng hoàn toàn.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
