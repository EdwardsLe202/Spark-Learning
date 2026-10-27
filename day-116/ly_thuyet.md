# Ngày 116 — Pretrained tokenizer và CPU MPS

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Pretrained tokenizer và CPU MPS”. Kết quả cần đạt: Có tokenizer/model pretrained thật và báo cáo máy; ví dụ kiểm tra thiết bị chưa thay lab inference.

## Từ mới gắn với bài này

- **Pretrained model (model đã học trước)**.
- **Tokenizer (bộ chia mã hóa token)**.
- **MPS (backend tính toán cho thiết bị Apple)**.

## Tình huống và cách hiểu

**Pretrained model (model đã học trước)** đi cùng **tokenizer (bộ chia mã hóa token)** và revision. Tải model từ nguồn có model card/license, lưu commit thực để tái lập. Cùng tên model nhưng main đổi theo thời gian có thể thay kết quả.

**MPS (backend tính toán cho thiết bị Apple)** có thể được hỗ trợ trên Mac; CPU luôn là điểm bắt đầu của lab nhỏ. Cài model inference không đồng nghĩa có đủ RAM cho training. Giới hạn input/output token và batch trước khi thử.

Ví dụ chỉ kiểm tra thiết bị, không tự tải hàng GB. Lab dùng script download riêng và local model ở bước này; ghi dung lượng, revision, latency và giới hạn chất lượng, đặc biệt khi phục vụ tiếng Việt.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-116/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import torch
print({"cpu": True, "mps_available": torch.backends.mps.is_available(), "cuda_available": torch.cuda.is_available()})
print("Tải model chủ động: python scripts/download_course_models.py generator")
print("Sau tải: mở tokenizer và so token count trên hai câu tiếng Việt theo hướng dẫn.")
```

## Đọc từng phần của ví dụ

Không tự chọn CUDA chỉ vì tutorial dùng GPU. Download là bước riêng có tên/revision/cache rõ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có tokenizer/model pretrained thật và báo cáo máy; ví dụ kiểm tra thiết bị chưa thay lab inference.

## Ba câu kiểm tra hiểu bài

1. Pretrained model có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: model đã học trước.
- Luồng chính: Không tự chọn CUDA chỉ vì tutorial dùng GPU. Download là bước riêng có tên/revision/cache rõ.
- Đối chiếu tiêu chí: Có tokenizer/model pretrained thật và báo cáo máy; ví dụ kiểm tra thiết bị chưa thay lab inference. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 22 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
