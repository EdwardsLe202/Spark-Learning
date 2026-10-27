"""Ngày 113: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 113 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(113, exercise=False)
    import torch
    from torch import nn
    from torch.utils.data import TensorDataset, DataLoader
    torch.manual_seed(42)
    x = torch.arange(4, dtype=torch.float32).reshape(-1, 1)
    y = 2 * x + 1
    loader = DataLoader(TensorDataset(x, y), batch_size=4, shuffle=False)
    model = nn.Linear(1, 1)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.05)
    losses = []
    for epoch in range(100):
        for xb, yb in loader:
            optimizer.zero_grad()
            loss = nn.functional.mse_loss(model(xb), yb)
            loss.backward()
            optimizer.step()
        losses.append(float(loss.detach()))
    print(losses[0], losses[-1])
    assert losses[-1] < losses[0]


if __name__ == "__main__":
    main()
