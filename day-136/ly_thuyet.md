# Ngày 136 — Recall MRR nDCG và tách dev test

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Recall MRR nDCG và tách dev test”. Kết quả cần đạt: Có metric đúng đơn vị doc, không tuning trên test hoặc chia Recall cho nhóm không có relevant.

## Từ mới gắn với bài này

- **Recall@k (tỷ lệ tài liệu liên quan tìm được)**.
- **MRR (nghịch đảo hạng đúng đầu tiên trung bình)**.
- **nDCG (chất lượng thứ hạng có chuẩn hóa)**.

## Tình huống và cách hiểu

**Recall@k (tỷ lệ tài liệu liên quan tìm được)** cần mẫu số là toàn bộ relevant đã gán nhãn. **MRR (nghịch đảo hạng đúng đầu tiên trung bình)** đo tài liệu đúng đầu tiên. **nDCG (chất lượng thứ hạng có chuẩn hóa)** dùng mức liên quan và vị trí; helper hiện dùng nhãn nhị phân.

Bộ query gán nhãn doc_id, nên gộp chunk về doc duy nhất trước khi lấy top-k và chấm. Câu không có relevant không chia Recall cho 0; đánh giá từ chối riêng. Nhãn chưa đầy đủ cần version lại bộ eval, không âm thầm sửa sau khi xem test.

Chọn cấu hình trên dev=16 câu, giữ test=24 cho chấm cuối. Chỉ dùng nhóm có relevant cho metric retrieval và báo số câu thực được tính.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-136/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import retrieval_metrics, eval_queries, chunk_documents, load_corpus, sparse_search, doc_ids
print(retrieval_metrics(["wrong", "right"], ["right"], k=2))
chunks = chunk_documents(load_corpus())
rows = []
for case in eval_queries("dev"):
    if case["relevant_doc_ids"]:
        ranked = sparse_search(case["query"], chunks, role=case["user_role"], k=10)
        rows.append({"query_id": case["query_id"], **retrieval_metrics(doc_ids(ranked), case["relevant_doc_ids"], k=3)})
write_json(out / "sparse_dev_metrics.json", rows)
print("Số câu có relevant được chấm:", len(rows))
```

## Đọc từng phần của ví dụ

Fixture wrong/right cho recall=1 và MRR=0.5. Sparse dev là benchmark từ vựng, chưa là dense baseline.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có metric đúng đơn vị doc, không tuning trên test hoặc chia Recall cho nhóm không có relevant.

## Ba câu kiểm tra hiểu bài

1. Recall@k có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tỷ lệ tài liệu liên quan tìm được.
- Luồng chính: Fixture wrong/right cho recall=1 và MRR=0.5. Sparse dev là benchmark từ vựng, chưa là dense baseline.
- Đối chiếu tiêu chí: Có metric đúng đơn vị doc, không tuning trên test hoặc chia Recall cho nhóm không có relevant. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 26 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
