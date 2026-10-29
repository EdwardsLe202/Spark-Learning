"""Ngày 22: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 22 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-22").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    from pyspark.sql import Window
    window = Window.partitionBy("customer_id").orderBy("order_date", "order_id")
    frame = window.rowsBetween(Window.unboundedPreceding, Window.currentRow)
    result = orders.withColumn("previous_amount", F.lag("amount").over(window)).withColumn("running_amount", F.sum("amount").over(frame))
    result.filter(F.col("customer_id") == "C001").select("order_id", "amount", "previous_amount", "running_amount").show()
finally:
    spark.stop()
