# Ngày 01 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Môi trường Python chuẩn, không cần cài thư viện ngoài.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-01/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Mở `data/README.md`, xem hai file CSV và ghi ý nghĩa mỗi dòng.
2. Trong phần comment trong `bai_lam.py`, chọn công cụ cho ba tình huống: CSV 20 MB, giao dịch nhiều năm cần tổng hợp theo khách hàng, sự kiện ứng dụng tới liên tục. Ghi cả giả định RAM và yêu cầu thời gian.
3. Vẽ sơ đồ trên bằng Markdown hoặc Mermaid. Gắn tên công cụ vào từng bước.
4. Chạy file khởi động bằng lệnh bên dưới; sửa để in thêm đường dẫn bảng khách hàng.
5. Viết 5–8 câu giải thích vì sao repo dùng dữ liệu nhỏ để học nguyên lý Spark.

## Cách chạy

```bash
python scripts/run_day.py 01
```

Lưu đầu ra tự tạo ở `artifacts/day-01/` bằng `output_dir(1)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Một sơ đồ có nguồn dữ liệu, bước xử lý, nơi lưu model và hai cách dự đoán; ba lựa chọn công cụ có lý do. Không yêu cầu cài Spark trong ngày này.

## Lỗi dễ gặp và cách điều tra

Đồng nhất Spark với database; nghĩ dùng Python nghĩa là mọi dòng đều được xử lý bằng vòng lặp Python; khẳng định local nhiều luồng là cluster.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Ước lượng dữ liệu 1 triệu dòng × 200 byte; giải thích vì sao kích thước file chưa phản ánh đầy đủ bộ nhớ khi xử lý.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
