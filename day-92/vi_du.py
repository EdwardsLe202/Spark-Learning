"""Ngày 92: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 92 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(92, exercise=False)
    import ast
    path = ROOT / "services/airflow/dags/churn_pipeline.py"
    ast.parse(path.read_text())
    print("DAG nguồn:", path)
    print("Chưa chạy Airflow. Thực hiện lab theo docs/CAI_DAT_NANG_CAO.md.")


if __name__ == "__main__":
    main()
