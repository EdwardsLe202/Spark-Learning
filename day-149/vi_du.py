"""Ngày 149: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 149 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(149, exercise=False)
    files = ["course_support.py", "services/pipeline.py", "services/churn_api.py", "rag_support.py"]
    manifest = {name: __import__("hashlib").sha256((ROOT / name).read_bytes()).hexdigest() for name in files}
    write_json(out / "code_manifest.json", manifest)
    print(manifest)
    print("Bổ sung model/prompt/index/data/dependency version thật của dự án bạn.")


if __name__ == "__main__":
    main()
