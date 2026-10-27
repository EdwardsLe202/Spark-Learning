# Ngày 28 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường `requirements-api.txt`; ngày 21 và 23 cần model sklearn đã lưu ở ngày 14.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-28/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy công cụ giả lập và thử job_id không đúng mẫu, trường thừa, job không tồn tại; ghi rõ loại lỗi.
2. Tạo dispatcher chỉ cho search_docs và get_job_status. Thử đề xuất công cụ delete_file và kiểm tra bị từ chối trước khi chạy.
3. Xây workflow cố định: xác định câu hỏi → truy xuất tài liệu được phép → lấy trạng thái nếu cần → trả lời có nguồn. Giữ request_id xuyên suốt.
4. Thêm loop mô phỏng tối đa 3 bước, tổng timeout và retry tối đa 1 với lỗi tạm thời. Test model đề xuất cùng công cụ mãi vẫn phải dừng.
5. So 10 tác vụ giữa workflow và loop: đúng đáp án, đúng công cụ, số bước, latency và lỗi quyền. Dùng kết quả để chọn cách đơn giản phù hợp.

## Cách chạy

```bash
python scripts/run_day.py 28
```

Lưu đầu ra tự tạo ở `artifacts/day-28/` bằng `output_dir(28)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

job-001 trả succeeded; công cụ lạ không được chạy; tham số lỗi bị chặn. Loop dừng không quá 3 bước kể cả đầu ra model lặp. Phân biệt đề xuất mô phỏng với tool call của model thật.

## Lỗi dễ gặp và cách điều tra

Dùng eval xử lý JSON; tin công cụ hoặc model tự cấp quyền; retry vô hạn; chỉ chấm đáp án cuối mà bỏ qua hành động sai.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Nối dispatcher vào adapter model thật, ghi tool schema và version; kiểm tra output sai schema và timeout vẫn không mở rộng quyền.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
