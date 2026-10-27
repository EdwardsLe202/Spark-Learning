# Ngày 05 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-05/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Đọc tám dòng dirty và tự đánh dấu lỗi trước khi viết code.
2. Tạo cột lý do theo thứ tự: thiếu customer_id, timestamp lỗi, amount không parse được, amount âm, customer không tồn tại. Dùng customers làm tập khóa tham chiếu.
3. Tách bản ghi lỗi và bản ghi ứng viên hợp lệ. Trong ứng viên, giữ mỗi event_id bản có ingested_at mới nhất; tra Window ở ngày 6 nếu cần.
4. Ghi clean và quarantine thành hai thư mục riêng dưới artifacts/day-05. Ghi số dòng trùng bị bỏ riêng.
5. Tạo báo cáo đối soát đầu vào = lỗi + bản trùng bị bỏ + đầu ra; tính tổng amount của clean.

## Cách chạy

```bash
python scripts/run_day.py 05
```

Lưu đầu ra tự tạo ở `artifacts/day-05/` bằng `output_dir(5)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Đầu vào 8; lỗi 5 (D003–D007); loại bản D002 cũ 1; clean 2 (D001 và D002 mới); tổng clean = 170.000 VND. Báo cáo phải thỏa 8 = 5 + 1 + 2.

## Lỗi dễ gặp và cách điều tra

Điền amount lỗi thành 0 làm mất dấu lỗi; dedup tùy ý; đếm dòng lỗi nhiều lần; dùng cast mà không kiểm tra cấu hình parse.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Tạo DataFrame có array hai phần tử và chạy explode; giải thích số dòng trước sau, gồm trường hợp array rỗng và NULL.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
