"""Ngày 72: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 72 --example
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
    out = output(72, exercise=False)
    with spark_session("course-day-72", delta=False) as spark:
        orders = orders_df(spark)
        from pyspark.ml import PipelineModel
        from pyspark.ml.functions import vector_to_array
        train = spark_snapshot(spark)
        model = spark_ml_pipeline().fit(train)
        path = out / "pipeline"
        model.write().overwrite().save(str(path))
        loaded = PipelineModel.load(str(path))
        print("Đọc lại:", loaded.transform(train.limit(2)).select(vector_to_array("probability")[1].alias("score")).collect())


if __name__ == "__main__":
    main()
