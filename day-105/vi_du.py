"""Ngày 105: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 105 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(105, exercise=False)
    policy = {"trigger": ["quality_checked", "labels_complete", "reviewed_performance_drop"], "gates": ["same_validation_protocol", "schema_compatible", "minimum_metric", "no_slice_regression_unexplained"], "on_reject": "keep_previous", "after_promote": ["readiness", "monitor", "rollback_if_needed"]}
    write_json(out / "retrain_policy.json", policy)
    print(policy)


if __name__ == "__main__":
    main()
