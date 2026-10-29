"""Ngày 26: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 26
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-26").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    # Phần đọc đầu vào được giải thích từ ngày 06.
    orders = (spark.read.option("header", True)
              .schema("order_id string, customer_id string, order_date string, amount long, status string")
              .csv(str(DATA / "orders.csv")))
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")
    orders.show(truncate=False)

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Viết lại lọc completed → nhóm status → tổng tiền, gọi explain rồi show.
    # 2. Chỉ ra filter/groupBy là transformation; show/count/write là action.
    # 3. So kết quả với ngày 10 để xác nhận thêm explain không đổi số liệu.
    # 4. Bổ sung nếu muốn: giữ phiên bằng input trước stop để mở UI theo địa chỉ log.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
