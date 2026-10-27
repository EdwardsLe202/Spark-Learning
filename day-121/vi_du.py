"""Ngày 121: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 121 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(121, exercise=False)
    budget = {"limit": 2048, "instruction_tokens": 150, "question_tokens": 80, "context_tokens": 1200, "max_output_tokens": 256}
    print("Tổng dự kiến:", sum(v for k, v in budget.items() if k != "limit"))
    assert sum(v for k, v in budget.items() if k != "limit") <= budget["limit"]
    print("Các số là ví dụ budget; đo token thật bằng tokenizer trong lab.")


if __name__ == "__main__":
    main()
