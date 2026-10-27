# Ngày 140 — ACL trước retrieval và context

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “ACL trước retrieval và context”. Kết quả cần đạt: Permission violations ở context bằng 0; không coi prompt nhắc quyền là đủ.

## Từ mới gắn với bài này

- **ACL — Access Control List (danh sách quyền)**.
- **Tenant (nhóm dữ liệu tách biệt)**.
- **Authorization filter (bộ lọc theo quyền)**.

## Tình huống và cách hiểu

**ACL — Access Control List (danh sách quyền)** cần được kiểm tra trong hoặc trước truy xuất. **Tenant (nhóm dữ liệu tách biệt)** không lấy từ lời model suy đoán. **Authorization filter (bộ lọc theo quyền)** phải dùng role/danh tính tin cậy do server cấp.

Không retrieve toàn bộ rồi đưa context tới model và mới xóa câu trả lời ngoài quyền. Ở corpus nhỏ, allowed_chunks lọc trước tính score. Trong vector store lớn, dùng payload filter tương đương và test đường gọi thực.

CLI có role để giả lập fixture nội bộ, không có nghĩa web user được tự truyền role=internal. Test cả chiều public bị chặn và internal được đọc theo policy, kể cả query chứa câu tự nhận admin.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-140/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import chunk_documents, load_corpus, allowed_chunks
chunks = chunk_documents(load_corpus())
public = allowed_chunks(chunks, "public")
internal = allowed_chunks(chunks, "internal")
assert all(c["access"] == "public" for c in public)
assert any(c["doc_id"] == "doc-internal" for c in internal)
print("Public/internal chunks:", len(public), len(internal))
```

## Đọc từng phần của ví dụ

Role truyền từ fixture tin cậy. Câu hỏi tự nhận admin chưa được đưa vào phép quyết định quyền.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Permission violations ở context bằng 0; không coi prompt nhắc quyền là đủ.

## Ba câu kiểm tra hiểu bài

1. ACL — Access Control List có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: danh sách quyền.
- Luồng chính: Role truyền từ fixture tin cậy. Câu hỏi tự nhận admin chưa được đưa vào phép quyết định quyền.
- Đối chiếu tiêu chí: Permission violations ở context bằng 0; không coi prompt nhắc quyền là đủ. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 27 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
