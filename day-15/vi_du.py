"""Ngày 15: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 15 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-15").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    dated = orders.withColumn("order_day", F.to_date("order_date", "yyyy-MM-dd"))
    result = dated.filter((F.col("order_day") >= F.lit("2025-01-03").cast("date")) & (F.col("order_day") < F.lit("2025-01-06").cast("date")))
    result.select("order_id", "order_day").show()
    print("Số đơn:", result.count())
finally:
    spark.stop()
