"""Ngày 10: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 10
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-10") as spark:
        df = read_events(spark, "events_tiny.csv").withColumn("event_date", F.to_date(F.to_timestamp("event_time")))
        for day in ["2025-01-02", "2025-01-15", "2025-01-20", "2025-01-15"]:
            target = output_dir(10) / "daily" / f"event_date={day}"
            # Nguồn tiny độc lập với đích nên không tự overwrite nguồn đang đọc.
            df.filter(F.col("event_date") == day).drop("event_date").write.mode("overwrite").parquet(str(target))
        print("Đã chạy ba ngày và chạy lại ngày 15.")

# Bài tự làm hôm nay:
# TODO Chạy batch mẫu và đọc toàn daily, đối chiếu 3 dòng duy nhất. Lần chạy lại ngày 15 không thêm dòng.
# TODO Tạo bản nguồn bổ sung một sự kiện ngày 15 có ingested_at muộn, dựng lại riêng ngày đó và kiểm tra ngày khác không đổi.
# TODO Tạo `artifacts/day-10/stream_in`, chép một file CSV vào đó. Dùng readStream với schema tường minh, header=true; writeStream format parquet, outputMode append, checkpointLocation riêng, trigger(availableNow=True), rồi awaitTermination().
# TODO Thêm file thứ hai tên mới, chạy lại cùng checkpoint và cùng đích. Đọc đích để đối soát; không sửa nội dung file đã được stream xử lý.
# TODO Lưu log hai lần chạy; giải thích khác nhau giữa giữ checkpoint và tạo truy vấn mới từ đầu.
