"""Ngày 23: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 23
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
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Viết lại chuỗi làm sạch vào bai_lam.py theo từng bước, kiểm tra count sau mỗi bước.
    # 2. Bổ sung error_reason cho lỗi cơ bản bằng when: thiếu khách, tiền lỗi, tiền âm, ngày lỗi.
    # 3. Ghi clean và dữ liệu lỗi ra hai đích Parquet riêng dưới artifacts/beginner/day-23/exercise.
    # 4. Đối soát 10=5+1+1+3 và đọc lại clean để kiểm tra tổng 390000.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
