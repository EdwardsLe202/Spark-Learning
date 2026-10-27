# Ngày 135 — Reranker chỉ sửa thứ hạng ứng viên

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Reranker chỉ sửa thứ hạng ứng viên”. Kết quả cần đạt: Có score model reranker thật và báo cáo đánh đổi; không gọi sort score cũ là model reranking.

## Từ mới gắn với bài này

- **Reranker (model chấm lại ứng viên)**.
- **Cross-encoder (model xem query và đoạn cùng nhau)**.

## Tình huống và cách hiểu

**Reranker (model chấm lại ứng viên)** chỉ sắp tập đã được retrieve. **Cross-encoder (model xem query và đoạn cùng nhau)** thường chính xác hơn cách so vector độc lập ở một số tác vụ nhưng tốn công cho từng cặp.

Nếu tài liệu đúng chưa có trong ứng viên, reranker không tìm nó từ ngoài tập. Tăng candidates có thể tăng recall và latency, rồi chọn ít context hơn sau rerank. Lọc quyền trước khi gửi cặp query/text tới model.

Mẫu dùng model reranker thật đã tải. Score không mặc định probability và không cùng thang với embedding. Lab cần đo query tiếng Việt vì tên multilingual không thay benchmark ứng dụng của bạn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-135/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus, chunk_documents, sparse_search, rerank
candidates = sparse_search("Vì sao phải ghi model version?", chunk_documents(load_corpus()), role="public", k=6)
ranked = rerank("Vì sao phải ghi model version?", candidates, k=3)
print([(c["doc_id"], c["reranker_score"]) for c in ranked])
```

## Đọc từng phần của ví dụ

Sparse tạo tập ứng viên hợp lệ, cross-encoder chấm lại đúng tập này. Download reranker là bước riêng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có score model reranker thật và báo cáo đánh đổi; không gọi sort score cũ là model reranking.

## Ba câu kiểm tra hiểu bài

1. Reranker có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: model chấm lại ứng viên.
- Luồng chính: Sparse tạo tập ứng viên hợp lệ, cross-encoder chấm lại đúng tập này. Download reranker là bước riêng.
- Đối chiếu tiêu chí: Có score model reranker thật và báo cáo đánh đổi; không gọi sort score cũ là model reranking. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 26 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
