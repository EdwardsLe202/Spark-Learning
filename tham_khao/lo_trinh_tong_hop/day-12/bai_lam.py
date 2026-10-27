"""Ngày 12: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 12
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-12") as spark:
        from pyspark.ml import Pipeline
        from pyspark.ml.feature import VectorAssembler
        from pyspark.ml.classification import LogisticRegression
        train = spark.createDataFrame([(1.0,0.0),(2.0,0.0),(3.0,1.0),(4.0,1.0)], "events_30d double, label double")
        pipeline = Pipeline(stages=[VectorAssembler(inputCols=["events_30d"], outputCol="features"), LogisticRegression(maxIter=10)])
        model = pipeline.fit(train)
        model.transform(train).select("events_30d", "probability", "prediction").show(truncate=False)
        # Đây chỉ là dữ liệu minh họa API; chưa phải model churn của dự án.

# Bài tự làm hôm nay:
# TODO Chạy ví dụ và phân loại từng stage là estimator hay transformer.
# TODO Thay train minh họa bằng snapshot train ngày 11; giữ validation và test độc lập. Đổi cột churn sang label kiểu double nếu cần.
# TODO Thêm Imputer cho recency, StringIndexer và OneHotEncoder cho plan/region, VectorAssembler và LogisticRegression. Chốt thứ tự các feature.
# TODO Fit chỉ train, transform validation; lưu PipelineModel vào artifacts/day-12/model. Viết phần load bằng PipelineModel.load và chạy ở tiến trình mới.
# TODO Thử category lạ trên bản sao fixture, kiểm tra không lỗi và lưu dự đoán trước/sau load để đối chiếu.
