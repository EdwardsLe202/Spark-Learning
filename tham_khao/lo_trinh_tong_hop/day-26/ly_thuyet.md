# Ngày 26 — Lý thuyết: Truy xuất hybrid search và reranking

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: So sánh hai cấu hình retrieval trên query có nhãn và đo chất lượng cùng latency.

## 1. Những cách tìm kiếm bổ sung nhau
**Dense retrieval (truy xuất bằng vector đặc)** tìm gần về biểu diễn ngữ nghĩa. **Sparse retrieval (truy xuất bằng biểu diễn thưa)** thường gắn với từ hoặc đặc trưng từ vựng; **keyword search (tìm kiếm từ khóa)** hữu ích cho mã và thuật ngữ chính xác. TF-IDF hoặc BM25 là các cách xếp hạng từ vựng, không đồng nghĩa embedding ngữ nghĩa.

**Hybrid search (tìm kiếm kết hợp)** trộn các nguồn ứng viên. Không cộng bừa hai score khác thang đo. **Reciprocal Rank Fusion — RRF (hợp nhất dựa trên nghịch đảo thứ hạng)** là một cách kết hợp thứ hạng thay vì score gốc. Chốt cách khử trùng doc hoặc chunk khi đánh giá.

## 2. Quyền phải lọc trước khi chọn context
**Top-k (k kết quả đứng đầu)** xác định số ứng viên lấy về. **Metadata filter (bộ lọc theo thông tin mô tả)** chặn tài liệu sai quyền hoặc sai phiên bản ngay trong bước truy xuất. Lấy top-k toàn cục rồi bỏ tài liệu cấm có thể làm mất recall và không an toàn nếu context đã đi tới model. Với corpus nhỏ có thể lọc tập được phép trước rồi tính similarity.

**Reranker (mô hình hoặc bộ chấm điểm xếp lại ứng viên)** chỉ sắp xếp tập đã được lấy. Nếu tài liệu đúng không có trong ứng viên, reranker không thể tạo ra nó. Lấy nhiều hơn có thể tăng recall nhưng làm tăng nhiễu và latency.

## 3. Đo trước khi kết luận
**Recall@k (tỷ lệ tài liệu liên quan tìm được trong k kết quả)** = số relevant tìm thấy / tổng relevant đã gán nhãn. **MRR — Mean Reciprocal Rank (trung bình nghịch đảo hạng kết quả liên quan đầu tiên)** đo vị trí kết quả đúng đầu tiên. **nDCG (độ tốt thứ hạng đã chuẩn hóa có chiết khấu)** phù hợp nhãn liên quan nhiều mức. Corpus này gán nhãn theo doc_id; gộp chunk về doc trước khi tính metric. Câu không có tài liệu đúng cần metric từ chối riêng, không chia Recall cho 0.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
def recall_at_k(ranked_doc_ids, relevant_doc_ids, k):
    relevant = set(relevant_doc_ids)
    if not relevant:
        return None  # Đánh giá câu không có đáp án bằng metric khác.
    return len(set(ranked_doc_ids[:k]) & relevant) / len(relevant)
print(recall_at_k(["doc-api", "doc-spark", "doc-rag"], ["doc-spark"], 2))
# TODO: thay danh sách mẫu bằng output retrieval trên corpus thật.
```

## Năm ý đối chiếu với lộ trình gốc

- 26.1 — Dense retrieval, sparse retrieval, keyword search và hybrid search.
- 26.2 — Top k, metadata filter, phân quyền truy xuất và các truy vấn theo phiên bản.
- 26.3 — Reranker, lựa chọn context và ảnh hưởng đến độ trễ.
- 26.4 — Recall at k, MRR, nDCG và mức độ đầy đủ của nhãn relevance.
- 26.5 — Phân tích lỗi do parser, chunk, embedding, retrieval và ranking.

Các ý trên giữ phạm vi phần 26 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Reranker có tìm tài liệu ngoài ứng viên không?
2. Câu không có relevant tính Recall thế nào?
3. Vì sao cần lọc quyền trước context?

## Đọc thêm từ nguồn chính thức

- [Qdrant hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
