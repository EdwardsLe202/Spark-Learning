"""Ngày 08: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 08 --example
"""
import os
import sys
from pathlib import Path
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "beginner"
spark = SparkSession.builder.master("local[2]").appName("beginner-day-08").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    result = orders.filter((orders["status"] == "completed") & (orders["amount"] >= 150000))
    result.select("order_id", "amount", "status").show()
    print("Số đơn phù hợp:", result.count())
finally:
    spark.stop()
