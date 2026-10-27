"""Ngày 143: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 143 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(143, exercise=False)
    from rag_support import dispatch_tool
    cases = [("get_job_status", {"job_id": "job-001"}), ("unknown_tool", {}), ("get_job_status", {"job_id": "bad"})]
    for name, args in cases:
        try:
            print({"ok": True, "result": dispatch_tool(name, args, role="public")})
        except (ValueError, PermissionError) as error:
            print({"ok": False, "error": type(error).__name__})


if __name__ == "__main__":
    main()
