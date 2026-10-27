"""Ngày 114: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 114 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(114, exercise=False)
    import torch
    from torch import nn
    torch.manual_seed(42)
    model = nn.Sequential(nn.Linear(3, 4), nn.ReLU(), nn.Dropout(0.2), nn.Linear(4, 1))
    x = torch.ones(2, 3)
    model.eval()
    with torch.no_grad():
        before = model(x)
    torch.save(model.state_dict(), out / "weights.pt")
    loaded = nn.Sequential(nn.Linear(3, 4), nn.ReLU(), nn.Dropout(0.2), nn.Linear(4, 1))
    loaded.load_state_dict(torch.load(out / "weights.pt", map_location="cpu", weights_only=True))
    loaded.eval()
    with torch.no_grad():
        assert torch.allclose(before, loaded(x))
    print("Checkpoint load khớp.")


if __name__ == "__main__":
    main()
