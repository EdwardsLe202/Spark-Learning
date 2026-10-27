# Ngày 22 — Lý thuyết: PyTorch và nền tảng Transformer

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Train mô hình tensor nhỏ trên CPU, lưu trọng số và chạy inference sau load.

## 1. Tensor và luồng dữ liệu
**Tensor (mảng số nhiều chiều)** có **shape (kích thước từng chiều)**, **dtype (kiểu phần tử)** và **device (thiết bị chứa dữ liệu và thực hiện phép tính)**. Batch 16 mẫu, mỗi mẫu 3 feature, có shape [16,3]. Lớp Linear(3,1) tạo [16,1]; nhãn phải có shape tương thích để tránh broadcasting ngoài ý muốn.

**Dataset (đối tượng cung cấp mẫu dữ liệu)** và **DataLoader (bộ đọc dữ liệu theo lô)** tách cách đọc với model. **Forward pass (lượt tính đầu ra)** tạo prediction; **loss function (hàm đo sai lệch)** so prediction với nhãn; **backward pass (lượt tính gradient)** dùng autograd; **optimizer (thuật toán cập nhật trọng số)** thực hiện bước học. Cần zero_grad trước lần backward mới để không cộng dồn ngoài ý muốn.

## 2. Train và inference
`model.train()` bật hành vi huấn luyện cho lớp như dropout; `model.eval()` chuyển hành vi đánh giá. `torch.no_grad()` hoặc inference_mode tắt việc theo dõi gradient. Eval không tự tắt gradient. **Checkpoint (bản lưu trạng thái)** có thể chứa trọng số, optimizer và epoch để tiếp tục học; lưu state_dict trọng số đủ cho inference nếu giữ định nghĩa kiến trúc.

**Overfitting (học quá sát tập train)** xảy ra khi train tốt nhưng dữ liệu mới kém. Giữ split, theo dõi loss validation và seed. Với Mac, CPU luôn là đường bắt đầu nhẹ; **MPS — Metal Performance Shaders (backend tăng tốc trên thiết bị Apple được hỗ trợ)** tùy phép toán và phiên bản. Mac không mặc định có CUDA.

## 3. Từ vector tới Transformer
**Embedding (biểu diễn đầu vào bằng vector)** biến token thành vector. **Attention (cơ chế tính mức liên quan giữa các vị trí)** giúp một token kết hợp thông tin từ token khác. **Transformer (kiến trúc mạng dựa trên attention)** là nền của nhiều pretrained model. **Pretrained model (mô hình đã được huấn luyện trước)** giúp không phải học ngôn ngữ từ đầu; bài này chỉ cần hiểu luồng và tài nguyên, không train một LLM lớn.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
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
```

## Năm ý đối chiếu với lộ trình gốc

- 22.1 — Tensor, shape, dtype, device và thao tác cơ bản.
- 22.2 — Dataset, DataLoader, batch, forward, loss, backward và optimizer.
- 22.3 — Train, eval, no grad, overfitting, checkpoint và lưu load trọng số.
- 22.4 — Embedding, attention, Transformer và pretrained model ở mức ứng dụng.
- 22.5 — CPU, GPU, Apple MPS khi được hỗ trợ; bộ nhớ, batch size và giới hạn phần cứng.

Các ý trên giữ phạm vi phần 22 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Eval khác no_grad thế nào?
2. Batch size ảnh hưởng số bước cập nhật ra sao?
3. Vì sao inference vẫn có thể hết RAM?

## Đọc thêm từ nguồn chính thức

- [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
