# Ngày 95 — Image container volume và kiến trúc máy

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Image container volume và kiến trúc máy”. Kết quả cần đạt: Có kết quả Docker thật và giải thích vòng đời dữ liệu, hoặc đánh dấu runtime chưa cài.

## Từ mới gắn với bài này

- **Image (mẫu môi trường)**.
- **Container (tiến trình từ image)**.
- **Volume (vùng lưu gắn ngoài)**.

## Tình huống và cách hiểu

**Image (mẫu môi trường)** chứa runtime và dependency. **Container (tiến trình từ image)** là một lần chạy. **Volume (vùng lưu gắn ngoài)** giữ artifact sau khi container bị thay. Xóa container không có nghĩa file trong volume bị xóa.

Mac Apple Silicon thường là ARM, nhiều server là x86. Image build trên một kiến trúc chưa được coi là kiểm chứng kiến trúc khác. Thư viện có wheel/native dependency cần tương thích.

Mẫu kiểm tra Docker CLI/daemon nếu có, không tự khởi động hay cài Docker. Lab ghi rõ phần đã chạy. Không dùng venv sạch để đánh dấu rằng image đã build nếu chưa thực hiện Docker build/run.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-095/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import platform, shutil, subprocess
print("Kiến trúc Python:", platform.machine())
if shutil.which("docker"):
    result = subprocess.run(["docker", "version"], capture_output=True, text=True)
    print("Docker daemon khả dụng:", result.returncode == 0)
else:
    print("Chưa có Docker CLI; làm cài đặt runtime trước lab.")
```

## Đọc từng phần của ví dụ

CLI có mặt chưa chắc daemon chạy. Kiểm tra chỉ đọc trạng thái, không kéo image hay mở dịch vụ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có kết quả Docker thật và giải thích vòng đời dữ liệu, hoặc đánh dấu runtime chưa cài.

## Ba câu kiểm tra hiểu bài

1. Image có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mẫu môi trường.
- Luồng chính: CLI có mặt chưa chắc daemon chạy. Kiểm tra chỉ đọc trạng thái, không kéo image hay mở dịch vụ.
- Đối chiếu tiêu chí: Có kết quả Docker thật và giải thích vòng đời dữ liệu, hoặc đánh dấu runtime chưa cài. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 18 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
