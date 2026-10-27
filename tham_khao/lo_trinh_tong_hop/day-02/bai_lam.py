"""Ngày 02: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 02
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-02") as spark:
        from spark_lab import output_dir
        out = output_dir(2) / "smoke_parquet"
        df = spark.createDataFrame([("A", 2), ("B", 3)], "name string, value int")
        assert df.agg(F.sum("value")).first()[0] == 5
        df.write.mode("overwrite").parquet(str(out))
        assert spark.read.parquet(str(out)).count() == 2
        print("Smoke check: 2 dòng, tổng = 5")

# Bài tự làm hôm nay:
# TODO Làm theo `docs/CAI_DAT.md`; dùng `uname -m`, `python --version` và `java -version` để ghi kiến trúc, Python và Java.
# TODO Cài duy nhất `requirements.txt` vào môi trường riêng, rồi chạy file khởi động.
# TODO Thêm kiểm tra schema và tổng sau khi đọc Parquet, không chỉ kiểm tra số dòng.
# TODO Mở terminal mới, kích hoạt lại môi trường và chạy lại. Kết quả phải giống nhau.
# TODO Khi cần xem UI, thêm `input("Enter để kết thúc")` bên trong khối có Spark, mở UI rồi mới Enter. Ghi một ảnh hoặc mô tả vào nhật ký.
