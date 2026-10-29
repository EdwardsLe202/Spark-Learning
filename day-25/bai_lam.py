"""Ngày 25: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 25
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-25").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tự thử chạy lại ngày 3 với overwrite, đối soát số dòng và tổng.
    # 2. Dùng một đích append thử riêng để thấy cùng hai đơn ghi hai lần thành 4 dòng. Không dùng đích chính.
    # 3. Thêm O009/C005/2025-01-03/20000/completed vào bản nguồn DataFrame bằng unionByName.
    # 4. Xử lý lại đầy đủ ngày 3 từ nguồn mới, kiểm tra ngày 1 không đổi. Không ghi sửa data/beginner/orders.csv.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
