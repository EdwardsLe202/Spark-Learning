"""Ngày 38: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 38 --example
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
    out = output(38, exercise=False)
    with spark_session("course-day-38", delta=False) as spark:
        orders = orders_df(spark)
        small = spark.createDataFrame([("C001", "vip"), ("C002", "normal")], "customer_id string, tier string")
        regular = orders.join(small, "customer_id", "left")
        hinted = orders.join(F.broadcast(small), "customer_id", "left")
        regular.explain()
        hinted.explain()
        assert regular.count() == hinted.count() == 8


if __name__ == "__main__":
    main()
