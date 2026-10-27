"""Ngày 04: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 04 --example
"""
import os
import sys
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
spark = SparkSession.builder.master("local[2]").appName("beginner-day-04").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:

    # NỘI DUNG HỌC HÔM NAY
    rows = [("O001", "C001", 100000), ("O002", "C001", 200000), ("O003", "C002", 50000)]
    orders = spark.createDataFrame(rows, ["order_id", "customer_id", "amount"])
    orders.show()
    print("Số dòng:", orders.count())
finally:
    spark.stop()
