"""Ngày 85: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 85 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(85, exercise=False)
    import subprocess
    result = subprocess.run([sys.executable, str(ROOT / "services/pipeline.py"), "--step", "train", "--version", "../bad"], capture_output=True, text=True)
    print({"exit_code": result.returncode, "rejected": result.returncode != 0})
    assert result.returncode != 0


if __name__ == "__main__":
    main()
