"""Spark JDBC/PostgreSQL local; lần đầu cần tải JAR PostgreSQL từ Maven."""
import os
from pyspark.sql import SparkSession, functions as F

password = os.environ.get("COURSE_DB_PASSWORD")
if not password:
    raise SystemExit("Đặt COURSE_DB_PASSWORD trong terminal trước khi chạy")
spark = (SparkSession.builder.master("local[2]").appName("course-jdbc")
         .config("spark.jars.packages", "org.postgresql:postgresql:42.7.5").getOrCreate())
try:
    table = spark.read.jdbc("jdbc:postgresql://127.0.0.1:5433/course", "public.orders",
                            properties={"user": "course", "password": password, "driver": "org.postgresql.Driver"})
    result = table.agg(F.count("*").alias("rows"), F.sum("amount").alias("total")).first()
    assert result.rows == 3 and result.total == 350000
    print("JDBC:", result)
finally:
    spark.stop()
