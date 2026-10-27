# Ngày 133 — Sparse retrieval TF-IDF và mã chính xác

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Sparse retrieval TF-IDF và mã chính xác”. Kết quả cần đạt: Có baseline từ vựng thật, được gọi đúng tên và không lẫn dense semantic.

## Từ mới gắn với bài này

- **Sparse retrieval (tìm bằng biểu diễn thưa)**.
- **TF-IDF (trọng số từ theo tần suất)**.
- **BM25 (xếp hạng từ vựng)**.

## Tình huống và cách hiểu

**Sparse retrieval (tìm bằng biểu diễn thưa)** thường gắn với từ. **TF-IDF (trọng số từ theo tần suất)** và **BM25 (xếp hạng từ vựng)** có thể tìm mã/thuật ngữ chính xác tốt hơn một số model semantic.

TF-IDF không hiểu nghĩa như dense embedding đã học. Chuẩn hóa Unicode, chữ hoa và cách tách từ ảnh hưởng tiếng Việt. Query dùng từ khác hẳn có thể không khớp dù cùng ý.

Mẫu dùng sklearn TfidfVectorizer trên tập chunk được phép. Không fit vocabulary trên tài liệu ngoài quyền rồi vô tình log chúng. Lab so dense/sparse trên dev và giữ runtime/recall trước khi quyết định kết hợp.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-133/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus, chunk_documents, sparse_search
ranked = sparse_search("mã 422 readiness", chunk_documents(load_corpus()), role="public", k=3)
print([(c["doc_id"], c["score"]) for c in ranked])
```

## Đọc từng phần của ví dụ

Score là cosine của vector TF-IDF được chuẩn hóa mặc định, không là probability nội dung đúng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có baseline từ vựng thật, được gọi đúng tên và không lẫn dense semantic.

## Ba câu kiểm tra hiểu bài

1. Sparse retrieval có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tìm bằng biểu diễn thưa.
- Luồng chính: Score là cosine của vector TF-IDF được chuẩn hóa mặc định, không là probability nội dung đúng.
- Đối chiếu tiêu chí: Có baseline từ vựng thật, được gọi đúng tên và không lẫn dense semantic. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 26 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
