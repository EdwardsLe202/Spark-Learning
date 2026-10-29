"""Ngày 14: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 14
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-14").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Đóng file ví dụ, tự viết lại báo cáo trong bai_lam.py.
    # 2. Viết thêm báo cáo cancelled và đối soát cả số đơn lẫn tiền.
    # 3. Thử bỏ filter completed trên bản sai, chạy kiểm tra tổng để thấy lỗi bị bắt; rồi sửa lại.
    # 4. Giải thích từng bước bằng một câu, không chỉ ghi “chạy thành công”.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
