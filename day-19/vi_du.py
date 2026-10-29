"""Ngày 19: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 19 --example
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

    # NỘI DUNG HỌC HÔM NAY
    customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
    summary = orders.groupBy("customer_id").agg(F.sum("amount").alias("total_amount"))
    result = customers.join(summary, "customer_id", "left").fillna({"total_amount": 0})
    result.show()
    customers.join(orders, "customer_id", "left_anti").show()
finally:
    spark.stop()
