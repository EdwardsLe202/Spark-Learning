"""Không đặt master local: spark-submit chọn Standalone/client mode."""
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("course-standalone-smoke").getOrCreate()
try:
    orders = spark.read.option("header", True).schema(
        "order_id string, customer_id string, order_date string, amount long, status string"
    ).csv("/workspace/data/beginner/orders.csv")
    result = orders.agg(F.count("*").alias("rows"), F.sum("amount").alias("total"))
    row = result.first()
    assert row.rows == 8 and row.total == 1400000
    result.write.mode("overwrite").parquet("/work-output/summary")
    print("Master:", spark.sparkContext.master, "Kết quả:", row)
finally:
    spark.stop()
