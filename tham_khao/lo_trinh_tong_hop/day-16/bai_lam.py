"""Ngày 16: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 16
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-16") as spark:
        from pyspark.sql import Window
        # Fixture cố ý có khóa trùng: kiểm tra này phải phát hiện lỗi.
        df = spark.createDataFrame([("C001", 1), ("C001", 2)], "customer_id string, value int")
        duplicates = df.groupBy("customer_id").count().filter("count > 1")
        print("Khóa bị trùng:", duplicates.count())
        # TODO: biến kiểm tra thành hàm validate_unique(df, keys) và viết pytest cho nó.

# Bài tự làm hôm nay:
# TODO Tạo `projects/02-mlops/churn/` với __init__.py, features.py, train.py, predict.py và cli.py. Tách logic đã làm thành hàm có tham số.
# TODO Viết CLI nhận --snapshot-date, --input và --output. Log cấu hình, không log dữ liệu nhạy cảm.
# TODO Tạo tests/ dưới project, dùng pytest và fixture Spark local[2] có stop trong teardown. Dùng tmp_path làm đích ghi thử.
# TODO Viết ít nhất 5 test: expected feature trên tiny, sự kiện tương lai bị loại, ingested_at muộn bị loại, khóa dimension trùng bị chặn, rerun không tăng số dòng.
# TODO Cố tình sửa biên `< cutoff` thành `<= cutoff` và thêm fixture đúng cutoff để chứng minh test thất bại; hoàn nguyên và chạy xanh.
