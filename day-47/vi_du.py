"""Ngày 47: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 47 --example
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
    out = output(47, exercise=False)
    with spark_session("course-day-47", delta=False) as spark:
        orders = orders_df(spark)
        versions = spark.createDataFrame([("E1", "2025-01-01", 100), ("E1", "2025-01-03", 200)], "event_id string, available_date string, amount long")
        known = versions.filter(F.col("available_date") < "2025-01-02")
        window = Window.partitionBy("event_id").orderBy(F.col("available_date").desc(), F.col("amount").desc())
        known.withColumn("rn", F.row_number().over(window)).filter("rn = 1").show()


if __name__ == "__main__":
    main()
