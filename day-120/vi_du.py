"""Ngày 120: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 120 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(120, exercise=False)
    paths = {"pipeline": ROOT / "services/pipeline.py", "api": ROOT / "services/churn_api.py", "dag": ROOT / "services/airflow/dags/churn_pipeline.py", "tests": ROOT / "tests/test_course_contracts.py"}
    print({name: str(path) for name, path in paths.items()})
    print("Checklist:", ROOT / "projects/03-mlops-serving/README.md")
    print("Điền bằng chứng thật; file tồn tại không có nghĩa đã nghiệm thu.")


if __name__ == "__main__":
    main()
