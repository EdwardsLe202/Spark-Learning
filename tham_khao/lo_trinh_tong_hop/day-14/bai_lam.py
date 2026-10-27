"""Ngày 14: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 14
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-14") as spark:
        # Ví dụ giới hạn trước khi đưa dữ liệu nhỏ về driver.
        small = read_events(spark, "events_tiny.csv").select("customer_id", "amount").limit(10001)
        if small.count() > 10000:
            raise ValueError("Vượt giới hạn lab 10.000 dòng; cần lấy mẫu hoặc xuất shard")
        print(small.toPandas())

# Bài tự làm hôm nay:
# TODO Cài requirements-ml.txt. Xuất ba snapshot ngày 11 thành CSV nhỏ hoặc Parquet và đọc bằng pandas.
# TODO Trong bai_lam.py, ghép SimpleImputer, OneHotEncoder(handle_unknown="ignore"), ColumnTransformer và LogisticRegression thành sklearn Pipeline. Fit chỉ train.
# TODO Đánh giá validation bằng precision/recall và average_precision_score; ghi rõ đây là AP của sklearn, không mặc định bằng areaUnderPR của Spark.
# TODO Lưu pipeline bằng joblib vào artifacts/day-14/model.joblib, kèm input_example.json, feature_schema.json, model_metadata.json có code/data version. Load trong tiến trình mới và so xác suất.
# TODO Giữ ba feature số events_30d, spend_30d, recency_days và hai cột region, plan làm contract cho API ngày 21.
