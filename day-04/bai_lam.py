"""Ngày 04: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 04
"""
import os
import sys
from pyspark.sql import SparkSession

# Dùng cùng Python cho các phần xử lý; giữ phần này trong những bài đầu.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
spark = SparkSession.builder.master("local[2]").appName("beginner-day-04").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Chạy vi_du.py bằng lệnh trong bài này, tìm đúng ba dòng đơn hàng giữa các dòng log.
    # 2. Sao chép ba dòng rows/createDataFrame/show vào vùng tự làm của bai_lam.py.
    # 3. Thêm O004, C002, 70000 và in lại bảng/count.
    # 4. Đổi tên biến orders thành my_orders nhất quán; kiểm tra vẫn chạy.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
