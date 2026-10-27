"""Ngày 131: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 131 --example
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
    out = output(131, exercise=False)
    with spark_session("course-day-131", delta=False) as spark:
        orders = orders_df(spark)
        from rag_support import load_corpus, chunk_documents
        chunks = chunk_documents(load_corpus())
        rows = [(c["chunk_id"], c["content_hash"], c["text"]) for c in chunks]
        df = spark.createDataFrame(rows + rows[:1], "chunk_id string, content_hash string, text string")
        clean = df.dropDuplicates(["chunk_id", "content_hash"])
        print("Trước/sau:", df.count(), clean.count())
        clean.write.mode("overwrite").parquet(str(out / "embedding_jobs"))


if __name__ == "__main__":
    main()
