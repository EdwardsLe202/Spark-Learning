"""Ngày 04: tạo bảng ba đơn, thêm O004 và dùng tên my_orders.
Chạy từ gốc repo: uv run python scripts/run_day.py 04
"""
import os
import sys
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
spark = SparkSession.builder.master("local[2]").appName("beginner-day-04").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # SparkSession là phiên làm việc; my_orders là bảng trong phiên đó.
    rows = [
        ("O001", "C001", 100000),
        ("O002", "C001", 200000),
        ("O003", "C002", 50000),
    ]
    my_orders = spark.createDataFrame(rows, ["order_id", "customer_id", "amount"])
    print("Bảng ban đầu:")
    my_orders.orderBy("order_id").show()
    print("Số dòng ban đầu:", my_orders.count())  # 3

    # Sửa danh sách Python không tự thay đổi DataFrame đã tạo.
    # Tạo lại bảng từ danh sách bốn đơn, vẫn dùng tên my_orders nhất quán.
    rows.append(("O004", "C002", 70000))
    my_orders = spark.createDataFrame(rows, ["order_id", "customer_id", "amount"])
    print("Sau khi thêm O004:")
    my_orders.orderBy("order_id").show()
    print("Số dòng mới:", my_orders.count())  # 4
finally:
    spark.stop()
