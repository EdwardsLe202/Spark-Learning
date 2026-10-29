# Ngày 25 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Môi trường `requirements-ai.txt` cho dense retrieval; corpus và eval có sẵn trong `data/rag/`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-25/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Đọc data/rag/README.md và corpus.jsonl. Tách theo đoạn, thử chunk size khoảng 200–400 ký tự cho corpus nhỏ; ghi đây là ký tự, không gọi là token.
2. Tạo ID ổn định theo doc_id, version và vị trí chunk, kèm content_hash. Chạy ingest hai lần và kiểm tra số ID duy nhất không đổi.
3. Tính embedding bằng model hỗ trợ tiếng Việt (gợi ý paraphrase-multilingual-MiniLM-L12-v2), ghi revision thực và chuẩn hóa nếu dùng cosine. Tải model lần đầu cần mạng và dung lượng local, không cần API trả phí.
4. Lưu vector và metadata cùng manifest; kiểm tra model/index tương thích trước truy xuất. Có thể dùng Qdrant local thay file, không bắt buộc khởi động server.
5. Sửa một doc và xóa một doc trên bản sao corpus trong artifacts. Reindex và kiểm tra chunk cũ không còn truy xuất được; giữ corpus gốc cho benchmark.

## Cách chạy

```bash
python scripts/run_day.py 25
```

Lưu đầu ra tự tạo ở `artifacts/day-25/` bằng `output_dir(25)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Corpus gốc có 8 tài liệu. Rerun không tăng ID; chunk truy ngược được nguồn và version. Sau xóa, không còn chunk của doc đã xóa. Dense index cần model thật; keyword/mock không tính như đã làm embedding.

## Lỗi dễ gặp và cách điều tra

Đổi embedding model nhưng giữ index cũ; content_hash thay cho toàn bộ lịch sử; upsert mới nhưng bỏ sót chunk cũ; nhầm ký tự với token.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Dùng Spark dedup corpus lớn hơn rồi xuất batch embedding; thêm manifest để phát hiện pipeline đang đọc lẫn hai revision model.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
