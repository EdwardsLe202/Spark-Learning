# Ngày 17 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Môi trường Python chuẩn, không cần cài thư viện ngoài.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-17/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Dùng module/CLI ngày 16, viết run_pipeline(snapshot_date) gọi đúng thứ tự và dừng ngay nếu validate lỗi.
2. Cho features thất bại một lần có chủ ý. Thêm retry tối đa 2 lần cho lỗi tạm thời; schema lỗi phải dừng, không retry mù.
3. Backfill snapshot cũ hai lần; kiểm tra cùng số dòng, cùng khóa và cùng hash nội dung đã chuẩn hóa thứ tự.
4. Ghi metadata từng bước vào JSON: run_id, interval, input_hash, output_path, status, duration. Không truyền DataFrame qua cơ chế metadata.
5. Viết runbook (hướng dẫn vận hành) cho nguồn thiếu ngày và feature lỗi. Nếu học sâu Airflow, chuyển workflow sang DAG theo docs/CAI_DAT.md và kiểm chứng retry trên UI.

## Cách chạy

```bash
python scripts/run_day.py 17
```

Lưu đầu ra tự tạo ở `artifacts/day-17/` bằng `output_dir(17)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Có workflow local chạy tác vụ thật, không chỉ in tên bước; một lỗi validate chặn score, retry feature không nhân dữ liệu. Nếu chưa chạy scheduler, ghi rõ Airflow mới ở mức thiết kế.

## Lỗi dễ gặp và cách điều tra

Dùng ngày hiện tại thay ngày dữ liệu; retry vô hạn; scheduler tự train lại mọi thứ khi chỉ cần score; truyền bảng lớn qua XCom (kênh metadata của Airflow).

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Triển khai Airflow trong môi trường riêng, giới hạn một DAG run đồng thời và thử backfill; lưu ảnh cùng log tác vụ thực sự chạy.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
