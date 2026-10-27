# Ngày 98 — Compose readiness và dữ liệu bền vững

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Compose readiness và dữ liệu bền vững”. Kết quả cần đạt: Có /ready 200 khi model tồn tại và 503 trong ca thiếu model; log run container thật.

## Từ mới gắn với bài này

- **Compose (cấu hình các dịch vụ container)**.
- **Healthcheck (kiểm tra trạng thái dịch vụ)**.

## Tình huống và cách hiểu

**Compose (cấu hình các dịch vụ container)** mô tả image, port, environment và volume. **Healthcheck (kiểm tra trạng thái dịch vụ)** nên kiểm tra khả năng nhận việc, không chỉ tiến trình còn sống.

API cần model đã load để ready. Nếu file chưa có, /health vẫn có thể sống nhưng /ready trả 503. Volume artifact read-only ở API giảm khả năng ứng dụng làm đổi model trong lúc phục vụ.

Bài Compose chạy API local loopback, yêu cầu khóa từ biến môi trường. Dừng dịch vụ bằng compose down; dữ liệu artifact ở host vẫn còn. Không dùng down -v cho database trừ khi chủ động muốn xóa volume thử nghiệm.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-098/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
print((ROOT / "services/compose.yml").read_text())
print("Chuẩn bị model bằng services/pipeline.py trước khi up.")
print("Lab: docker compose -f services/compose.yml up --build")
```

## Đọc từng phần của ví dụ

File có healthcheck /ready và port host 127.0.0.1. In YAML chưa là bằng chứng dịch vụ đã chạy.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có /ready 200 khi model tồn tại và 503 trong ca thiếu model; log run container thật.

## Ba câu kiểm tra hiểu bài

1. Compose có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: cấu hình các dịch vụ container.
- Luồng chính: File có healthcheck /ready và port host 127.0.0.1. In YAML chưa là bằng chứng dịch vụ đã chạy.
- Đối chiếu tiêu chí: Có /ready 200 khi model tồn tại và 503 trong ca thiếu model; log run container thật. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 18 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
