"""Ngày 126: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 126 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(126, exercise=False)
    from rag_support import load_corpus
    corpus = load_corpus()
    print([(doc["doc_id"], doc["access"], doc["version"]) for doc in corpus])
    assert len(corpus) == 8
    print("Ingest: parse→chunk→embed→index; online: quyền→retrieve→generate→validate.")


if __name__ == "__main__":
    main()
