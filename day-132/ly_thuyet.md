# Ngày 132 — Dense retrieval có lọc quyền

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Dense retrieval có lọc quyền”. Kết quả cần đạt: Có score embedding thật; không có doc sai quyền trong top-k.

## Từ mới gắn với bài này

- **Dense retrieval (tìm bằng vector đặc)**.
- **Top-k (k kết quả đầu)**.
- **Trusted role (vai trò từ tầng xác thực)**.

## Tình huống và cách hiểu

**Dense retrieval (tìm bằng vector đặc)** so vector query và các chunk được phép. **Top-k (k kết quả đầu)** quyết định số bằng chứng đưa tới các bước sau. **Trusted role (vai trò từ tầng xác thực)** không lấy từ lời người hỏi tự nhận admin.

Với corpus nhỏ, helper lọc tập được phép trước rồi encode/rank. Điều này chậm hơn index sẵn nhưng dễ hiểu và đúng ranh giới quyền. Bài store ngày 130 cho hướng lưu vector khi mở rộng.

Không kết luận retrieval tốt từ một câu hợp ý. Ngày 136 đo trên bộ query có nhãn. Giữ query tiếng Việt và ghi revision embedding; khi đổi model cần tạo baseline mới rõ ràng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-132/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus, chunk_documents, dense_search
ranked = dense_search("local[2] là hai máy hay hai luồng?", chunk_documents(load_corpus()), role="public", k=3)
print([(c["doc_id"], c["score"]) for c in ranked])
assert all(c["access"] == "public" for c in ranked)
```

## Đọc từng phần của ví dụ

Đây là dense model thật; filter trước ranking. Top-k có thể gồm nhiều chunk cùng doc, cần gộp doc khi chấm nhãn doc.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có score embedding thật; không có doc sai quyền trong top-k.

## Ba câu kiểm tra hiểu bài

1. Dense retrieval có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tìm bằng vector đặc.
- Luồng chính: Đây là dense model thật; filter trước ranking. Top-k có thể gồm nhiều chunk cùng doc, cần gộp doc khi chấm nhãn doc.
- Đối chiếu tiêu chí: Có score embedding thật; không có doc sai quyền trong top-k. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 26 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
