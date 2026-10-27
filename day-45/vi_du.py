"""Ngày 45: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 45 --example
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
    out = output(45, exercise=False)
    with spark_session("course-day-45", delta=False) as spark:
        orders = orders_df(spark)
        from time import perf_counter
        records = []
        for i in range(3):
            start = perf_counter()
            result = orders.filter(F.col("status") == "completed").groupBy("customer_id").agg(F.sum("amount").alias("total"))
            rows = result.orderBy("customer_id").collect()
            records.append({"trial": i + 1, "seconds": perf_counter() - start, "total": sum(r.total for r in rows)})
        write_json(out / "baseline.json", records)
        print(records)


if __name__ == "__main__":
    main()
