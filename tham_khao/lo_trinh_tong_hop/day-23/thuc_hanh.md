# Ngày 23 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Môi trường `requirements-api.txt`; ngày 21 và 23 cần model sklearn đã lưu ở ngày 14.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-23/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Mở API ngày 21 ở terminal riêng. Chọn SLO lab, warm up 10 request rồi gửi ít nhất 100 request cho mỗi concurrency 1, 2, 4.
2. Lưu latency/status của mọi request; tính p50, p95, lỗi và throughput = tổng request / tổng wall time. Nêu cách xử lý timeout trong báo cáo.
3. Chỉ đổi một yếu tố như số worker; chạy lại cùng input, kiểm tra prediction không đổi và ghi RAM quan sát được.
4. Thực hiện rollback model theo manifest ngày 19, kiểm tra readiness và version trong response.
5. Hoàn thành `projects/02-mlops/README.md`: test, MLflow, batch, API, monitoring, load test và phạm vi Docker/Airflow/cloud đã thực sự làm.

## Cách chạy

```bash
python scripts/run_day.py 23
```

Lưu đầu ra tự tạo ở `artifacts/day-23/` bằng `output_dir(23)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Bảng tải ba mức concurrency, số mẫu, tỷ lệ lỗi và p95 có cấu hình đo; score khớp fixture; demo rollback về version cũ. Không đặt một con số latency chung cho mọi máy.

## Lỗi dễ gặp và cách điều tra

Chỉ đo request thành công; đếm tổng latency thay wall time để tính throughput; tăng worker vượt RAM; so model sau thay đổi mà không ghi version.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thêm giới hạn hàng đợi hoặc batch endpoint; kiểm tra quá tải trả lỗi có kiểm soát và không làm tiến trình chết.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
