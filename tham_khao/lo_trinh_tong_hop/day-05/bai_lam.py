"""Ngày 05: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 05
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-05") as spark:
        dirty = read_events(spark, "events_dirty.csv")
        parsed = (dirty.withColumn("amount_num", F.col("amount").cast("long"))
                  .withColumn("event_ts", F.to_timestamp("event_time")))
        parsed.select("event_id", "customer_id", "amount_num", "event_ts").show(truncate=False)

# Bài tự làm hôm nay:
# TODO Đọc tám dòng dirty và tự đánh dấu lỗi trước khi viết code.
# TODO Tạo cột lý do theo thứ tự: thiếu customer_id, timestamp lỗi, amount không parse được, amount âm, customer không tồn tại. Dùng customers làm tập khóa tham chiếu.
# TODO Tách bản ghi lỗi và bản ghi ứng viên hợp lệ. Trong ứng viên, giữ mỗi event_id bản có ingested_at mới nhất; tra Window ở ngày 6 nếu cần.
# TODO Ghi clean và quarantine thành hai thư mục riêng dưới artifacts/day-05. Ghi số dòng trùng bị bỏ riêng.
# TODO Tạo báo cáo đối soát đầu vào = lỗi + bản trùng bị bỏ + đầu ra; tính tổng amount của clean.
