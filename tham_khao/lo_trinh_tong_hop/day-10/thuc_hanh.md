# Ngày 10 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-10/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy batch mẫu và đọc toàn daily, đối chiếu 3 dòng duy nhất. Lần chạy lại ngày 15 không thêm dòng.
2. Tạo bản nguồn bổ sung một sự kiện ngày 15 có ingested_at muộn, dựng lại riêng ngày đó và kiểm tra ngày khác không đổi.
3. Tạo `artifacts/day-10/stream_in`, chép một file CSV vào đó. Dùng readStream với schema tường minh, header=true; writeStream format parquet, outputMode append, checkpointLocation riêng, trigger(availableNow=True), rồi awaitTermination().
4. Thêm file thứ hai tên mới, chạy lại cùng checkpoint và cùng đích. Đọc đích để đối soát; không sửa nội dung file đã được stream xử lý.
5. Lưu log hai lần chạy; giải thích khác nhau giữa giữ checkpoint và tạo truy vấn mới từ đầu.

## Cách chạy

```bash
python scripts/run_day.py 10
```

Lưu đầu ra tự tạo ở `artifacts/day-10/` bằng `output_dir(10)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Batch ban đầu có 3 dòng cho ba ngày; chạy lại cùng nguồn không tăng số dòng. Stream đọc file mới và giữ tiến độ qua hai lần chạy; có bảng đối soát theo event_id.

## Lỗi dễ gặp và cách điều tra

Dùng append cho retry; overwrite cả gốc thay vì một ngày; xóa checkpoint để chữa lỗi rồi gây đọc lại; thử phục hồi memory sink như sink bền vững.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thêm window theo event_time và watermark; kiểm tra một sự kiện đến muộn, ghi rõ hành vi quan sát theo tiến độ watermark của truy vấn.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
