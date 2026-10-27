"""Ngày 97: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 97 --example
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
    out = output(97, exercise=False)
    with spark_session("course-day-97", delta=False) as spark:
        orders = orders_df(spark)
        from pyspark.ml.functions import vector_to_array
        model = spark_ml_pipeline().fit(spark_snapshot(spark))
        features = build_features_spark(spark, "2025-07-01", include_labels=False)
        scored = model.transform(features).withColumn("score", vector_to_array("probability")[1]).withColumn("model_version", F.lit("spark-demo-v1"))
        result = scored.select("customer_id", "snapshot_date", "score", "prediction", "model_version")
        result.show(3)
        assert result.count() == 120


if __name__ == "__main__":
    main()
