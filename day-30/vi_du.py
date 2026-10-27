"""Ngày 30: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 30 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-30").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    completed = orders.filter(F.col("status") == "completed")
    assert orders.count() == 8
    assert completed.count() == 7
    assert completed.agg(F.sum("amount")).first()[0] == 1100000
    print("Ví dụ kiểm tra dữ liệu nền đã khớp. Ba bài cuối vẫn cần bạn tự viết.")
finally:
    spark.stop()
