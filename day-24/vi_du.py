"""Ngày 24: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 24 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-24").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    target_root = ROOT / "artifacts/beginner/day-24/daily"
    def run_day(day):
        part = orders.filter(F.col("order_date") == day)
        if part.count() == 0:
            raise ValueError("Không có dữ liệu ngày " + day)
        target = target_root / ("order_date=" + day)
        print("Ghi:", target)
        part.write.mode("overwrite").parquet(str(target))
    run_day("2025-01-01")
    run_day("2025-01-03")
    print("Đọc cả hai ngày:", spark.read.parquet(str(target_root)).count())
finally:
    spark.stop()
