"""Ngày 140: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 140 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(140, exercise=False)
    from rag_support import chunk_documents, load_corpus, allowed_chunks
    chunks = chunk_documents(load_corpus())
    public = allowed_chunks(chunks, "public")
    internal = allowed_chunks(chunks, "internal")
    assert all(c["access"] == "public" for c in public)
    assert any(c["doc_id"] == "doc-internal" for c in internal)
    print("Public/internal chunks:", len(public), len(internal))


if __name__ == "__main__":
    main()
