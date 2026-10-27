"""Ngày 06: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: python scripts/run_day.py 06
"""
import os
import sys
from pathlib import Path
from pyspark.sql import SparkSession

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
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Mở orders.csv bằng trình soạn thảo và tìm dòng tên cột.
    # 2. Chạy ví dụ, tìm O004 và mô tả trạng thái của nó.
    # 3. Trong bai_lam.py, in tên cột và số đơn. Viết vào ghi chú file có bao nhiêu dòng vật lý nếu tính cả header.
    # 4. Đổi đường dẫn sang tên file không tồn tại trên bản thử để nhận ra lỗi đường dẫn; sửa lại sau đó.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
