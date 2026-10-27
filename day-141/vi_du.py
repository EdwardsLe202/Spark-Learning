"""Ngày 141: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 141 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(141, exercise=False)
    from rag_support import dispatch_tool, allowed_chunks, chunk_documents, load_corpus
    try:
        dispatch_tool("delete_file", {"path": "any"}, role="public")
    except PermissionError:
        print("Chặn công cụ ngoài allowlist.")
    try:
        allowed_chunks(chunk_documents(load_corpus()), "self-claimed-admin")
    except PermissionError:
        print("Chặn role không tin cậy.")


if __name__ == "__main__":
    main()
