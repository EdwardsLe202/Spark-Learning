"""Ngày 08: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 08
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-08") as spark:
        words = spark.sparkContext.parallelize(["spark sql", "spark ml", "sql"], 2)
        counts = words.flatMap(lambda s: s.split()).map(lambda w: (w, 1)).reduceByKey(lambda a, b: a + b)
        print(sorted(counts.collect()))
        df = spark.range(20).repartition(4)
        print("repartition:", df.rdd.getNumPartitions())
        print("coalesce:", df.coalesce(2).rdd.getNumPartitions())

# Bài tự làm hôm nay:
# TODO Chạy word count và giải thích kiểu dữ liệu sau từng phép biến đổi.
# TODO Viết lại bằng DataFrame: split → explode → groupBy → count; đối chiếu từ và số lần.
# TODO Đổi repartition thành 2, 4, 8 và xem plan/UI. Ghi số partition trước sau coalesce(2).
# TODO Ghi mỗi biến thể vào một đích riêng; so số part-file nhưng không kết luận luôn một file cho mọi cấu hình.
# TODO Viết kịch bản task gửi email rồi bị retry. Đề xuất khóa chống gửi lặp, không thực sự gửi email.
