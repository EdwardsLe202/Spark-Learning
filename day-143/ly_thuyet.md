# Ngày 143 — Dispatcher validation timeout và lỗi có thể retry

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Dispatcher validation timeout và lỗi có thể retry”. Kết quả cần đạt: Không thực thi tên tùy ý, có loại lỗi rõ và retry hữu hạn.

## Từ mới gắn với bài này

- **Dispatcher (bộ chọn và gọi công cụ)**.
- **Allowlist (danh sách được phép)**.
- **Retryable error (lỗi có thể thử lại)**.

## Tình huống và cách hiểu

**Dispatcher (bộ chọn và gọi công cụ)** chỉ ánh xạ tên đã biết vào callable đã kiểm soát. **Allowlist (danh sách được phép)** không nhận tên hàm/shell tùy ý từ model. Lọc quyền của search_docs dùng cùng role server, không cho arguments tự ghi đè.

**Retryable error (lỗi có thể thử lại)** khác schema sai hoặc tool bị cấm. Timeout cần giới hạn từng tool và tổng request; backend có side effect cần idempotency trước khi retry. Bài chỉ dùng tool giả lập/read-only.

Mẫu thử status, unknown tool và input xấu. Lab bọc kết quả thành ok/error có code rõ, giữ trace và không làm lỗi trở thành một đáp án giả.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-143/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import dispatch_tool
cases = [("get_job_status", {"job_id": "job-001"}), ("unknown_tool", {}), ("get_job_status", {"job_id": "bad"})]
for name, args in cases:
    try:
        print({"ok": True, "result": dispatch_tool(name, args, role="public")})
    except (ValueError, PermissionError) as error:
        print({"ok": False, "error": type(error).__name__})
```

## Đọc từng phần của ví dụ

Tool lạ và tham số sai bị chặn trước thực thi. Không in arbitrary traceback/nội dung nhạy cảm ra user.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Không thực thi tên tùy ý, có loại lỗi rõ và retry hữu hạn.

## Ba câu kiểm tra hiểu bài

1. Dispatcher có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: bộ chọn và gọi công cụ.
- Luồng chính: Tool lạ và tham số sai bị chặn trước thực thi. Không in arbitrary traceback/nội dung nhạy cảm ra user.
- Đối chiếu tiêu chí: Không thực thi tên tùy ý, có loại lỗi rõ và retry hữu hạn. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 28 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
