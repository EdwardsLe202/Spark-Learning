"""Ngày 27: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 27
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-27").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Thử repartition(2) rồi repartition(4) ở hai biến thể riêng.
    # 2. Kiểm tra count và tổng tiền của cả hai vẫn bằng nguồn.
    # 3. Dùng explain cho groupBy và tìm Exchange nếu có trong plan.
    # 4. Viết một ví dụ vì sao một khách quá nhiều đơn có thể làm một phần xử lý nặng hơn; chưa cần tự sửa skew.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
