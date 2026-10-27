"""Ngày 116: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 116 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(116, exercise=False)
    import torch
    print({"cpu": True, "mps_available": torch.backends.mps.is_available(), "cuda_available": torch.cuda.is_available()})
    print("Tải model chủ động: python scripts/download_course_models.py generator")
    print("Sau tải: mở tokenizer và so token count trên hai câu tiếng Việt theo hướng dẫn.")


if __name__ == "__main__":
    main()
