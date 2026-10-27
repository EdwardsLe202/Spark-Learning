"""Ngày 133: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 133 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(133, exercise=False)
    from rag_support import load_corpus, chunk_documents, sparse_search
    ranked = sparse_search("mã 422 readiness", chunk_documents(load_corpus()), role="public", k=3)
    print([(c["doc_id"], c["score"]) for c in ranked])


if __name__ == "__main__":
    main()
