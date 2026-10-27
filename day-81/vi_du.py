"""Ngày 81: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 81 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(81, exercise=False)
    import subprocess
    result = subprocess.run([sys.executable, str(ROOT / "services/pipeline.py"), "--help"], capture_output=True, text=True, check=True)
    print(result.stdout)
    print("SHA code:", __import__("hashlib").sha256((ROOT / "services/pipeline.py").read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
