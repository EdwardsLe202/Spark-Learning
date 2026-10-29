"""Ngày 11: bài tự làm. Đọc thuc_hanh.md trước khi viết code.
Chạy từ gốc repo: uv run python scripts/run_day.py 11
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
spark = SparkSession.builder.master("local[2]").appName("beginner-day-11").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
try:
    print("Đây là khung bài làm; chạy được khung chưa có nghĩa đã làm xong.")

    # BẮT ĐẦU VIẾT BÀI CỦA BẠN Ở ĐÂY
    # 1. Tạo đúng bảng A/B/C như ví dụ trong bai_lam.py.
    # 2. Tách missing và known, in cả hai để thấy C=0 thuộc known.
    # 3. Tạo bản filled bằng fillna amount=0, kiểm tra nguồn orders vẫn có NULL.
    # 4. Viết một câu vì sao chưa biết tiền thì không nên mặc định coi như khách mua miễn phí.
    # KẾT THÚC VÙNG BÀI LÀM
finally:
    spark.stop()
