"""Ngày 07: chọn ba cột và đổi amount thành money_vnd.
Chạy từ gốc repo: uv run python scripts/run_day.py 07
"""
import os
import sys
from pathlib import Path
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "beginner"
spark = SparkSession.builder.master("local[2]").appName("beginner-day-07").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    # alias đặt tên cột trong bảng kết quả, không đổi cột của bảng nguồn.
    result = orders.select("customer_id", "order_date", orders["amount"].alias("money_vnd"))
    result.orderBy("customer_id", "order_date", "money_vnd").show(truncate=False)
    print("Cột nguồn:", orders.columns)
    print("Số dòng nguồn:", orders.count())  # 8
    print("Cột kết quả:", result.columns)
    print("Số dòng kết quả:", result.count())  # 8
    print("Kết quả còn 3 cột; amount được đặt tên money_vnd. Nguồn vẫn giữ 5 cột.")
    print("select chỉ chọn cột, không lọc dòng nên cả hai bảng vẫn có 8 đơn.")
finally:
    spark.stop()
