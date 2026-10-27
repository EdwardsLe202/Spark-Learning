"""Ngày 55: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 55 --example
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
    out = output(55, exercise=False)
    with spark_session("course-day-55", delta=False) as spark:
        orders = orders_df(spark)
        path = stream_workspace(out)
        write_stream_file(path, "a.json", [{"event_id": "a", "event_time": "2025-01-01T10:00:00Z", "value": 1}])
        def save_batch(df, batch_id):
            df.write.mode("overwrite").parquet(str(path / "batches" / ("batch=" + str(batch_id))))
        query = file_stream(spark, path).writeStream.foreachBatch(save_batch).option("checkpointLocation", str(path / "checkpoint")).trigger(availableNow=True).start()
        query.awaitTermination()
        print("Đã ghi các batch ở", path / "batches")


if __name__ == "__main__":
    main()
