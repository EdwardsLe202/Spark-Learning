"""Ngày 04: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 04
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-04") as spark:
        df = read_events(spark, "events_tiny.csv").withColumn("amount", F.col("amount").cast("long"))
        result = df.filter(F.col("amount") >= 100000).select("event_id", "amount")
        result.orderBy("event_id").show()
        df.createOrReplaceTempView("events")
        spark.sql("SELECT event_id, amount FROM events WHERE amount >= 100000 ORDER BY event_id").show()

# Bài tự làm hôm nay:
# TODO Chạy ví dụ và đọc schema trước, sau khi cast.
# TODO Tự viết DataFrame và SQL để lấy giao dịch của C001, thêm `amount_k = amount / 1000`, đổi tên cột rõ ràng.
# TODO Tổng hợp số giao dịch và tổng tiền theo customer_id bằng cả hai cách; so sánh hai kết quả sau `orderBy`.
# TODO Thử đọc `events_dirty.csv`, lọc riêng dòng có amount gốc khác rỗng nhưng cast ra NULL. Lưu danh sách event_id.
# TODO Viết kết quả và giải thích tại sao không dùng vòng lặp Python qua toàn bảng.
