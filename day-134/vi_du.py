"""Ngày 134: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 134 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(134, exercise=False)
    from rag_support import rrf
    first = [{"chunk_id": "a", "score": 0.9}, {"chunk_id": "b", "score": 0.8}]
    second = [{"chunk_id": "b", "score": 20}, {"chunk_id": "c", "score": 15}]
    print(rrf([first, second], k=3))


if __name__ == "__main__":
    main()
