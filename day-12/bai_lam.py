"""Ngày 12: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 12
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-12").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tự tạo lại bảng mẫu và loại trùng toàn dòng.
    # 2. Thêm đơn O003 của cùng khách cũ theo một bảng bạn tạo; giải thích vì sao mã đơn mới không tự là duplicate.
    # 3. Tạo hai dòng cùng order_id nhưng amount khác nhau. Viết vào ghi chú vì sao chưa thể tự chọn đúng bản chỉ từ khóa.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
