# Ngày 112 — Tensor shape dtype và device

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Tensor shape dtype và device”. Kết quả cần đạt: Ví dụ output [2,1]; biến thể [4,1], biết sửa lỗi dimension.

## Từ mới gắn với bài này

- **Tensor (mảng số nhiều chiều)**.
- **Shape (kích thước các chiều)**.
- **Device (thiết bị chứa và tính dữ liệu)**.

## Tình huống và cách hiểu

**Tensor (mảng số nhiều chiều)** có **shape (kích thước các chiều)**, dtype và **device (thiết bị chứa và tính dữ liệu)**. Batch 4 mẫu × 3 feature có shape [4,3]. Model phải nhận đúng chiều và dữ liệu trên thiết bị phù hợp.

Mac không mặc định có CUDA. CPU là lựa chọn bắt đầu; MPS tùy máy và phép toán. Không chuyển device chỉ vì thấy nhãn GPU ở tutorial viết cho môi trường khác.

Mẫu Linear(3,1) đổi mỗi vector ba số thành một đầu ra. Đây là mô hình tensor nhỏ để hiểu luồng, chưa là Transformer hay một LLM đã học ngôn ngữ.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-112/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import torch
from torch import nn
torch.manual_seed(42)
x = torch.tensor([[1., 2., 3.], [4., 5., 6.]])
model = nn.Linear(3, 1)
y = model(x)
print({"input_shape": list(x.shape), "output_shape": list(y.shape), "dtype": str(x.dtype), "device": str(x.device)})
assert list(y.shape) == [2, 1]
```

## Đọc từng phần của ví dụ

Linear dùng chiều cuối 3 làm số feature. Batch hai mẫu nên output hai dòng, mỗi dòng một số.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ví dụ output [2,1]; biến thể [4,1], biết sửa lỗi dimension.

## Ba câu kiểm tra hiểu bài

1. Tensor có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mảng số nhiều chiều.
- Luồng chính: Linear dùng chiều cuối 3 làm số feature. Batch hai mẫu nên output hai dòng, mỗi dòng một số.
- Đối chiếu tiêu chí: Ví dụ output [2,1]; biến thể [4,1], biết sửa lỗi dimension. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 22 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
