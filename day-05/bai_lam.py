"""Ngày 05: schema tường minh, thêm status và nhận diện sai kiểu.
Chạy từ gốc repo: uv run python scripts/run_day.py 05
"""
import os
import sys
from pyspark.sql import SparkSession
from pyspark.errors import PySparkTypeError

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
spark = SparkSession.builder.master("local[2]").appName("beginner-day-05").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    schema = "order_id string, customer_id string, amount long, status string"
    rows = [
        ("O001", "C001", 100000, "completed"),
        ("O002", "C001", 200000, "completed"),
        ("O003", "C002", 50000, "completed"),
    ]
    orders = spark.createDataFrame(rows, schema)
    orders.printSchema()
    print("Tên cột:", orders.columns)
    print("Số giá trị trong từng tuple:", [len(row) for row in rows])  # [4, 4, 4]
    orders.orderBy("order_id").show()

    # Chỉ thử sai kiểu trên dữ liệu riêng, không sửa bảng hợp lệ phía trên.
    try:
        spark.createDataFrame([("O004", "C002", "abc", "completed")], schema)
    except PySparkTypeError as exc:
        print("Lỗi sai kiểu dự kiến:", exc)
        print("amount được khai báo long nên không nhận chuỗi abc; cần truyền số nguyên.")
    else:
        raise AssertionError("Spark phải từ chối chuỗi abc với schema amount long.")

    corrected = spark.createDataFrame([("O004", "C002", 70000, "completed")], schema)
    print("Bản thử sau khi sửa amount thành số nguyên:")
    corrected.show()
finally:
    spark.stop()
