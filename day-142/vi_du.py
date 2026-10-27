"""Ngày 142: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 142 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(142, exercise=False)
    from pydantic import BaseModel, ConfigDict, Field
    from rag_support import get_job_status
    class StatusArgs(BaseModel):
        model_config = ConfigDict(extra="forbid", strict=True)
        job_id: str = Field(pattern=r"^job-[0-9]{3}$")
    print(StatusArgs.model_json_schema())
    args = StatusArgs.model_validate({"job_id": "job-001"})
    print(get_job_status(args.job_id))


if __name__ == "__main__":
    main()
