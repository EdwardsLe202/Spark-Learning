"""Ngày 112: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 112 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(112, exercise=False)
    import torch
    from torch import nn
    torch.manual_seed(42)
    x = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
    model = nn.Linear(3, 1)
    y = model(x)
    print({"input_shape": list(x.shape), "output_shape": list(y.shape), "dtype": str(x.dtype), "device": str(x.device)})
    assert list(y.shape) == [2, 1]


if __name__ == "__main__":
    main()
