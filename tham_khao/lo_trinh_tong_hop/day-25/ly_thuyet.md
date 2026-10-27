# Ngày 25 — Lý thuyết: Chuẩn bị tài liệu và xây chỉ mục RAG

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Tạo chunk có nguồn, quyền, phiên bản và cập nhật chỉ mục không sinh bản sao.

## 1. Tách ingest với luồng trả lời
**Ingestion (đưa dữ liệu vào hệ thống)** đọc tài liệu, làm sạch, chia đoạn, tính embedding và tạo index. **Chunk (đoạn văn bản dùng để truy xuất)** cần đủ ngữ cảnh; quá ngắn làm mất ý, quá dài làm loãng bằng chứng. **Chunk overlap (phần giao nhau giữa các đoạn)** giữ liên kết ở biên nhưng có thể tăng nội dung trùng. Cắt theo đoạn hoặc tiêu đề trước khi thử kích thước tùy ý.

**Metadata (thông tin mô tả kèm dữ liệu)** gồm doc_id, chunk_id, source, version, access và content_hash. Một chunk phải truy ngược về đúng phiên bản nguồn. Bài này dùng corpus tự tạo trong repo, không cần tải tài liệu có bản quyền chưa rõ.

## 2. Embedding và index phải cùng hệ quy chiếu
Embedding đưa văn bản tới vector số; **semantic similarity (độ tương đồng ngữ nghĩa)** đo mức gần nhau theo model và hàm đo đã chọn. **Vector store (kho tìm kiếm vector)** giữ vector cùng metadata. Model embedding, revision, số chiều, chuẩn hóa và metric phải được ghi cùng index. Cùng số chiều chưa đủ để trộn vector từ hai model khác nhau.

**Upsert (cập nhật hoặc thêm theo khóa)** giữ thao tác lặp không tạo bản sao nếu ID ổn định. Khi tài liệu sửa, không chỉ thêm chunk mới: cần loại chunk cũ không còn trong bản hiện hành. Khi xóa tài liệu, phải xóa hoặc vô hiệu toàn bộ chunk của nó trong phạm vi truy xuất.

## 3. Bắt đầu nhỏ rồi mở rộng
Bài local có thể lưu JSONL và ma trận vector, hoặc dùng Qdrant local. Dùng Sentence Transformers với model multilingual nhỏ do bạn chọn; ghi tên và revision thực. Nếu chưa tải model, làm nhánh keyword (từ khóa) để kiểm tra pipeline nhưng đánh dấu dense chưa hoàn thành. Spark phù hợp làm sạch hàng loạt; embedding API cần batch, timeout và retry kiểm soát, tránh một lời gọi ngoài cho mỗi dòng UDF.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
import hashlib
import json
from spark_lab import DATA
corpus = [json.loads(line) for line in (DATA / "rag/corpus.jsonl").read_text(encoding="utf-8").splitlines()]
chunks = []
for doc in corpus:
    digest = hashlib.sha256(doc["text"].encode()).hexdigest()
    chunks.append({**doc, "chunk_id": f'{doc["doc_id"]}:{doc["version"]}:000', "content_hash": digest})
print("Tài liệu:", len(corpus), "chunk ban đầu:", len(chunks))
# TODO: tách theo đoạn, lưu index và loại chunk cũ khi sửa/xóa tài liệu.
```

## Năm ý đối chiếu với lộ trình gốc

- 25.1 — RAG gồm ingest, chunk, embed, index, retrieve và generate.
- 25.2 — Trích xuất văn bản, chất lượng parser, chunk size, overlap và ranh giới nội dung.
- 25.3 — Document ID, chunk ID, content hash, nguồn, phiên bản và quyền truy cập.
- 25.4 — Spark làm sạch và dedup hàng loạt; embedding job có batching, rate limit và retry.
- 25.5 — Vector store, upsert, xóa tài liệu, reindex và thay embedding model.

Các ý trên giữ phạm vi phần 25 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Vì sao cần cả doc_id và chunk_id?
2. Cùng chiều vector có bảo đảm tương thích không?
3. Xóa tài liệu cần cập nhật những gì?

## Đọc thêm từ nguồn chính thức

- [Sentence Transformers model card](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)
- [Qdrant local quickstart](https://qdrant.tech/documentation/quickstart/)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
