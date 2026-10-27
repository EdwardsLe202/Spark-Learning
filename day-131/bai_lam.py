"""Ngày 131: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 131
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
    out = output(131, exercise=True)
    with spark_session("course-day-131", delta=False) as spark:
        orders = orders_df(spark)
        print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
        # 1. Xuất manifest chunk_id/hash/model_revision cho job cần tính.
        # 2. Worker embed batch nhỏ bằng model thật, retry tối đa 2 và ghi trạng thái.
        # 3. Gây lỗi giữa lô, restart không ghi trùng hoặc mất chunk.

        # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
