"""Ngày 20: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 20
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-20").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tự tạo bad_customers bằng cách thêm bản C001 như mẫu.
    # 2. Viết kiểm tra trước join: nếu có khóa count>1 thì raise ValueError.
    # 3. Chạy với bảng sai để thấy bị chặn; chạy lại với bảng khách chuẩn.
    # 4. Kiểm tra join chuẩn có 8 dòng và tổng 1400000.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
