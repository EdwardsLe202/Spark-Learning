"""Ngày 09: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 09
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-09") as spark:
        from time import perf_counter
        df = spark.range(100000).withColumn("key", F.when(F.col("id") < 90000, 0).otherwise(F.col("id") % 10))
        t0 = perf_counter()
        summary = df.groupBy("key").count()
        rows = summary.orderBy("key").collect()  # Chỉ có tối đa 10 dòng.
        print("seconds:", round(perf_counter() - t0, 3))
        print(rows)
        summary.explain("formatted")

# Bài tự làm hôm nay:
# TODO Chạy một lần warm up (khởi động nóng), rồi đo baseline ba lần. Ghi cấu hình máy, số dòng và từng thời gian.
# TODO Join bảng lớn giả lập với bảng 10 khóa; so plan mặc định và F.broadcast ở bảng nhỏ. Chỉ thay yếu tố này.
# TODO Kiểm tra số dòng, tổng id và kết quả theo key giữa hai phiên bản.
# TODO Đo trường hợp một DataFrame dùng ba lần với cache và không cache; tính cả chi phí action vật hóa cache.
# TODO Tạo bảng báo cáo gồm cấu hình, median runtime, loại join, shuffle quan sát được và nhận xét giới hạn local.
