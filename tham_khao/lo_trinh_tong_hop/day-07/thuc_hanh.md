# Ngày 07 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-07/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Ghi tiny ra Parquet theo event_date. Liệt kê file và thư mục để thấy partition theo lưu trữ.
2. Đọc lại và lọc ngày 2025-01-20; tìm PartitionFilters trong plan.
3. Ghi append hai lần vào một đích thử khác, đo số dòng. Ghi overwrite tại chính đích thử rồi đọc lại để thấy phạm vi thay thế.
4. So sánh schema CSV đọc chuỗi và Parquet sau khi đã cast; đối chiếu tổng tiền theo ngày.
5. Ghi data dictionary: tên cột, kiểu, đơn vị tiền, múi giờ, khóa và quy tắc partition.

## Cách chạy

```bash
python scripts/run_day.py 07
```

Lưu đầu ra tự tạo ở `artifacts/day-07/` bằng `output_dir(7)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Bộ tiny có 4 dòng trên 4 ngày; ngày 2025-01-20 có T002. Hai lần append cùng bộ tạo 8 dòng. Không thay đổi data/raw.

## Lỗi dễ gặp và cách điều tra

Nhầm thư mục .parquet với một file; overwrite sai cấp thư mục; suy diễn dữ liệu nhỏ nhanh hơn nghĩa là định dạng luôn tốt hơn.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Viết bản thiết kế chọn Delta hoặc Iceberg, tra compatibility của connector đúng Spark 3.5.7 trước khi thử; không thêm connector vào môi trường chính nếu chưa kiểm tra.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
