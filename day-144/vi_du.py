"""Ngày 144: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 144 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(144, exercise=False)
    from rag_support import dispatch_tool
    proposals = [{"name": "get_job_status", "arguments": {"job_id": "job-001"}}] * 10
    trace = []
    for step, proposal in enumerate(proposals[:3], 1):
        trace.append({"step": step, "result": dispatch_tool(proposal["name"], proposal["arguments"])})
    print({"status": "budget_exhausted", "calls": len(trace), "trace": trace})
    assert len(trace) == 3


if __name__ == "__main__":
    main()
