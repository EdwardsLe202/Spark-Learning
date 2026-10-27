"""Ngày 32: khung tự làm; đọc thuc_hanh.md, chưa phải lời giải.
Chạy: python scripts/run_day.py 32
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
    out = output(32, exercise=True)
    with spark_session("course-day-32", delta=False) as spark:
        orders = orders_df(spark)
        print("Khung bài làm: hãy tự thực hiện từng bước; chưa có kết quả nghiệm thu.")
        # 1. Thêm input trước stop trong bai_lam.py, mở UI theo URL thật.
        # 2. Chạy count rồi show; đối chiếu job/stage/task với code.
        # 3. Đổi numPartitions=2, ghi quan sát và giữ nguyên kết quả.

        # Viết phần xử lý của bạn bên dưới.


if __name__ == "__main__":
    main()
