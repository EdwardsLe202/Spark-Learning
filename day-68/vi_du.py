"""Ngày 68: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 68 --example
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
    out = output(68, exercise=False)
    with spark_session("course-day-68", delta=False) as spark:
        orders = orders_df(spark)
        from pyspark.ml import Pipeline
        from pyspark.ml.feature import Imputer, VectorAssembler, StandardScaler
        train = spark_snapshot(spark)
        pipeline = Pipeline(stages=[Imputer(inputCols=["recency_days"], outputCols=["recency_filled"]), VectorAssembler(inputCols=["events_30d", "spend_30d", "recency_filled"], outputCol="raw_features"), StandardScaler(inputCol="raw_features", outputCol="features", withMean=False)])
        model = pipeline.fit(train)
        model.transform(train).select("raw_features", "features").show(3, truncate=False)


if __name__ == "__main__":
    main()
