"""Ngày 39: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 39 --example
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
    out = output(39, exercise=False)
    with spark_session("course-day-39", delta=False) as spark:
        orders = orders_df(spark)
        old = spark.conf.get("spark.sql.adaptive.enabled")
        try:
            for enabled in ["false", "true"]:
                spark.conf.set("spark.sql.adaptive.enabled", enabled)
                result = orders.groupBy("customer_id").agg(F.sum("amount").alias("total"))
                result.collect()  # chỉ 4 dòng kết quả
                print("AQE:", enabled)
                result.explain("formatted")
        finally:
            spark.conf.set("spark.sql.adaptive.enabled", old)


if __name__ == "__main__":
    main()
