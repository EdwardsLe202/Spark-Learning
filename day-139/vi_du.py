"""Ngày 139: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 139 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(139, exercise=False)
    from rag_support import load_corpus, chunk_documents, keyword_search
    import uuid,time
    start = time.perf_counter()
    ranked = keyword_search("Spark là gì?", chunk_documents(load_corpus()), role="public")
    trace = {"request_id": uuid.uuid4().hex, "strategy": "keyword", "generation_model": None, "retrieved_ids": [c["chunk_id"] for c in ranked], "duration_seconds": time.perf_counter() - start, "status": "retrieval_only"}
    write_json(out / "trace.json", trace)
    print(trace)


if __name__ == "__main__":
    main()
