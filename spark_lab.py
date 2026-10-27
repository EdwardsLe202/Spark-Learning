"""Tiện ích của lộ trình tổng hợp cũ; khóa nền mới không cần import file này.
Bản tham khảo độc lập được giữ trong tham_khao/lo_trinh_tong_hop.
"""
from contextlib import contextmanager
from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def output_dir(day):
    path = ROOT / "artifacts" / f"day-{int(day):02d}"
    path.mkdir(parents=True, exist_ok=True)
    return path


@contextmanager
def spark_session(name="spark-learning"):
    # Worker Python cần cùng interpreter với driver.
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    from pyspark.sql import SparkSession
    spark = (SparkSession.builder.master("local[2]").appName(name)
             .config("spark.sql.session.timeZone", "UTC")
             .config("spark.sql.shuffle.partitions", "4")
             .config("spark.driver.memory", "1g")
             .getOrCreate())
    spark.sparkContext.setLogLevel("WARN")
    try:
        yield spark
    finally:
        spark.stop()


def read_events(spark, filename="events.csv"):
    from pyspark.sql.types import StructType, StructField, StringType
    fields = ["event_id", "customer_id", "event_time", "ingested_at", "amount", "event_type"]
    schema = StructType([StructField(c, StringType(), True) for c in fields])
    # Đọc chuỗi trước để người học chủ động parse và tách bản ghi lỗi.
    return spark.read.option("header", True).schema(schema).csv(str(DATA / "raw" / filename))


def read_customers(spark):
    return spark.read.option("header", True).schema(
        "customer_id string, region string, plan string, signup_date date"
    ).csv(str(DATA / "raw" / "customers.csv"))
