# Ngày 85 — Cấu hình log exception và exit code

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Cấu hình log exception và exit code”. Kết quả cần đạt: Input version sai trả mã khác 0; không có artifact ngoài vùng chạy được tạo.

## Từ mới gắn với bài này

- **Structured log (log có cấu trúc)**.
- **Exception (ngoại lệ)**.
- **Exit code (mã kết thúc)**.

## Tình huống và cách hiểu

**Structured log (log có cấu trúc)** lưu step, interval, version, số dòng và runtime để tìm lỗi. **Exception (ngoại lệ)** biểu thị tình huống cần xử lý; **exit code (mã kết thúc)** khác 0 cho scheduler biết không được coi là thành công.

Không catch mọi lỗi rồi in xong. Phân biệt input sai không nên retry với lỗi kết nối tạm thời có thể retry có giới hạn. Không log secret hoặc toàn bộ dữ liệu cá nhân chỉ để debug.

Services pipeline ném ValueError khi version sai hoặc candidate không đạt. Ví dụ cố tình dùng version không hợp lệ và kiểm tra mã trả về, thay vì để tác vụ sau vẫn chạy. Log cần gắn request/run ID nhất quán.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-085/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import subprocess
result = subprocess.run([sys.executable, str(ROOT / "services/pipeline.py"), "--step", "train", "--version", "../bad"], capture_output=True, text=True)
print({"exit_code": result.returncode, "rejected": result.returncode != 0})
assert result.returncode != 0
```

## Đọc từng phần của ví dụ

Path traversal bị chặn bằng kiểm tra version; code lỗi không bị biến thành thành công giả.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Input version sai trả mã khác 0; không có artifact ngoài vùng chạy được tạo.

## Ba câu kiểm tra hiểu bài

1. Structured log có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: log có cấu trúc.
- Luồng chính: Path traversal bị chặn bằng kiểm tra version; code lỗi không bị biến thành thành công giả.
- Đối chiếu tiêu chí: Input version sai trả mã khác 0; không có artifact ngoài vùng chạy được tạo. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 16 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
