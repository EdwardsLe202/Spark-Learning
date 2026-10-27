# Ngày 81 — Tách notebook thành module và CLI

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Tách notebook thành module và CLI”. Kết quả cần đạt: Có help, lệnh tái chạy và module không tạo side effect khi import.

## Từ mới gắn với bài này

- **Module (đơn vị mã nguồn)**.
- **CLI — Command Line Interface (giao diện dòng lệnh)**.
- **Code reference (định danh code của lần chạy)**.

## Tình huống và cách hiểu

**Module (đơn vị mã nguồn)** chứa hàm có thể import mà không tự chạy toàn bộ job. **CLI — Command Line Interface (giao diện dòng lệnh)** nhận tham số như ngày dữ liệu, version và đích, thay vì sửa hằng số mỗi lần chạy.

Tách đọc/ghi khỏi logic biến đổi giúp kiểm thử dễ. Giữ main ở if __name__ để import không ghi file hay train. **Code reference (định danh code của lần chạy)** cần biết cả nội dung chưa commit; chỉ log HEAD khi working tree đang đổi chưa đủ tái lập.

Services/pipeline.py là chương trình tham chiếu đã tách validate/features/train/evaluate/score. Đọc một bước trước, rồi tự tách code dự án của bạn. Đừng tạo nhiều thư mục rỗng mà chưa có lệnh chạy thật.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-081/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import subprocess
result = subprocess.run([sys.executable, str(ROOT / "services/pipeline.py"), "--help"], capture_output=True, text=True, check=True)
print(result.stdout)
print("SHA code:", __import__("hashlib").sha256((ROOT / "services/pipeline.py").read_bytes()).hexdigest())
```

## Đọc từng phần của ví dụ

--help kiểm tra CLI không chạy train. Hash gắn với nội dung code hiện tại.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có help, lệnh tái chạy và module không tạo side effect khi import.

## Ba câu kiểm tra hiểu bài

1. Module có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đơn vị mã nguồn.
- Luồng chính: --help kiểm tra CLI không chạy train. Hash gắn với nội dung code hiện tại.
- Đối chiếu tiêu chí: Có help, lệnh tái chạy và module không tạo side effect khi import. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 16 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
