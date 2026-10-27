# Ngày 26 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường `requirements-ai.txt` cho dense retrieval; corpus và eval có sẵn trong `data/rag/`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-26/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Đọc queries.jsonl; chỉ dùng split=dev để chọn chunk size, top-k và cấu hình. Giữ split=test cho báo cáo cuối.
2. Tạo baseline dense ngày 25. Lọc access dựa trên user_role tin cậy ở server trước truy xuất, không tin role do prompt tự nhận.
3. Thêm một nhánh TF-IDF/BM25; hợp nhất bằng RRF hoặc thêm reranker thật. Không gọi một lần sort score cũ là reranking bằng model.
4. Tính Recall@1/@3 và MRR theo doc_id cho các câu có relevant hợp lệ; đo median/p95 latency và ghi lỗi. Tách nhóm unanswerable/ambiguous/forbidden.
5. Chọn cấu hình trên dev rồi đánh giá test; phân tích ít nhất 5 truy vấn sai hoặc khó bằng nguồn → chunk → embedding → retrieval → ranking.

## Cách chạy

```bash
python scripts/run_day.py 26
```

Lưu đầu ra tự tạo ở `artifacts/day-26/` bằng `output_dir(26)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Ví dụ Recall@2=1.0. Báo cáo có dense baseline và biến thể, split rõ, metric theo đúng đơn vị doc_id và kiểm tra quyền. Nếu nhãn đều đúng, phân tích 5 ca khó thay vì bịa lỗi.

## Lỗi dễ gặp và cách điều tra

Đánh giá theo chunk nhưng nhãn theo doc; tuning trên test; cộng score khác thang; coi reranker chữa được nguồn thiếu.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thêm graded relevance (mức liên quan nhiều cấp) để tính nDCG; đo đánh đổi top-k tăng với latency và groundedness của câu trả lời.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
