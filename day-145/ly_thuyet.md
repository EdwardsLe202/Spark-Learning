# Ngày 145 — Nghiệm thu dự án 3 RAG có đánh giá

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Nghiệm thu dự án 3 RAG có đánh giá”. Kết quả cần đạt: Có dense/generation thật, eval, ACL context 0 vi phạm và runbook; phần chưa làm ghi chưa đạt.

## Từ mới gắn với bài này

- **End-to-end evaluation (đánh giá toàn luồng)**.
- **Index rollback (quay về chỉ mục trước)**.

## Tình huống và cách hiểu

**End-to-end evaluation (đánh giá toàn luồng)** tách retrieval và generation, chấm cả quyền/citation. **Index rollback (quay về chỉ mục trước)** cần corpus/chunk/embedding revision tương thích, không chỉ đổi một tên collection.

Dự án 3 có ingest update/delete, dense baseline và hybrid/reranker, 40 câu có nhãn, trace và xử lý thiếu bằng chứng. Tool workflow chỉ thêm khi hữu ích; fine-tune không là điều kiện bắt buộc để hệ RAG hoạt động đúng.

Mỗi phần cần bằng chứng thật. Keyword fixture, model proposal mô phỏng hoặc parser pass chưa thay dense/generation thật. Nếu chất lượng model nhỏ kém, báo metric/lỗi và giới hạn tài nguyên, đừng sửa nhãn test cho đẹp.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-145/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus, eval_queries
print({"documents": len(load_corpus()), "eval_cases": len(eval_queries())})
print("Nghiệm thu:", ROOT / "projects/04-rag-workflow/README.md")
print("Cần output/trace/grade thực, không chỉ đếm file.")
```

## Đọc từng phần của ví dụ

Mẫu nhắc đầu vào và checklist. Demo toàn luồng là phần người học đã tích lũy từ các ngày trước.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có dense/generation thật, eval, ACL context 0 vi phạm và runbook; phần chưa làm ghi chưa đạt.

## Ba câu kiểm tra hiểu bài

1. End-to-end evaluation có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đánh giá toàn luồng.
- Luồng chính: Mẫu nhắc đầu vào và checklist. Demo toàn luồng là phần người học đã tích lũy từ các ngày trước.
- Đối chiếu tiêu chí: Có dense/generation thật, eval, ACL context 0 vi phạm và runbook; phần chưa làm ghi chưa đạt. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 30 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
