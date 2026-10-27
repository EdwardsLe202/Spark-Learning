# Ngày 126 — RAG ingest tách khỏi luồng hỏi đáp

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “RAG ingest tách khỏi luồng hỏi đáp”. Kết quả cần đạt: 8 tài liệu có source/version/access; không gọi đọc JSON là đã hoàn thành RAG.

## Từ mới gắn với bài này

- **RAG — Retrieval-Augmented Generation (sinh câu trả lời có truy xuất)**.
- **Ingestion (đưa tài liệu vào hệ thống)**.
- **Online path (luồng trả lời yêu cầu)**.

## Tình huống và cách hiểu

**RAG — Retrieval-Augmented Generation (sinh câu trả lời có truy xuất)** đưa bằng chứng được tìm vào context cho model. **Ingestion (đưa tài liệu vào hệ thống)** đọc/chunk/embed/index; **online path (luồng trả lời yêu cầu)** kiểm tra quyền/retrieve/generate/validate.

Không nhúng lại toàn bộ corpus hoặc chạy SparkSession mỗi khi có câu hỏi. Spark phù hợp làm sạch batch khi quy mô cần; online retrieval có runtime riêng. Corpus repo có quyền sử dụng rõ vì được tự tạo.

Bài chỉ đọc tám tài liệu và vẽ hai luồng. Tài liệu có access=internal phải được bảo vệ bằng code, không nhờ model tự quyết định ai là admin. Giữ version nguồn trước khi chia chunk.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-126/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus
corpus = load_corpus()
print([(doc["doc_id"], doc["access"], doc["version"]) for doc in corpus])
assert len(corpus) == 8
print("Ingest: parse→chunk→embed→index; online: quyền→retrieve→generate→validate.")
```

## Đọc từng phần của ví dụ

Chỉ xem metadata, chưa embedding/generation. Source repo:// là định danh nội bộ của lab, không phải URL web.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

8 tài liệu có source/version/access; không gọi đọc JSON là đã hoàn thành RAG.

## Ba câu kiểm tra hiểu bài

1. RAG — Retrieval-Augmented Generation có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: sinh câu trả lời có truy xuất.
- Luồng chính: Chỉ xem metadata, chưa embedding/generation. Source repo:// là định danh nội bộ của lab, không phải URL web.
- Đối chiếu tiêu chí: 8 tài liệu có source/version/access; không gọi đọc JSON là đã hoàn thành RAG. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 25 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
