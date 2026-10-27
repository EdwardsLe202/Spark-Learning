"""Ngày 128: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 128 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(128, exercise=False)
    from rag_support import load_corpus, chunk_documents
    corpus = load_corpus()
    a, b = chunk_documents(corpus), chunk_documents(corpus)
    assert [c["chunk_id"] for c in a] == [c["chunk_id"] for c in b]
    kept = chunk_documents([d for d in corpus if d["doc_id"] != "doc-spark"])
    assert not any(c["doc_id"] == "doc-spark" for c in kept)
    write_json(out / "chunks.json", a)
    print(len(a), "chunk ID ổn định; bản thử xóa doc không còn chunk của doc đó.")


if __name__ == "__main__":
    main()
