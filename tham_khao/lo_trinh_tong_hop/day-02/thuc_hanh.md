# Ngày 02 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-02/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Làm theo `docs/CAI_DAT.md`; dùng `uname -m`, `python --version` và `java -version` để ghi kiến trúc, Python và Java.
2. Cài duy nhất `requirements.txt` vào môi trường riêng, rồi chạy file khởi động.
3. Thêm kiểm tra schema và tổng sau khi đọc Parquet, không chỉ kiểm tra số dòng.
4. Mở terminal mới, kích hoạt lại môi trường và chạy lại. Kết quả phải giống nhau.
5. Khi cần xem UI, thêm `input("Enter để kết thúc")` bên trong khối có Spark, mở UI rồi mới Enter. Ghi một ảnh hoặc mô tả vào nhật ký.

## Cách chạy

```bash
python scripts/run_day.py 02
```

Lưu đầu ra tự tạo ở `artifacts/day-02/` bằng `output_dir(2)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

In `Smoke check: 2 dòng, tổng = 5`; có thư mục `artifacts/day-02/smoke_parquet`. Ghi đủ lệnh, phiên bản và kết quả đọc lại.

## Lỗi dễ gặp và cách điều tra

`JAVA_GATEWAY_EXITED`: kiểm tra Java và JAVA_HOME. `ModuleNotFoundError`: kiểm tra interpreter và môi trường. Không dùng Python 3.14 chỉ vì đó là lệnh python3 mặc định trên máy.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Tạo notebook dùng đúng interpreter; ghi lại cách chọn kernel nhưng vẫn giữ script là cách tái chạy chính.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
