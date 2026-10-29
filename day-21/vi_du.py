"""Ngày 21: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 21 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-21").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    from pyspark.sql import Window
    window = Window.partitionBy("customer_id").orderBy(F.col("order_date").desc(), F.col("order_id").desc())
    ranked = orders.withColumn("rn", F.row_number().over(window))
    ranked.select("customer_id", "order_id", "order_date", "rn").show()
    latest = ranked.filter(F.col("rn") == 1)
    latest.select("customer_id", "order_id").show()
finally:
    spark.stop()
