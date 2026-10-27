"""Ngày 130: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 130 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(130, exercise=False)
    from qdrant_client import QdrantClient, models
    client = QdrantClient(":memory:")
    client.create_collection("docs", vectors_config=models.VectorParams(size=2, distance=models.Distance.COSINE))
    point = models.PointStruct(id=1, vector=[1.0, 0.0], payload={"doc_id": "doc-spark", "access": "public"})
    client.upsert("docs", points=[point])
    client.upsert("docs", points=[point])
    print("Số point:", client.count("docs").count)
    print(client.query_points("docs", query=[1.0, 0.0], query_filter=models.Filter(must=[models.FieldCondition(key="access", match=models.MatchValue(value="public"))]), limit=3).points)
    client.delete("docs", points_selector=models.PointIdsList(points=[1]))
    assert client.count("docs").count == 0
    client.close()


if __name__ == "__main__":
    main()
