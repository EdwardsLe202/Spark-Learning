"""Ngày 05: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 05 --example
"""
import os
import sys
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
spark = SparkSession.builder.master("local[2]").appName("beginner-day-05").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:

    # NỘI DUNG HỌC HÔM NAY
    orders = spark.createDataFrame(
        [("O001", "C001", 100000), ("O002", "C001", 200000), ("O003", "C002", 50000)],
        "order_id string, customer_id string, amount long",
    )
    orders.printSchema()
    print("Tên cột:", orders.columns)
finally:
    spark.stop()
