# Ngày 20 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường `requirements-ml.txt`; dùng artifact từ các ngày được nêu trong lab.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-20/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Lấy snapshot score ngày 18 làm current, chọn reference có cùng contract và lưu hash hai tập.
2. Tạo ba bản sao: spend nhân 3, region lạ, thiếu cột events_30d. Kiểm tra schema lỗi phải chặn score, hai trường hợp còn lại tạo cảnh báo phù hợp.
3. Tính tỷ lệ thiếu, tỷ lệ category lạ, trung bình/quantile feature và score theo region. Ghi ngưỡng minh họa, không gọi đó là ngưỡng chuẩn.
4. Giả lập nhãn đến sau 30 ngày, tính precision/recall trên đúng snapshot. Phân biệt kết luận trước và sau khi có nhãn.
5. Viết policy retrain: điều kiện mở điều tra, điều kiện train, chất lượng candidate cần đạt và trường hợp giữ model cũ. Thử một candidate kém và lưu lý do từ chối.

## Cách chạy

```bash
python scripts/run_day.py 20
```

Lưu đầu ra tự tạo ở `artifacts/day-20/` bằng `output_dir(20)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Ba tình huống tạo ba phản ứng có lý do; schema lỗi chặn pipeline. Báo cáo không khẳng định model kém khi chỉ thấy drift mà chưa có nhãn.

## Lỗi dễ gặp và cách điều tra

Auto-retrain theo mọi cảnh báo; trộn nhãn các snapshot; bỏ nhóm ít mẫu; tính metric trên nhãn chưa quan sát đủ.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Tạo biểu đồ phân bố reference/current, thêm lượng mẫu tối thiểu và thời gian duy trì cảnh báo trước khi mở sự cố.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
