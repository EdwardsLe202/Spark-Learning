"""Ngày 138: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 138 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(138, exercise=False)
    from rag_support import eval_queries
    from collections import Counter
    cases = eval_queries()
    print(Counter(c["category"] for c in cases))
    print(Counter(c["split"] for c in cases))
    assert len(cases) == 40
    write_json(out / "grading_rubric.json", {"correctness": "đối chiếu dữ kiện", "groundedness": "mỗi phát biểu có bằng chứng", "citation": "đúng đoạn hỗ trợ", "permission": "không có context sai quyền"})


if __name__ == "__main__":
    main()
