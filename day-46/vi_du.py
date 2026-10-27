"""Ngày 46: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 46 --example
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
    out = output(46, exercise=False)
    with spark_session("course-day-46", delta=False) as spark:
        orders = orders_df(spark)
        events = events_df(spark, "events_tiny.csv")
        start = F.to_timestamp(F.lit("2025-01-20T00:00:00Z"))
        end = F.to_timestamp(F.lit("2025-01-21T00:00:00Z"))
        result = events.filter((F.col("event_ts") >= start) & (F.col("event_ts") < end))
        result.select("event_id", "event_ts", "available_ts").show(truncate=False)


if __name__ == "__main__":
    main()
