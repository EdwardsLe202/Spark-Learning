# Ngày 115 — Embedding attention và Transformer

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Embedding attention và Transformer”. Kết quả cần đạt: Shape đúng, attention weights tổng 1; không gọi vector ngẫu nhiên là embedding ngữ nghĩa đã học.

## Từ mới gắn với bài này

- **Embedding (biểu diễn token bằng vector)**.
- **Attention (kết hợp thông tin theo mức liên quan)**.
- **Transformer (kiến trúc mạng dùng attention)**.

## Tình huống và cách hiểu

**Embedding (biểu diễn token bằng vector)** ánh xạ mã token vào vector số. **Attention (kết hợp thông tin theo mức liên quan)** tính trọng số từ query/key rồi kết hợp value. **Transformer (kiến trúc mạng dùng attention)** xây các lớp có attention cùng các thành phần khác.

Mẫu chỉ là phép attention nhỏ với trọng số ngẫu nhiên để hiểu shape. Nó không được huấn luyện ngôn ngữ và không dùng làm model sinh câu trả lời. Sum trọng số trên các key bằng 1 sau softmax.

Để dùng pretrained model, phải giữ tokenizer, special token, revision và context limit tương thích. Fine-tuning hoặc huấn luyện từ đầu cần dữ liệu/tài nguyên khác, không bắt đầu bằng việc train LLM lớn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-115/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import torch
import math
torch.manual_seed(42)
q, k, v = [torch.randn(1, 2, 4) for _ in range(3)]
weights = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(4), dim=-1)
output_tensor = weights @ v
print("Weights:", weights.shape, "Output:", output_tensor.shape)
assert torch.allclose(weights.sum(dim=-1), torch.ones(1, 2))
```

## Đọc từng phần của ví dụ

Hai token, mỗi vector bốn chiều. Ma trận trọng số [1,2,2] kết hợp value thành [1,2,4].

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Shape đúng, attention weights tổng 1; không gọi vector ngẫu nhiên là embedding ngữ nghĩa đã học.

## Ba câu kiểm tra hiểu bài

1. Embedding có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: biểu diễn token bằng vector.
- Luồng chính: Hai token, mỗi vector bốn chiều. Ma trận trọng số [1,2,2] kết hợp value thành [1,2,4].
- Đối chiếu tiêu chí: Shape đúng, attention weights tổng 1; không gọi vector ngẫu nhiên là embedding ngữ nghĩa đã học. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 22 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
