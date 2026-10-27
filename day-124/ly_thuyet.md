# Ngày 124 — Adapter model local và usage budget

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Adapter model local và usage budget”. Kết quả cần đạt: Có output model thật và usage; parser/content được đánh giá riêng, lỗi được báo trung thực.

## Từ mới gắn với bài này

- **Adapter (lớp giao tiếp tách model/provider)**.
- **Usage (lượng token sử dụng)**.
- **Deadline (hạn thời gian toàn yêu cầu)**.

## Tình huống và cách hiểu

**Adapter (lớp giao tiếp tách model/provider)** giúp ứng dụng không phụ thuộc một nhà cung cấp. Repo có generate_text dùng model local đã tải và ghi revision; không cần key API trả phí.

**Usage (lượng token sử dụng)** và latency cần được log theo request. Max_new_tokens giới hạn số token, không tự là **deadline (hạn thời gian toàn yêu cầu)**. Max_time của generate kiểm tra trong bước sinh, không là timeout cứng bao gồm load; deadline cứng cần process/worker có thể hủy.

Bài này chạy model thật. Nếu chưa tải được, chỉ hoàn thành phần thiết kế adapter và ghi generation chưa thực hành, không thay bằng regex rồi báo chất lượng LLM. Model nhỏ có thể sai tiếng Việt; eval sẽ ghi lỗi thật.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-124/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import generate_text
result = generate_text("Trích xuất JSON duy nhất với order_id và amount_vnd; thiếu thì null.", "Đơn A01 có giá 120000 đồng.", max_new_tokens=64)
print(result)
```

## Đọc từng phần của ví dụ

Generate_text chỉ load cache đã có, không tự tải. Response có text, input/output token, thời gian và resolved revision.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có output model thật và usage; parser/content được đánh giá riêng, lỗi được báo trung thực.

## Ba câu kiểm tra hiểu bài

1. Adapter có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: lớp giao tiếp tách model/provider.
- Luồng chính: Generate_text chỉ load cache đã có, không tự tải. Response có text, input/output token, thời gian và resolved revision.
- Đối chiếu tiêu chí: Có output model thật và usage; parser/content được đánh giá riêng, lỗi được báo trung thực. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 24 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
