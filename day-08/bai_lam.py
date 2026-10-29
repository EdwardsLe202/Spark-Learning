"""Ngày 08: lọc theo khách, kết hợp điều kiện và kiểm tra giá trị biên.
Chạy từ gốc repo: uv run python scripts/run_day.py 08
"""
import os
import sys
from pathlib import Path
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "beginner"
spark = SparkSession.builder.master("local[2]").appName("beginner-day-08").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    # 1. Dự đoán C001 có O001, O002, O008.
    customer_orders = orders.filter(orders["customer_id"] == "C001")
    print("Các đơn của C001 (dự đoán: O001, O002, O008):")
    customer_orders.orderBy("order_id").show(truncate=False)

    # 2. Mỗi điều kiện cần ngoặc; dùng & để yêu cầu đồng thời cả hai.
    at_least = orders.filter((orders["status"] == "completed") & (orders["amount"] >= 150000))
    above = orders.filter((orders["status"] == "completed") & (orders["amount"] > 150000))
    print("completed và amount >= 150000: O002, O005, O008")
    at_least.orderBy("order_id").show(truncate=False)
    print("completed và amount > 150000: O002, O008")
    above.orderBy("order_id").show(truncate=False)
    print("O005 bị loại khi dùng > vì amount = 150000, đúng bằng ngưỡng.")

    # 3. Lọc trạng thái riêng, không mang điều kiện amount từ bước trước.
    cancelled = orders.filter(orders["status"] == "cancelled")
    cancelled.orderBy("order_id").show(truncate=False)
    print("O004: khách C003, ngày 2025-01-04, trị giá 300000 đồng, đã hủy.")
finally:
    spark.stop()
