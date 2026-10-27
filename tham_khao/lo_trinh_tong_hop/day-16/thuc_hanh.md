# Ngày 16 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-16/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Tạo `projects/02-mlops/churn/` với __init__.py, features.py, train.py, predict.py và cli.py. Tách logic đã làm thành hàm có tham số.
2. Viết CLI nhận --snapshot-date, --input và --output. Log cấu hình, không log dữ liệu nhạy cảm.
3. Tạo tests/ dưới project, dùng pytest và fixture Spark local[2] có stop trong teardown. Dùng tmp_path làm đích ghi thử.
4. Viết ít nhất 5 test: expected feature trên tiny, sự kiện tương lai bị loại, ingested_at muộn bị loại, khóa dimension trùng bị chặn, rerun không tăng số dòng.
5. Cố tình sửa biên `< cutoff` thành `<= cutoff` và thêm fixture đúng cutoff để chứng minh test thất bại; hoàn nguyên và chạy xanh.

## Cách chạy

```bash
python scripts/run_day.py 16
```

Lưu đầu ra tự tạo ở `artifacts/day-16/` bằng `output_dir(16)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Ví dụ thấy 1 khóa bị trùng. Bộ test dự án có ca biên đúng cutoff; kiểm thử âm thực sự bắt được lỗi cố ý. Lệnh chạy: python -m pytest projects/02-mlops/tests -q.

## Lỗi dễ gặp và cách điều tra

Chạy test trên dữ liệu cá nhân; để side effect lúc import; test so dòng chưa sắp xếp; bắt exception rồi tiếp tục ghi thành công.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thêm kiểm tra đọc ghi Parquet trong thư mục tạm và kiểm tra CLI trả mã lỗi khi thiếu ngày hợp lệ.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
