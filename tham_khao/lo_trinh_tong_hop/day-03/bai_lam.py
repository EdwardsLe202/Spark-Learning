"""Ngày 03: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 03
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-03") as spark:
        df = spark.range(0, 100, 1, 4)
        result = df.withColumn("bucket", F.col("id") % 3).groupBy("bucket").count()
        result.explain("formatted")
        result.orderBy("bucket").show()
        print("Partition đầu vào:", df.rdd.getNumPartitions())

# Bài tự làm hôm nay:
# TODO Trước khi chạy, tính tay số phần tử chia hết cho 3 từ 0 tới 99.
# TODO Chạy ví dụ; ghi nơi có `Exchange` và giải thích vì sao phải nhóm các khóa.
# TODO Thêm hai action `count()` rồi `show()`. Xem Spark UI khi giữ phiên bằng `input()`; ghi số job thực tế, không đoán một action luôn bằng đúng một job.
# TODO Đổi số partition đầu vào từ 4 thành 2 rồi 8. Đối chiếu task và kết quả.
# TODO Vẽ quan hệ application → job → stage → task vào phần comment trong `bai_lam.py`.
