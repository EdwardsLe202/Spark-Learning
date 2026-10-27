"""Ngày 54: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 54 --example
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
    out = output(54, exercise=False)
    with spark_session("course-day-54", delta=False) as spark:
        orders = orders_df(spark)
        df = spark.createDataFrame([("2025-01-01T10:00:00Z", 1), ("2025-01-01T10:04:00Z", 2), ("2025-01-01T10:05:00Z", 3)], "time string, value long").withColumn("ts", F.to_timestamp("time"))
        df.groupBy(F.window("ts", "5 minutes")).agg(F.sum("value").alias("total")).orderBy("window").show(truncate=False)


if __name__ == "__main__":
    main()
