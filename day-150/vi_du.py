"""Ngày 150: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 150 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(150, exercise=False)
    rubric = {"spark_correctness": 20, "execution_performance": 15, "ml_evaluation": 15, "mlops": 20, "api_operations": 10, "rag_workflow": 15, "documentation": 5}
    assert sum(rubric.values()) == 100
    write_json(out / "rubric.json", rubric)
    print(rubric)
    print("Checklist cuối:", ROOT / "projects/NGHIEM_THU_TOAN_LO_TRINH.md")


if __name__ == "__main__":
    main()
