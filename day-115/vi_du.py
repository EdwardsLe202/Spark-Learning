"""Ngày 115: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 115 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(115, exercise=False)
    import torch
    import math
    torch.manual_seed(42)
    q, k, v = [torch.randn(1, 2, 4) for _ in range(3)]
    weights = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(4), dim=-1)
    output_tensor = weights @ v
    print("Weights:", weights.shape, "Output:", output_tensor.shape)
    assert torch.allclose(weights.sum(dim=-1), torch.ones(1, 2))


if __name__ == "__main__":
    main()
