# Ngày 03 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-03/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Trước khi chạy, tính tay số phần tử chia hết cho 3 từ 0 tới 99.
2. Chạy ví dụ; ghi nơi có `Exchange` và giải thích vì sao phải nhóm các khóa.
3. Thêm hai action `count()` rồi `show()`. Xem Spark UI khi giữ phiên bằng `input()`; ghi số job thực tế, không đoán một action luôn bằng đúng một job.
4. Đổi số partition đầu vào từ 4 thành 2 rồi 8. Đối chiếu task và kết quả.
5. Vẽ quan hệ application → job → stage → task vào `ghi_chu.md`.

## Cách chạy

```bash
python scripts/run_day.py 03
```

Lưu đầu ra tự tạo ở `artifacts/day-03/` bằng `output_dir(3)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Ba nhóm bucket 0, 1, 2 lần lượt có 34, 33, 33 dòng. Kết quả không đổi khi đổi partition; có ghi nhận thực tế từ plan hoặc UI.

## Lỗi dễ gặp và cách điều tra

Gọi collect với dữ liệu lớn sẽ đưa dữ liệu về driver; nhầm task với một dòng dữ liệu; lấy số stage local làm quy luật cho mọi truy vấn.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Tắt AQE cho một lần quan sát rồi bật lại; mô tả sự khác nhau và giữ cấu hình gốc cho ngày tiếp theo.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
