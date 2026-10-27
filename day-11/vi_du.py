"""Ngày 11: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 11 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-11").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:

    # NỘI DUNG HỌC HÔM NAY
    orders = spark.createDataFrame([("A", 100000), ("B", None), ("C", 0)], "order_id string, amount long")
    missing = orders.filter(orders["amount"].isNull())
    missing.show()
    orders.agg(F.count("*").alias("rows"), F.count("amount").alias("known_amounts"), F.sum("amount").alias("total")).show()
finally:
    spark.stop()
