"""Ngày 22: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 22
"""
from spark_lab import ROOT, DATA, output_dir

import torch
from torch import nn
torch.manual_seed(42)
x = torch.tensor([[0.0], [1.0], [2.0], [3.0]])
y = 2 * x + 1
model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)
for epoch in range(100):
    optimizer.zero_grad()
    loss = nn.functional.mse_loss(model(x), y)
    loss.backward()
    optimizer.step()
model.eval()
with torch.no_grad():
    print("shape:", model(x).shape, "loss:", loss.item())
# TODO: lưu state_dict; load vào Linear(1,1) ở tiến trình mới và so kết quả.

# Bài tự làm hôm nay:
# TODO Cài torch theo requirements-ai.txt hoặc cài riêng torch==2.6.0 nếu chỉ học ngày này; chạy ví dụ CPU.
# TODO Ghi shape, dtype và device của x, y, prediction. In loss ở epoch 0 và cuối để kiểm tra xu hướng giảm.
# TODO Chuyển dữ liệu sang TensorDataset/DataLoader, thử batch_size 1 và 4; ghi khác nhau về số bước cập nhật.
# TODO Lưu state_dict, tạo model mới, load bằng map_location="cpu", eval và no_grad. So dự đoán trên fixture bằng torch.allclose.
# TODO Viết 5–8 câu giải thích embedding → attention → Transformer; phân biệt điều đã chạy (Linear) với kiến trúc mới học lý thuyết.
