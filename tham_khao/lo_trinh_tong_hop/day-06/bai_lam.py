"""Ngày 06: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 06
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-06") as spark:
        from pyspark.sql import Window
        w = Window.partitionBy("event_id").orderBy(F.col("ingested_at").desc(), F.col("amount").desc())
        latest = read_events(spark, "events_dirty.csv").withColumn("rn", F.row_number().over(w)).filter("rn = 1")
        latest.filter("event_id = 'D002'").show()
        customers = read_customers(spark)
        print("Số khóa customer:", customers.select("customer_id").distinct().count())

# Bài tự làm hôm nay:
# TODO Join tiny với customers theo customer_id, tổng hợp tiền theo region. Đối soát tổng tiền trước sau join.
# TODO Cố tình nhân bản dòng C001 trong bảng customers, join lại và ghi vì sao tổng tiền sai. Thêm kiểm tra phát hiện khóa trùng trước khi ghép.
# TODO Viết left anti join để tìm customer không tồn tại trong dirty.
# TODO Dùng row_number giữ D002 mới nhất. Thêm fixture hai dòng bằng timestamp và chốt tiêu chí phụ rõ ràng.
# TODO Tính lag amount theo customer_id, sắp xếp event_time và event_id; giải thích dòng đầu có NULL. Viết tay sự khác nhau giữa ba giao dịch và ba ngày.
