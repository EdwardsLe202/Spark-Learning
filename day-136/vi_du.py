"""Ngày 136: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 136 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(136, exercise=False)
    from rag_support import retrieval_metrics, eval_queries, chunk_documents, load_corpus, sparse_search, doc_ids
    print(retrieval_metrics(["wrong", "right"], ["right"], k=2))
    chunks = chunk_documents(load_corpus())
    rows = []
    for case in eval_queries("dev"):
        if case["relevant_doc_ids"]:
            ranked = sparse_search(case["query"], chunks, role=case["user_role"], k=10)
            rows.append({"query_id": case["query_id"], **retrieval_metrics(doc_ids(ranked), case["relevant_doc_ids"], k=3)})
    write_json(out / "sparse_dev_metrics.json", rows)
    print("Số câu có relevant được chấm:", len(rows))


if __name__ == "__main__":
    main()
