"""Ngày 11: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 11
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-11") as spark:
        cutoff = F.to_timestamp(F.lit("2025-02-01T00:00:00Z"))
        events = (read_events(spark, "events_tiny.csv")
                  .withColumn("event_ts", F.to_timestamp("event_time"))
                  .withColumn("available_ts", F.to_timestamp("ingested_at"))
                  .withColumn("amount", F.col("amount").cast("long")))
        history = events.filter((F.col("event_ts") >= cutoff - F.expr("INTERVAL 30 DAYS")) &
                                (F.col("event_ts") < cutoff) & (F.col("available_ts") < cutoff))
        history.groupBy("customer_id").agg(F.count("*").alias("events_30d"), F.sum("amount").alias("spend_30d")).show()

# Bài tự làm hôm nay:
# TODO Trước hết dùng tiny và ba khách hàng C001, C002, C003. Viết tay feature và nhãn tại cutoff 2025-02-01.
# TODO Hoàn thiện hàm nhận events, customers, cutoff và observed_until; từ chối tạo nhãn nếu chưa đủ 30 ngày tương lai. Tạo recency bằng datediff giữa ngày cutoff và ngày giao dịch gần nhất.
# TODO Thêm sự kiện tương lai giá trị rất lớn và một giao dịch lịch sử có ingested_at sau cutoff. Kiểm tra cả hai không làm đổi feature.
# TODO Chạy với events.csv và toàn bộ customers cho ba cutoff train/validation/test. Ghi ba thư mục Parquet riêng dưới artifacts/day-11, mỗi thư mục 120 dòng và khóa duy nhất.
# TODO Hoàn thành `projects/01-data-pipeline/README.md`: gắn code ngày 5–11, kiểm tra rerun, backfill, join và báo cáo chất lượng.
