"""Ngày 30: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 30
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-30").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # A. Lọc đơn completed có amount >=150000; tính số đơn và tổng tiền.
    # B. Tạo báo cáo completed cho tất cả khách, gồm người chưa có đơn. Lưu, đọc lại và kiểm tra.
    # C. Chọn đơn mới nhất mỗi khách theo order_date rồi order_id; giải thích tiêu chí phụ.
    # D. Tự chỉ ra một lỗi bạn đã mắc, cách kiểm tra phát hiện và phần cần học tiếp.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
