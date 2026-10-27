"""Ngày 95: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 95 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(95, exercise=False)
    import platform, shutil, subprocess
    print("Kiến trúc Python:", platform.machine())
    if shutil.which("docker"):
        result = subprocess.run(["docker", "version"], capture_output=True, text=True)
        print("Docker daemon khả dụng:", result.returncode == 0)
    else:
        print("Chưa có Docker CLI; làm cài đặt runtime trước lab.")


if __name__ == "__main__":
    main()
