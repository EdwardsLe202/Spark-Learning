# Ngày 18 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường `requirements-ml.txt`; dùng artifact từ các ngày được nêu trong lab.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-18/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Tạo feature cutoff 2025-07-01 bằng hàm ngày 11. Batch score bằng model ngày 12; không fit lại preprocessing.
2. Ghi score lớp 1 và metadata; chọn khóa (customer_id, snapshot_date, model_version). Chạy lại cùng đầu vào và đối chiếu số dòng.
3. Viết predict CLI chạy được trong terminal mới bằng đường dẫn model và feature tường minh.
4. Với Docker, bắt đầu nhánh sklearn nhẹ: cài requirements-ml.txt, gắn model và input bằng volume, chạy predict CLI. Ghi cách build, run và kiến trúc máy. Nếu chưa có Docker, thực hiện venv sạch và ghi giới hạn kiểm chứng.
5. Viết bảng dữ liệu nào nằm trong image, container và volume; thử xóa container thử rồi đọc lại volume.

## Cách chạy

```bash
python scripts/run_day.py 18
```

Lưu đầu ra tự tạo ở `artifacts/day-18/` bằng `output_dir(18)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

120 prediction cho snapshot 2025-07-01, không trùng khóa khi rerun; có version model cụ thể. Code load không thực hiện train. Có bằng chứng clean run và phạm vi đã thử.

## Lỗi dễ gặp và cách điều tra

Artifact chỉ tồn tại trên notebook; quên volume làm mất file; dùng alias động mà không ghi resolved version; image ARM được coi là kiểm chứng x86.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Đóng gói Spark job có Java 17 và spark-submit; so chi phí khởi động với batch sklearn nhỏ. Không thay runtime của model khi chưa kiểm tra tương đương.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
