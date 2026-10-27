# Ngày 113 — DataLoader forward loss backward optimizer

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “DataLoader forward loss backward optimizer”. Kết quả cần đạt: Loss cuối thấp hơn đầu, prediction/target cùng shape; không yêu cầu giá trị chính xác mọi thiết bị.

## Từ mới gắn với bài này

- **DataLoader (bộ đọc theo lô)**.
- **Loss (hàm đo sai lệch)**.
- **Gradient (đạo hàm dùng cập nhật trọng số)**.

## Tình huống và cách hiểu

**DataLoader (bộ đọc theo lô)** cấp batch từ Dataset. Forward tạo dự đoán, **loss (hàm đo sai lệch)** so với target, backward tính **gradient (đạo hàm dùng cập nhật trọng số)** và optimizer.step cập nhật tham số.

Zero_grad trước backward mới để không cộng dồn ngoài ý muốn. Shape prediction và y phải khớp để tránh broadcasting sai. Bài dùng y=2x+1 để tự biết quy luật, không tải bộ dữ liệu ngoài.

Batch size đổi số bước update mỗi epoch. So runtime/loss cần ghi seed và cấu hình, không mặc định hai batch size cho cùng kết quả từng số. Theo dõi validation khi chuyển sang dữ liệu thật để tránh overfit.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-113/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
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
```

## Đọc từng phần của ví dụ

DataLoader giữ batch/target cùng thứ tự. Detach đưa loss về số để lưu, không giữ cả đồ thị gradient.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Loss cuối thấp hơn đầu, prediction/target cùng shape; không yêu cầu giá trị chính xác mọi thiết bị.

## Ba câu kiểm tra hiểu bài

1. DataLoader có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: bộ đọc theo lô.
- Luồng chính: DataLoader giữ batch/target cùng thứ tự. Detach đưa loss về số để lưu, không giữ cả đồ thị gradient.
- Đối chiếu tiêu chí: Loss cuối thấp hơn đầu, prediction/target cùng shape; không yêu cầu giá trị chính xác mọi thiết bị. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 22 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
