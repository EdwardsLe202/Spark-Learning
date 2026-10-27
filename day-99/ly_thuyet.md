# Ngày 99 — CI chạy test và tạo artifact

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “CI chạy test và tạo artifact”. Kết quả cần đạt: Có test tái chạy được từ môi trường sạch; CI không tự phát hành production.

## Từ mới gắn với bài này

- **CI — Continuous Integration (kiểm tra khi tích hợp code)**.
- **Build artifact (sản phẩm build có định danh)**.

## Tình huống và cách hiểu

**CI — Continuous Integration (kiểm tra khi tích hợp code)** cần môi trường sạch và fixture không phụ thuộc máy cá nhân. **Build artifact (sản phẩm build có định danh)** phải gắn commit/config để biết mình kiểm tra bản nào.

Workflow nền của repo kiểm tra tài liệu; workflow mở rộng thêm pytest nghiệp vụ trong môi trường Python cố định. Spark test cần Java. Không cho token/cloud credential vào test chỉ vì tiện chạy.

CI xanh chưa tự chấp nhận model hay cho phép deploy. Tách kiểm tra source, chất lượng dữ liệu, model gate và phát hành. Khi branch thay scope, mô tả đúng artifact cuối chứ không liệt kê công nghệ đã thử bỏ đi.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-099/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
path = ROOT / ".github/workflows/course-integration.yml"
print(path.read_text())
print("Chạy tương đương local: python -m pytest tests -q")
```

## Đọc từng phần của ví dụ

Workflow là cấu hình chạy khi push/PR; mẫu không tự gửi code hay tạo release ngoài repo.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có test tái chạy được từ môi trường sạch; CI không tự phát hành production.

## Ba câu kiểm tra hiểu bài

1. CI — Continuous Integration có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: kiểm tra khi tích hợp code.
- Luồng chính: Workflow là cấu hình chạy khi push/PR; mẫu không tự gửi code hay tạo release ngoài repo.
- Đối chiếu tiêu chí: Có test tái chạy được từ môi trường sạch; CI không tự phát hành production. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 19 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
