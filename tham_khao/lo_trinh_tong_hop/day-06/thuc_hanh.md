# Ngày 06 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-06/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Join tiny với customers theo customer_id, tổng hợp tiền theo region. Đối soát tổng tiền trước sau join.
2. Cố tình nhân bản dòng C001 trong bảng customers, join lại và ghi vì sao tổng tiền sai. Thêm kiểm tra phát hiện khóa trùng trước khi ghép.
3. Viết left anti join để tìm customer không tồn tại trong dirty.
4. Dùng row_number giữ D002 mới nhất. Thêm fixture hai dòng bằng timestamp và chốt tiêu chí phụ rõ ràng.
5. Tính lag amount theo customer_id, sắp xếp event_time và event_id; giải thích dòng đầu có NULL. Viết tay sự khác nhau giữa ba giao dịch và ba ngày.

## Cách chạy

```bash
python scripts/run_day.py 06
```

Lưu đầu ra tự tạo ở `artifacts/day-06/` bằng `output_dir(6)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Tổng tiền tiny sau join chuẩn vẫn là 1.250.000 VND. Anti join tìm C999 (và dòng customer_id rỗng nếu chưa lọc). D002 mới có amount 70.000.

## Lỗi dễ gặp và cách điều tra

Dùng distinct sau join để che lỗi quan hệ; groupBy nhầm cấp độ; sắp xếp timestamp bằng nhau nhưng thiếu khóa phụ.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Tạo timestamp số giây, dùng rangeBetween(-7*86400,0); tạo hai giao dịch cùng timestamp và giải thích biên cửa sổ.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
