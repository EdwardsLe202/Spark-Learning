"""Ngày 25: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 25 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-25").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    target_root = ROOT / "artifacts/beginner/day-25/daily"
    def run_day(day, source):
        part = source.filter(F.col("order_date") == day)
        part.write.mode("overwrite").parquet(str(target_root / ("order_date=" + day)))
    run_day("2025-01-01", orders)
    run_day("2025-01-03", orders)
    run_day("2025-01-03", orders)
    loaded = spark.read.parquet(str(target_root))
    print("Sau chạy lại:", loaded.count(), loaded.agg(F.sum("amount")).first()[0])
finally:
    spark.stop()
