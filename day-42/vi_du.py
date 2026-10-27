"""Ngày 42: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 42 --example
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
    out = output(42, exercise=False)
    with spark_session("course-day-42", delta=False) as spark:
        orders = orders_df(spark)
        target = out / "by_date"
        orders.write.mode("overwrite").partitionBy("order_date").parquet(str(target))
        result = spark.read.parquet(str(target)).filter(F.col("order_date") == F.lit("2025-01-03").cast("date"))
        result.explain("formatted")
        print("Ngày 3:", result.count())


if __name__ == "__main__":
    main()
