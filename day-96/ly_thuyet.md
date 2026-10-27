# Ngày 96 — Build image và chạy batch từ môi trường sạch

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Build image và chạy batch từ môi trường sạch”. Kết quả cần đạt: Có image chạy được và 120 prediction từ container, không dựa file ẩn trong notebook.

## Từ mới gắn với bài này

- **Dockerfile (tệp mô tả build image)**.
- **Build context (tập tệp gửi cho builder)**.

## Tình huống và cách hiểu

**Dockerfile (tệp mô tả build image)** giữ cách cài runtime/dependency. **Build context (tập tệp gửi cho builder)** cần loại .env, cache và model lớn không cần thiết bằng .dockerignore.

Services/Dockerfile dùng nhánh sklearn nhẹ, không cần JVM trong API. Artifact được gắn ngoài để đổi version. Model phải được tạo trước bằng CLI, không để API train khi khởi động rồi gọi là serving ổn định.

Build và chạy từ image kiểm chứng môi trường khác terminal của bạn. Ghi lệnh và log, kiểm tra file đầu ra qua volume. Model Spark phải dùng image có Java/Spark, không nhét nó vào runtime sklearn rồi hy vọng load được.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-096/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
path = ROOT / "services/Dockerfile"
print(path.read_text())
print("Lab: docker build -f services/Dockerfile -t spark-course-api:local .")
print("Đọc .dockerignore trước khi build; ví dụ này chưa build image.")
```

## Đọc từng phần của ví dụ

Mẫu hiển thị cấu hình, không giả vờ đã chạy Docker. Lab có lệnh build và batch đầy đủ trong hướng dẫn.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có image chạy được và 120 prediction từ container, không dựa file ẩn trong notebook.

## Ba câu kiểm tra hiểu bài

1. Dockerfile có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tệp mô tả build image.
- Luồng chính: Mẫu hiển thị cấu hình, không giả vờ đã chạy Docker. Lab có lệnh build và batch đầy đủ trong hướng dẫn.
- Đối chiếu tiêu chí: Có image chạy được và 120 prediction từ container, không dựa file ẩn trong notebook. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 18 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
