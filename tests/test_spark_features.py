"""So phép tính Spark với mốc tính tay và tham chiếu Python độc lập."""
import math
import os
import pytest

from course_support import (FEATURES, build_features_spark, events_df,
                            snapshot_pd, spark_session)


@pytest.fixture(scope="module")
def spark():
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")
    with spark_session("test-feature-contract") as session:
        yield session


@pytest.mark.parametrize("cutoff", ["2025-02-01", "2025-04-01", "2025-06-01"])
def test_spark_matches_independent_python_snapshot(spark, cutoff):
    actual = {row.customer_id: row.asDict() for row in build_features_spark(spark, cutoff).collect()}
    expected = snapshot_pd(cutoff)
    assert len(actual) == len(expected) == 120
    for row in expected.to_dict("records"):
        found = actual[row["customer_id"]]
        for col in FEATURES + ["label", "snapshot_date"]:
            value = row[col]
            if isinstance(value, float) and math.isnan(value):
                assert found[col] is None
            elif isinstance(value, (int, float)):
                assert found[col] == pytest.approx(value, abs=1e-8)
            else:
                assert found[col] == value


def test_tiny_features_have_hand_calculated_values(spark):
    events = events_df(spark, "events_tiny.csv")
    rows = {r.customer_id: r for r in build_features_spark(spark, "2025-02-01", events).collect()}
    assert (rows["C001"].events_30d, rows["C001"].spend_30d, rows["C001"].recency_days, rows["C001"].label) == (2, 300000, 12, 0)
    assert (rows["C002"].events_30d, rows["C002"].spend_30d, rows["C002"].recency_days, rows["C002"].label) == (1, 50000, 17, 1)
    assert (rows["C003"].events_30d, rows["C003"].spend_30d, rows["C003"].recency_days, rows["C003"].label) == (0, 0, None, 1)


def test_future_and_late_ingestion_do_not_change_historical_features(spark):
    from pyspark.sql import functions as F
    events = events_df(spark, "events_tiny.csv")
    extra = spark.createDataFrame([
        ("future", "C001", "2025-02-08T10:00:00Z", "2025-02-08T11:00:00Z", "999999999", "purchase"),
        ("late", "C001", "2025-01-25T10:00:00Z", "2025-02-02T11:00:00Z", "999999999", "purchase")
    ], "event_id string, customer_id string, event_time string, ingested_at string, amount string, event_type string")
    extra = (extra.withColumn("event_ts", F.to_timestamp("event_time"))
             .withColumn("available_ts", F.to_timestamp("ingested_at"))
             .withColumn("amount_num", F.col("amount").cast("double")))
    cols = ["customer_id"] + FEATURES
    before = build_features_spark(spark, "2025-02-01", events).select(cols).orderBy("customer_id").collect()
    after = build_features_spark(spark, "2025-02-01", events.unionByName(extra)).select(cols).orderBy("customer_id").collect()
    assert before == after


def test_spark_refuses_snapshot_after_source_coverage(spark):
    with pytest.raises(ValueError, match="tới cutoff"):
        build_features_spark(spark, "2025-08-02", include_labels=False)
