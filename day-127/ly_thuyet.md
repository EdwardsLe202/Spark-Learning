# Ngày 127 — Parser chunk boundary size và overlap

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Parser chunk boundary size và overlap”. Kết quả cần đạt: Mọi chunk có nguồn; size được mô tả đúng đơn vị, không lấy nhiều chunk làm thước đo chất lượng.

## Từ mới gắn với bài này

- **Chunk (đoạn để truy xuất)**.
- **Overlap (phần giao giữa các đoạn)**.
- **Parser quality (chất lượng trích xuất nguồn)**.

## Tình huống và cách hiểu

**Chunk (đoạn để truy xuất)** cần đủ ngữ cảnh để câu hỏi có bằng chứng. **Overlap (phần giao giữa các đoạn)** giữ liên kết ở biên nhưng có thể tăng trùng và chi phí. **Parser quality (chất lượng trích xuất nguồn)** sai thì embedding tốt cũng không cứu được bằng chứng đã mất.

Bắt đầu tách theo đoạn/tiêu đề rồi mới cắt khi quá dài. Helper dùng số ký tự vì corpus nhỏ; không gọi size=400 là 400 token. Đánh giá cả đoạn bị cắt ngang ý, bảng và ký hiệu đặc biệt.

Chỉ đổi một cấu hình trên dev để so. Nếu sửa chunk sau khi xem test, báo đó là vòng tuning mới chứ không phải test độc lập cũ.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-127/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus, chunk_documents
for size, overlap in [(200, 30), (400, 60)]:
    chunks = chunk_documents(load_corpus(), size=size, overlap=overlap)
    print(size, overlap, len(chunks), max(len(c["text"]) for c in chunks))
print("Đơn vị size/overlap là ký tự trong helper mẫu.")
```

## Đọc từng phần của ví dụ

Helper giữ metadata ở mỗi chunk. So số chunk và chiều dài chỉ là kiểm tra cơ học, vẫn cần đọc nội dung.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Mọi chunk có nguồn; size được mô tả đúng đơn vị, không lấy nhiều chunk làm thước đo chất lượng.

## Ba câu kiểm tra hiểu bài

1. Chunk có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đoạn để truy xuất.
- Luồng chính: Helper giữ metadata ở mỗi chunk. So số chunk và chiều dài chỉ là kiểm tra cơ học, vẫn cần đọc nội dung.
- Đối chiếu tiêu chí: Mọi chunk có nguồn; size được mô tả đúng đơn vị, không lấy nhiều chunk làm thước đo chất lượng. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 25 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
