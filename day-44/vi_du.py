"""Ngày 44: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 44 --example
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
    out = output(44, exercise=False)
    with spark_session("course-day-44", delta=True) as spark:
        orders = orders_df(spark)
        target = out / "orders_delta"
        orders.write.format("delta").mode("overwrite").save(str(target))
        from delta.tables import DeltaTable
        table = DeltaTable.forPath(spark, str(target))
        version = table.history(1).select("version").first()[0]
        table.delete("order_id = 'O004'")
        print("Hiện tại:", spark.read.format("delta").load(str(target)).count())
        print("Trước xóa:", spark.read.format("delta").option("versionAsOf", version).load(str(target)).count())


if __name__ == "__main__":
    main()
