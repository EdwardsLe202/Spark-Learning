# Ngày 114 — Train eval no_grad và checkpoint

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Train eval no_grad và checkpoint”. Kết quả cần đạt: Output trước/sau load khớp khi eval/no_grad; phân biệt mode với gradient.

## Từ mới gắn với bài này

- **Train / Eval mode (chế độ học / đánh giá)**.
- **Checkpoint (bản lưu trạng thái model)**.
- **Autograd (cơ chế tự tính gradient)**.

## Tình huống và cách hiểu

Model.eval đổi hành vi lớp như dropout/batch normalization; nó không tự tắt **autograd (cơ chế tự tính gradient)**. No_grad/inference_mode ngừng theo dõi gradient trong phạm vi phù hợp. Hai việc có mục đích khác nhau.

**Checkpoint (bản lưu trạng thái model)** có thể chứa weights, optimizer và epoch để tiếp tục train. Inference chỉ cần trọng số cùng định nghĩa kiến trúc và preprocessing đã giữ. Chỉ load artifact tin cậy; dùng map_location cho thiết bị hiện có.

Bài lưu một model nhỏ rồi load vào instance mới. Lab lặp lại từ script mới và kiểm tra kết quả tương đương, không dựa vào biến model vẫn nằm trong notebook.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-114/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
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
```

## Đọc từng phần của ví dụ

Cả hai model cùng kiến trúc và eval để dropout không làm phép so ngẫu nhiên. Weights_only phù hợp state_dict.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Output trước/sau load khớp khi eval/no_grad; phân biệt mode với gradient.

## Ba câu kiểm tra hiểu bài

1. Train / Eval mode có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: chế độ học / đánh giá.
- Luồng chính: Cả hai model cùng kiến trúc và eval để dropout không làm phép so ngẫu nhiên. Weights_only phù hợp state_dict.
- Đối chiếu tiêu chí: Output trước/sau load khớp khi eval/no_grad; phân biệt mode với gradient. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 22 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
