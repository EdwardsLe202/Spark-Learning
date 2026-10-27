# Ngày 141 — Prompt injection regression và lỗi dịch vụ

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Prompt injection regression và lỗi dịch vụ”. Kết quả cần đạt: Không chạy tool lạ hoặc cấp role qua prompt; lỗi được trace và dừng đúng budget.

## Từ mới gắn với bài này

- **Prompt injection (nội dung không tin cậy chèn chỉ dẫn)**.
- **Regression test (kiểm thử lỗi quay lại)**.
- **Fail closed (từ chối khi kiểm tra quyền không thành công)**.

## Tình huống và cách hiểu

**Prompt injection (nội dung không tin cậy chèn chỉ dẫn)** có thể nằm trong tài liệu được retrieve. Đặt nó trong context không cho nó quyền gọi tool hoặc đổi role. Prompt phân cách hỗ trợ hành vi nhưng kiểm soát quyền vẫn phải ở code.

**Regression test (kiểm thử lỗi quay lại)** giữ các ca đã từng gây sai sau khi đổi prompt/index/model. **Fail closed (từ chối khi kiểm tra quyền không thành công)** tránh trả context khi không xác định được role. Lỗi index/model cần status và retry hữu hạn.

Doc-injection là payload thử giả lập, không phải lệnh cho bạn thực hiện. Mẫu kiểm tra lọc quyền và allowlist công cụ độc lập model. Lab còn phải thử generation thật để ghi model có bị lệch nhiệm vụ hay không.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-141/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import dispatch_tool, allowed_chunks, chunk_documents, load_corpus
try:
    dispatch_tool("delete_file", {"path": "any"}, role="public")
except PermissionError:
    print("Chặn công cụ ngoài allowlist.")
try:
    allowed_chunks(chunk_documents(load_corpus()), "self-claimed-admin")
except PermissionError:
    print("Chặn role không tin cậy.")
```

## Đọc từng phần của ví dụ

Không có exec/shell hay quyền ghi trong dispatcher. Nội dung tài liệu không thay được danh sách công cụ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Không chạy tool lạ hoặc cấp role qua prompt; lỗi được trace và dừng đúng budget.

## Ba câu kiểm tra hiểu bài

1. Prompt injection có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: nội dung không tin cậy chèn chỉ dẫn.
- Luồng chính: Không có exec/shell hay quyền ghi trong dispatcher. Nội dung tài liệu không thay được danh sách công cụ.
- Đối chiếu tiêu chí: Không chạy tool lạ hoặc cấp role qua prompt; lỗi được trace và dừng đúng budget. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 27 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
