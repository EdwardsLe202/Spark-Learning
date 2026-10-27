"""Ngày 123: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 123 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(123, exercise=False)
    from pydantic import BaseModel, ConfigDict, Field, ValidationError
    class Order(BaseModel):
        model_config = ConfigDict(extra="forbid", strict=True)
        order_id: str | None
        amount_vnd: int | None = Field(ge=0)
    for raw in ['{"order_id":"A01","amount_vnd":120000}', '{"order_id":"A01","amount_vnd":-1}', 'not json']:
        try:
            print(Order.model_validate_json(raw))
        except ValidationError as error:
            print("Parser rejected:", error.error_count())


if __name__ == "__main__":
    main()
