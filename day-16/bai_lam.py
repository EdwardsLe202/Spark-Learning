"""Ngày 16: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 16
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-16").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tự ghi bảng completed vào thư mục exercise trong artifacts/beginner/day-16.
    # 2. Đọc lại và kiểm tra số dòng, tổng tiền, schema.
    # 3. Chạy lại cùng chương trình và xác nhận vẫn 7 dòng.
    # 4. Xem thư mục trong trình soạn thảo: có một hay nhiều file phần? Ghi điều thực thấy, không khẳng định mọi lần ghi luôn có cùng số file.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
