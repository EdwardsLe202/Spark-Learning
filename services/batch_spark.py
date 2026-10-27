"""Batch scoring Spark model đã lưu; chạy bằng spark-submit hoặc Python đúng môi trường."""
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import spark_session


def main():
    from pyspark.ml import PipelineModel
    from pyspark.ml.functions import vector_to_array
    from pyspark.sql import functions as F
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--features", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    destination = Path(args.output).resolve()
    if destination == Path(args.features).resolve() or destination == ROOT:
        raise ValueError("Đích không được trùng nguồn hay thư mục gốc")
    with spark_session("batch-churn") as spark:
        model = PipelineModel.load(args.model)
        frame = spark.read.parquet(args.features)
        result = (model.transform(frame).withColumn("score", vector_to_array("probability")[1])
                  .withColumn("model_version", F.lit(args.version))
                  .select("customer_id", "snapshot_date", "score", "prediction", "model_version"))
        if result.groupBy("customer_id", "snapshot_date", "model_version").count().filter("count > 1").count():
            raise ValueError("Prediction trùng khóa")
        result.write.mode("overwrite").parquet(str(destination))
        print("Đã score:", result.count())


if __name__ == "__main__":
    main()
