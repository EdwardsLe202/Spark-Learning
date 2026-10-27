"""Ngày 13: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 13
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
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tạo lại mẫu bốn dòng và ba nhãn error_reason.
    # 2. Tách clean có reason=ok và rejected có reason khác ok.
    # 3. Kiểm tra 4 đầu vào = 1 sạch + 3 lỗi.
    # 4. Thêm chuỗi "0" và kiểm tra được chấp nhận, không nhầm với thiếu.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
