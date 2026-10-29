"""Ngày 06: đọc CSV, phân biệt header và dữ liệu, thử lỗi đường dẫn.
Chạy từ gốc repo: uv run python scripts/run_day.py 06
"""
import os
import sys
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.errors import AnalysisException

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "beginner"
spark = SparkSession.builder.master("local[2]").appName("beginner-day-06").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    orders.orderBy("order_id").show(truncate=False)
    orders.printSchema()
    print("Tên cột:", orders.columns)
    print("Số đơn (không tính header):", orders.count())  # 8

    # Đếm dòng văn bản chỉ để đối chiếu fixture này: mỗi đơn nằm trên một dòng.
    with (DATA / "orders.csv").open(encoding="utf-8") as source:
        header = source.readline().strip()
        physical_lines = 1 + sum(1 for _ in source)
    print("Header:", header)
    print("Số dòng vật lý, tính cả header:", physical_lines)  # 9
    print("O004: khách C003, ngày 2025-01-04, 300000 đồng, cancelled (đã hủy).")

    # Thử một đường dẫn sai riêng; bảng orders vẫn đọc từ file chuẩn.
    try:
        spark.read.option("header", True).csv(str(DATA / "__missing_day_06__.csv"))
    except AnalysisException as exc:
        if exc.getErrorClass() != "PATH_NOT_FOUND":
            raise
        print("Lỗi đường dẫn dự kiến:", exc)
    else:
        raise AssertionError("Bản thử cần một đường dẫn không tồn tại.")
    print("Đường dẫn đúng:", DATA / "orders.csv")
    print("Bảng chuẩn vẫn có", orders.count(), "đơn; không cần đổi tên cột để sửa lỗi đường dẫn.")
finally:
    spark.stop()
