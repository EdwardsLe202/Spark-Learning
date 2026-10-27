# Ngày 09 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-09/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy một lần warm up (khởi động nóng), rồi đo baseline ba lần. Ghi cấu hình máy, số dòng và từng thời gian.
2. Join bảng lớn giả lập với bảng 10 khóa; so plan mặc định và F.broadcast ở bảng nhỏ. Chỉ thay yếu tố này.
3. Kiểm tra số dòng, tổng id và kết quả theo key giữa hai phiên bản.
4. Đo trường hợp một DataFrame dùng ba lần với cache và không cache; tính cả chi phí action vật hóa cache.
5. Tạo bảng báo cáo gồm cấu hình, median runtime, loại join, shuffle quan sát được và nhận xét giới hạn local.

## Cách chạy

```bash
python scripts/run_day.py 09
```

Lưu đầu ra tự tạo ở `artifacts/day-09/` bằng `output_dir(9)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Group key=0 có 91.000 dòng; mỗi key 1–9 có 1.000. Tổng 100.000. Không có yêu cầu biến thể phải nhanh hơn; phải giải thích bằng dữ liệu đo.

## Lỗi dễ gặp và cách điều tra

Đo lệnh chưa có action; giữ cache từ lần đo trước; chỉ đổi nhiều cấu hình cùng lúc; gọi toPandas trên bảng lớn để xem nhanh.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

So built-in với Python UDF trên dữ liệu vừa máy; xác nhận action sử dụng cột kết quả, vì count đơn thuần có thể bỏ tính cột không cần thiết.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
