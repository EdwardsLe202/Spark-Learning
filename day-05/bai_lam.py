"""Ngày 05: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 05
"""
import os
import sys
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
spark = SparkSession.builder.master("local[2]").appName("beginner-day-05").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tạo lại bảng ba đơn có schema tường minh trong bai_lam.py.
    # 2. Thêm cột status kiểu string, điền completed vào cả ba tuple.
    # 3. In schema và tên cột, kiểm tra mỗi tuple có bốn giá trị theo đúng thứ tự.
    # 4. Thử sai kiểu amount="abc" trên bản thử, ghi vì sao Spark từ chối; sửa về số để chương trình chạy lại.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
