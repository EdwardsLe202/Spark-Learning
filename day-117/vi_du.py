"""Ngày 117: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 117 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(117, exercise=False)
    import numpy as np
    sample_ms = [10, 12, 11, 14, 13, 30, 15, 12, 11, 16]
    print({"p50": float(np.percentile(sample_ms, 50)), "p95": float(np.percentile(sample_ms, 95)), "n": len(sample_ms), "source": "illustrative_numbers"})


if __name__ == "__main__":
    main()
