# Ngày 08 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-08/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy word count và giải thích kiểu dữ liệu sau từng phép biến đổi.
2. Viết lại bằng DataFrame: split → explode → groupBy → count; đối chiếu từ và số lần.
3. Đổi repartition thành 2, 4, 8 và xem plan/UI. Ghi số partition trước sau coalesce(2).
4. Ghi mỗi biến thể vào một đích riêng; so số part-file nhưng không kết luận luôn một file cho mọi cấu hình.
5. Viết kịch bản task gửi email rồi bị retry. Đề xuất khóa chống gửi lặp, không thực sự gửi email.

## Cách chạy

```bash
python scripts/run_day.py 08
```

Lưu đầu ra tự tạo ở `artifacts/day-08/` bằng `output_dir(8)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Word count: ml=1, spark=2, sql=2. Repartition ví dụ có 4 partition, coalesce có 2; hai API cho cùng tần suất.

## Lỗi dễ gặp và cách điều tra

Dùng accumulator làm bộ đếm giao dịch chính thức; đưa mọi dữ liệu về một partition; nghĩ lineage bảo vệ khi nguồn bị xóa.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thử broadcast một dictionary nhỏ trong RDD rồi viết lại lookup bằng join; giải thích vì sao DataFrame là lựa chọn chính cho bảng.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
