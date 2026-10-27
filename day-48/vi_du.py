"""Ngày 48: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 48 --example
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
    out = output(48, exercise=False)
    with spark_session("course-day-48", delta=True) as spark:
        orders = orders_df(spark)
        from delta.tables import DeltaTable
        path = out / "events"
        spark.createDataFrame([("E1", 100), ("E2", 50)], "event_id string, amount long").write.format("delta").mode("overwrite").save(str(path))
        changes = spark.createDataFrame([("E1", 120), ("E3", 70)], "event_id string, amount long")
        for _ in range(2):
            DeltaTable.forPath(spark, str(path)).alias("t").merge(changes.alias("s"), "t.event_id = s.event_id").whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
        result = spark.read.format("delta").load(str(path))
        result.show()
        assert result.count() == 3


if __name__ == "__main__":
    main()
