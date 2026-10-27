"""Ngày 70: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 70 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
from course_support import (spark_session, orders_df, events_df, spark_snapshot, build_features_spark, spark_ml_pipeline, stream_workspace, write_stream_file, file_stream, run_file_stream)
from pyspark.sql import functions as F, Window

def main():
    out = output(70, exercise=False)
    with spark_session("course-day-70", delta=False) as spark:
        orders = orders_df(spark)
        train, val = spark_snapshot(spark), spark_snapshot(spark, "2025-04-01")
        pipeline = spark_ml_pipeline(reg_param=0.1)
        model = pipeline.fit(train)
        predicted = model.transform(val)
        predicted.select("customer_id", "label", "probability", "prediction").show(5, truncate=False)
        assert predicted.count() == 120


if __name__ == "__main__":
    main()
