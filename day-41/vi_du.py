"""Ngày 41: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 41 --example
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
    out = output(41, exercise=False)
    with spark_session("course-day-41", delta=False) as spark:
        orders = orders_df(spark)
        df = spark.createDataFrame([('{"customer":{"id":"C001"},"items":["a","b"]}',), ('{"customer":{"id":"C002"},"items":[]}',)], "payload string")
        parsed = df.select(F.from_json("payload", "customer struct<id:string>, items array<string>").alias("data"))
        parsed.select("data.customer.id", F.explode("data.items").alias("item")).show()


if __name__ == "__main__":
    main()
