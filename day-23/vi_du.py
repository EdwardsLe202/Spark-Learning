"""Ngày 23: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: python scripts/run_day.py 23 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-23").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:

    # NỘI DUNG HỌC HÔM NAY
    spark.conf.set("spark.sql.ansi.enabled", "false")
    raw = spark.read.option("header", True).schema("order_id string, customer_id string, order_date string, amount string, status string").csv(str(DATA / "orders_dirty.csv"))
    parsed = raw.withColumn("amount_num", F.col("amount").cast("long")).withColumn("order_day", F.to_date("order_date", "yyyy-MM-dd"))
    valid = F.col("customer_id").isNotNull() & (F.col("customer_id") != "") & F.col("amount_num").isNotNull() & (F.col("amount_num") >= 0) & F.col("order_day").isNotNull()
    candidates = parsed.filter(valid)
    basic_errors = parsed.filter(~valid)
    unique = candidates.distinct()
    customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
    unknown = unique.join(customers.select("customer_id"), "customer_id", "left_anti")
    clean = unique.join(customers.select("customer_id"), "customer_id", "inner")
    print("raw/basic_errors/candidates/unique/unknown/clean:", raw.count(), basic_errors.count(), candidates.count(), unique.count(), unknown.count(), clean.count())
    clean.select("order_id", "customer_id", "amount_num").show()
finally:
    spark.stop()
