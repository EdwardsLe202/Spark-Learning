"""Ngày 34: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 34 --example
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
    out = output(34, exercise=False)
    with spark_session("course-day-34", delta=False) as spark:
        orders = orders_df(spark)
        rdd = spark.sparkContext.parallelize(["spark sql", "spark ml", "sql"], 2)
        pairs = rdd.flatMap(lambda s: s.split()).map(lambda word: (word, 1))
        counts = pairs.reduceByKey(lambda a, b: a + b)
        print(sorted(counts.collect()))


if __name__ == "__main__":
    main()
