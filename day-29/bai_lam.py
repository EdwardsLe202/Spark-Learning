"""Ngày 29: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 29
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-29").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Làm theo đặc tả projects/01-spark-report/README.md; tự viết luồng chính trước khi mở mẫu.
    # 2. Ghi hai báo cáo Parquet vào đích exercise, đọc lại để xác nhận.
    # 3. Chạy lại hai lần và xác nhận số dòng không tăng.
    # 4. Thử bảng khách trùng C001 để thấy chương trình dừng.
    # 5. Viết hướng dẫn chạy ngắn và giải thích vì sao phải giữ C005.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
