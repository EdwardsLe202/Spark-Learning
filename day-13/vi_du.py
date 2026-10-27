"""Ngày 13: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 13 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-13").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:

    # NỘI DUNG HỌC HÔM NAY
    spark.conf.set("spark.sql.ansi.enabled", "false")
    orders = spark.createDataFrame([("A", "100000"), ("B", "abc"), ("C", "-10000"), ("D", "")], "order_id string, amount_raw string")
    parsed = orders.withColumn("amount", F.col("amount_raw").cast("long"))
    result = parsed.withColumn("error_reason", F.when(F.col("amount").isNull(), "invalid_number").when(F.col("amount") < 0, "negative_amount").otherwise("ok"))
    result.show()
finally:
    spark.stop()
