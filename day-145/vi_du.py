"""Ngày 145: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 145 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(145, exercise=False)
    from rag_support import load_corpus, eval_queries
    print({"documents": len(load_corpus()), "eval_cases": len(eval_queries())})
    print("Nghiệm thu:", ROOT / "projects/04-rag-workflow/README.md")
    print("Cần output/trace/grade thực, không chỉ đếm file.")


if __name__ == "__main__":
    main()
