"""Ngày 79: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 79 --example
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
    out = output(79, exercise=False)
    with spark_session("course-day-79", delta=False) as spark:
        orders = orders_df(spark)
        train = spark_snapshot(spark)
        target = out / "train_shards"
        train.repartition(2).write.mode("overwrite").parquet(str(target))
        write_json(out / "manifest.json", {"split": "train", "rows": 120, "snapshot": "2025-02-01", "format": "parquet"})
        print("Số part-file:", len(list(target.glob("part-*"))))


if __name__ == "__main__":
    main()
