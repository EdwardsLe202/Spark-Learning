"""Ngày 17: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 17 --example
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-17").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))

    # NỘI DUNG HỌC HÔM NAY
    orders.createOrReplaceTempView("orders_view")
    result = spark.sql("""
        SELECT customer_id, SUM(amount) AS total_amount
        FROM orders_view
        WHERE status = 'completed'
        GROUP BY customer_id
        ORDER BY customer_id
    """)
    result.show()
finally:
    spark.stop()
