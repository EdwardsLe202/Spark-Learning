"""Ngày 53: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 53 --example
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
    out = output(53, exercise=False)
    with spark_session("course-day-53", delta=False) as spark:
        orders = orders_df(spark)
        path = stream_workspace(out)
        write_stream_file(path, "a.json", [{"event_id": "a", "event_time": "2025-01-01T10:00:00Z", "value": 1}])
        source = file_stream(spark, path).withColumn("event_ts", F.to_timestamp("event_time"))
        result = source.withWatermark("event_ts", "10 minutes").groupBy(F.window("event_ts", "5 minutes")).agg(F.sum("value").alias("total"))
        query = result.writeStream.format("parquet").outputMode("append").option("path", str(path / "output")).option("checkpointLocation", str(path / "checkpoint")).trigger(availableNow=True).start()
        query.awaitTermination()
        print((query.lastProgress or {}).get("eventTime", {}))


if __name__ == "__main__":
    main()
