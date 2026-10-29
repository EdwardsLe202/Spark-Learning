"""Ngày 29: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 29 --example
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

    # NỘI DUNG HỌC HÔM NAY
    customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
    if customers.groupBy("customer_id").count().filter("count > 1").count() > 0:
        raise ValueError("Khách trùng khóa")
    summary = orders.filter(F.col("status") == "completed").groupBy("customer_id").agg(F.sum("amount").alias("total_amount"))
    report = customers.join(summary, "customer_id", "left").fillna({"total_amount": 0})
    regional = report.groupBy("region").agg(F.sum("total_amount").alias("total_amount"))
    report.orderBy("customer_id").show()
    regional.show()
finally:
    spark.stop()
