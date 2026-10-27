"""Ngày 137: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 137 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(137, exercise=False)
    from rag_support import rag_answer
    result = rag_answer("local[2] là hai máy hay hai luồng?", role="public", k=3)
    write_json(out / "answer.json", result)
    print(result)


if __name__ == "__main__":
    main()
