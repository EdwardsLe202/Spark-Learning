"""Ngày 12: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 12 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-12").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:

    # NỘI DUNG HỌC HÔM NAY
    orders = spark.createDataFrame([("O001", 100000), ("O001", 100000), ("O002", 200000)], "order_id string, amount long")
    clean = orders.distinct()
    print("Trước:", orders.count(), "Sau:", clean.count())
    clean.agg(F.sum("amount").alias("total")).show()
finally:
    spark.stop()
