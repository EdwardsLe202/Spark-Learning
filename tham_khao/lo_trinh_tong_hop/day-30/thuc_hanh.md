# Ngày 30 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Môi trường Python chuẩn, không cần cài thư viện ngoài.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-30/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Đối chiếu ba README dự án, điền đường dẫn bằng chứng cho từng tiêu chí. Sửa lỗi về thời gian, khóa và quyền trước khi thêm công nghệ.
2. Tạo môi trường mới theo docs/CAI_DAT.md, dùng output path mới. Chạy data → features → train/load → score → API và ingest → retrieve → answer/eval theo phạm vi đã hoàn thành.
3. Demo một file lỗi, một backfill, một candidate bị từ chối, một rollback, câu hỏi không có nguồn và tài liệu ngoài quyền.
4. Viết data dictionary, model card, release manifest, runbook và báo cáo retrieval/generation. Chỉ gắn số liệu đo thật, ghi máy và dữ liệu.
5. Chuẩn bị demo 10 phút: 2 phút kiến trúc, 3 phút tính đúng, 2 phút MLOps/API, 2 phút RAG, 1 phút giới hạn. Ghi 5 việc học tiếp theo bằng lỗ hổng thực tế.

## Cách chạy

```bash
python scripts/run_day.py 30
```

Lưu đầu ra tự tạo ở `artifacts/day-30/` bằng `output_dir(30)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Ba mốc có checklist và bằng chứng. Người khác có thể chạy theo README; mọi phần chưa chạy được đánh dấu rõ. Có kịch bản demo và rubric tự chấm, không chỉ ảnh giao diện.

## Lỗi dễ gặp và cách điều tra

Dồn toàn bộ dự án vào ngày cuối; gọi mock là production; sửa số liệu cho đẹp; tài liệu chỉ chạy được bằng đường dẫn máy cá nhân.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Nhờ người khác chạy từ hướng dẫn mà không giải thích miệng; ghi lại chỗ họ mắc và sửa README trước khi chia sẻ portfolio.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
