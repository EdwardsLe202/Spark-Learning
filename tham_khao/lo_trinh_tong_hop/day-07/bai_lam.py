"""Ngày 07: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 07
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-07") as spark:
        df = read_events(spark, "events_tiny.csv").withColumn("event_date", F.to_date(F.to_timestamp("event_time")))
        out = output_dir(7) / "by_date"
        df.write.mode("overwrite").partitionBy("event_date").parquet(str(out))
        selected = spark.read.parquet(str(out)).filter("event_date = DATE '2025-01-20'")
        selected.explain("formatted")
        selected.show()

# Bài tự làm hôm nay:
# TODO Ghi tiny ra Parquet theo event_date. Liệt kê file và thư mục để thấy partition theo lưu trữ.
# TODO Đọc lại và lọc ngày 2025-01-20; tìm PartitionFilters trong plan.
# TODO Ghi append hai lần vào một đích thử khác, đo số dòng. Ghi overwrite tại chính đích thử rồi đọc lại để thấy phạm vi thay thế.
# TODO So sánh schema CSV đọc chuỗi và Parquet sau khi đã cast; đối chiếu tổng tiền theo ngày.
# TODO Ghi data dictionary: tên cột, kiểu, đơn vị tiền, múi giờ, khóa và quy tắc partition.
