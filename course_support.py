"""Đầu vào và tiện ích cho ngày 31–150. Mỗi hàm được liên kết từ bài học.

Không huấn luyện hoặc tải model lúc import. Ví dụ và bài làm dùng đích riêng.
"""
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
import csv
import hashlib
import json
import os
import sys

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FULL = ROOT / "artifacts" / "full"
FEATURES = ["events_30d", "spend_30d", "recency_days", "region", "plan"]


def output(day, exercise=False):
    path = FULL / f"day-{int(day):03d}" / ("exercise" if exercise else "example")
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def data_hash():
    content = (DATA / "raw/events.csv").read_bytes() + b"\n" + (DATA / "raw/customers.csv").read_bytes()
    return hashlib.sha256(content).hexdigest()


@contextmanager
def spark_session(name, delta=False):
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    from pyspark.sql import SparkSession
    builder = (SparkSession.builder.master("local[2]").appName(name)
               .config("spark.sql.session.timeZone", "UTC")
               .config("spark.sql.shuffle.partitions", "4")
               .config("spark.sql.ansi.enabled", "false"))
    if delta:
        from delta import configure_spark_with_delta_pip
        builder = configure_spark_with_delta_pip(builder
            .config("spark.jars.ivy", str(FULL / "ivy-cache"))
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog"))
    spark = builder.getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    try:
        yield spark
    finally:
        spark.stop()


def orders_df(spark):
    return spark.read.option("header", True).schema(
        "order_id string, customer_id string, order_date string, amount long, status string"
    ).csv(str(DATA / "beginner/orders.csv"))


def events_df(spark, filename="events.csv"):
    from pyspark.sql import functions as F
    schema = "event_id string, customer_id string, event_time string, ingested_at string, amount string, event_type string"
    return (spark.read.option("header", True).schema(schema).csv(str(DATA / "raw" / filename))
            .withColumn("event_ts", F.to_timestamp("event_time"))
            .withColumn("available_ts", F.to_timestamp("ingested_at"))
            .withColumn("amount_num", F.col("amount").cast("double")))


def snapshot_pd(cutoff="2025-02-01", include_labels=True):
    """Tham chiếu tính snapshot bằng Python; ngày 56–60 tự viết lại bằng Spark.

    Giữ người không có sự kiện. Feature cần cả event_time và ingested_at < cutoff.
    """
    import pandas as pd
    c = datetime.fromisoformat(cutoff).replace(tzinfo=timezone.utc)
    observed = datetime(2025, 8, 1, tzinfo=timezone.utc)
    if c > observed:
        raise ValueError("Nguồn chưa quan sát đầy đủ tới cutoff để tạo feature")
    if include_labels and c + timedelta(days=30) > observed:
        raise ValueError("Nguồn chưa quan sát đủ 30 ngày tương lai để gán nhãn")
    if c < datetime(2025, 1, 31, tzinfo=timezone.utc):
        raise ValueError("Nguồn chưa có đủ lịch sử 30 ngày cho cutoff này")
    parse = lambda value: datetime.fromisoformat(value.replace("Z", "+00:00"))
    with (DATA / "raw/events.csv").open(encoding="utf-8", newline="") as f:
        events = list(csv.DictReader(f))
    with (DATA / "raw/customers.csv").open(encoding="utf-8", newline="") as f:
        customers = list(csv.DictReader(f))
    histories = {}
    future = set()
    for event in events:
        t, available = parse(event["event_time"]), parse(event["ingested_at"])
        cid = event["customer_id"]
        if c - timedelta(days=30) <= t < c and available < c:
            histories.setdefault(cid, []).append((t, float(event["amount"])))
        if c <= t < c + timedelta(days=30):
            future.add(cid)
    rows = []
    for customer in customers:
        cid = customer["customer_id"]
        history = histories.get(cid, [])
        row = {"customer_id": cid, "snapshot_date": cutoff,
               "events_30d": float(len(history)), "spend_30d": sum(v for _, v in history),
               "recency_days": float((c.date() - max(t.date() for t, _ in history)).days) if history else None,
               "region": customer["region"], "plan": customer["plan"]}
        if include_labels:
            row["label"] = float(cid not in future)
        rows.append(row)
    return pd.DataFrame(rows)


def spark_snapshot(spark, cutoff="2025-02-01"):
    """Chuyển fixture tham chiếu sang Spark để bài ML không cần artifact của người học."""
    frame = snapshot_pd(cutoff)
    records = []
    import math
    for row in frame.to_dict("records"):
        if row["recency_days"] is not None and math.isnan(row["recency_days"]):
            row["recency_days"] = None
        records.append(row)
    return spark.createDataFrame(records, "customer_id string, snapshot_date string, events_30d double, spend_30d double, recency_days double, region string, plan string, label double")


def build_features_spark(spark, cutoff, events=None, include_labels=True):
    """Lời giải tham chiếu dự án 1; các ngày 56–60 giải thích từng bước."""
    from pyspark.sql import functions as F
    from pyspark.sql import Window
    c = datetime.fromisoformat(cutoff).replace(tzinfo=timezone.utc)
    observed = datetime(2025, 8, 1, tzinfo=timezone.utc)
    if c > observed:
        raise ValueError("Nguồn chưa quan sát đầy đủ tới cutoff để tạo feature")
    if c < datetime(2025, 1, 31, tzinfo=timezone.utc):
        raise ValueError("Thiếu cửa sổ lịch sử 30 ngày")
    if include_labels and c + timedelta(days=30) > observed:
        raise ValueError("Chưa đủ cửa sổ nhãn")
    events = events if events is not None else events_df(spark)
    point = F.to_timestamp(F.lit(cutoff + "T00:00:00Z"))
    latest = Window.partitionBy("event_id").orderBy(F.col("available_ts").desc(), F.col("event_ts").desc())
    known = (events.filter(F.col("available_ts") < point)
             .withColumn("rn", F.row_number().over(latest)).filter("rn = 1"))
    history = known.filter((F.col("event_ts") >= point - F.expr("INTERVAL 30 DAYS")) & (F.col("event_ts") < point))
    agg = history.groupBy("customer_id").agg(F.count("*").cast("double").alias("events_30d"),
            F.sum("amount_num").alias("spend_30d"), F.max("event_ts").alias("last_event"))
    customers = spark.read.option("header", True).schema(
        "customer_id string, region string, plan string, signup_date date"
    ).csv(str(DATA / "raw/customers.csv"))
    result = (customers.filter(F.col("signup_date") < F.lit(cutoff).cast("date"))
              .join(agg, "customer_id", "left").fillna({"events_30d": 0.0, "spend_30d": 0.0})
              .withColumn("recency_days", F.datediff(F.to_date(point), F.to_date("last_event")).cast("double"))
              .withColumn("snapshot_date", F.lit(cutoff)))
    if include_labels:
        future = (events.filter((F.col("event_ts") >= point) & (F.col("event_ts") < point + F.expr("INTERVAL 30 DAYS")))
                  .select("customer_id").distinct().withColumn("has_future", F.lit(1)))
        result = result.join(future, "customer_id", "left").withColumn("label", F.when(F.col("has_future").isNull(), 1.0).otherwise(0.0)).drop("has_future")
    return result.drop("last_event", "signup_date")


def stream_workspace(out):
    """Mỗi lần thí nghiệm có checkpoint mới; restart bên trong dùng lại nó."""
    import uuid
    path = Path(out) / ("run-" + uuid.uuid4().hex[:10])
    (path / "input").mkdir(parents=True)
    write_json(Path(out) / "last_run.json", {"path": str(path)})
    return path


def write_stream_file(path, name, rows):
    target = Path(path) / "input" / name
    if target.exists():
        raise FileExistsError("File source của stream phải bất biến; chọn tên mới")
    target.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")


def file_stream(spark, path):
    return (spark.readStream.schema("event_id string, event_time string, value long")
            .option("maxFilesPerTrigger", 1).json(str(Path(path) / "input")))


def run_file_stream(spark, path):
    query = (file_stream(spark, path).writeStream.format("parquet").outputMode("append")
             .option("checkpointLocation", str(Path(path) / "checkpoint"))
             .option("path", str(Path(path) / "output")).trigger(availableNow=True).start())
    query.awaitTermination()
    return query.lastProgress


def sklearn_pipeline(C=1.0):
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    numeric = Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    preprocess = ColumnTransformer([
        ("numeric", numeric, FEATURES[:3]),
        ("category", OneHotEncoder(handle_unknown="ignore"), FEATURES[3:])])
    return Pipeline([("preprocess", preprocess), ("classifier", LogisticRegression(C=C, max_iter=300, random_state=42))])


def fit_sklearn(C=1.0):
    train, validation = snapshot_pd(), snapshot_pd("2025-04-01")
    model = sklearn_pipeline(C).fit(train[FEATURES], train["label"])
    return model, train, validation


def spark_ml_pipeline(reg_param=0.1):
    """Pipeline tham chiếu; ngày 67–72 tự lắp từng stage trước khi dùng lại."""
    from pyspark.ml import Pipeline
    from pyspark.ml.feature import Imputer, StringIndexer, OneHotEncoder, VectorAssembler
    from pyspark.ml.classification import LogisticRegression
    numbers = FEATURES[:3]
    imputed = [name + "_filled" for name in numbers]
    stages = [Imputer(inputCols=numbers, outputCols=imputed)]
    stages += [StringIndexer(inputCol=name, outputCol=name + "_idx", handleInvalid="keep") for name in FEATURES[3:]]
    stages += [OneHotEncoder(inputCols=["region_idx", "plan_idx"], outputCols=["region_vec", "plan_vec"]),
               VectorAssembler(inputCols=imputed + ["region_vec", "plan_vec"], outputCol="features"),
               LogisticRegression(regParam=reg_param, maxIter=20)]
    return Pipeline(stages=stages)


def ensure_demo_model():
    """Tạo artifact mẫu riêng cho bài serving; API không gọi hàm này khi nhận request."""
    import joblib
    path = FULL / "models/churn.joblib"
    path.parent.mkdir(parents=True, exist_ok=True)
    model, _, _ = fit_sklearn()
    joblib.dump(model, path)
    write_json(path.with_suffix(".json"), {"model_version": "demo-v1", "threshold": 0.5,
               "data_hash": data_hash(), "features": FEATURES, "training_snapshot": "2025-02-01"})
    return path


def setup_tracking():
    import mlflow
    FULL.mkdir(parents=True, exist_ok=True)
    mlflow.set_tracking_uri("sqlite:///" + str(FULL / "mlflow.db"))
    name = "spark-course-150"
    if mlflow.get_experiment_by_name(name) is None:
        mlflow.create_experiment(name, artifact_location=(FULL / "mlflow-artifacts").as_uri())
    mlflow.set_experiment(name)
    return mlflow


def metric_counts(y_true, scores, threshold=0.5):
    pairs = [(int(y), float(score) >= threshold) for y, score in zip(y_true, scores)]
    tp = sum(y == 1 and p for y, p in pairs)
    fp = sum(y == 0 and p for y, p in pairs)
    fn = sum(y == 1 and not p for y, p in pairs)
    tn = sum(y == 0 and not p for y, p in pairs)
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn,
            "precision": tp / (tp + fp) if tp + fp else 0.0,
            "recall": tp / (tp + fn) if tp + fn else 0.0}
