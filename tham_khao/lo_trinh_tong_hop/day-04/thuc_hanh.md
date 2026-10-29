# Ngày 04 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-04/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy ví dụ và đọc schema trước, sau khi cast.
2. Tự viết DataFrame và SQL để lấy giao dịch của C001, thêm `amount_k = amount / 1000`, đổi tên cột rõ ràng.
3. Tổng hợp số giao dịch và tổng tiền theo customer_id bằng cả hai cách; so sánh hai kết quả sau `orderBy`.
4. Thử đọc `events_dirty.csv`, lọc riêng dòng có amount gốc khác rỗng nhưng cast ra NULL. Lưu danh sách event_id.
5. Viết kết quả và giải thích tại sao không dùng vòng lặp Python qua toàn bảng.

## Cách chạy

```bash
python scripts/run_day.py 04
```

Lưu đầu ra tự tạo ở `artifacts/day-04/` bằng `output_dir(4)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Ví dụ lọc trả T001, T002, T004. Tổng toàn tiny = 1.250.000 VND; C001 = 1.200.000, C002 = 50.000. Hai API phải cho cùng giá trị.

## Lỗi dễ gặp và cách điều tra

Quên gán DataFrame trả về; dùng `and`; so sánh tiền khi cột còn là chuỗi; xem thứ tự từ show như thứ tự cố định.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Viết điều kiện CASE WHEN phân nhóm giao dịch dưới 100.000, từ 100.000 tới 200.000, trên 200.000; kiểm tra chính xác các biên.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
