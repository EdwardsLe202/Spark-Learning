# Ngày 15 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường `requirements-ml.txt`; dùng artifact từ các ngày được nêu trong lab.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-15/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy ví dụ rồi xem UI với lệnh trong docs/CAI_DAT.md. Phân biệt run metadata với model artifact.
2. Chạy ít nhất 5 thí nghiệm nhỏ từ ngày 13–14, mỗi run log cấu hình, validation metric, thời gian, snapshot hash, code reference và schema. Không dùng metric bịa để đủ số run.
3. Dùng mlflow.sklearn.log_model với pipeline, signature và input_example. Đăng ký model dưới tên churn-sklearn, lưu version cụ thể.
4. Tạo alias candidate, load model theo version và kiểm tra cùng fixture như ngày 14. Giữ Spark model tên riêng nếu log thêm nhánh đó.
5. Viết một prediction metadata gồm customer_id, snapshot_date, model_version, run_id, data_hash và code_reference.

## Cách chạy

```bash
python scripts/run_day.py 15
```

Lưu đầu ra tự tạo ở `artifacts/day-15/` bằng `output_dir(15)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Có 5 training run thật trên cùng split để so sánh, ít nhất một model được lưu và load lại; từ model version tìm được run và snapshot hash.

## Lỗi dễ gặp và cách điều tra

Log đường dẫn thay vì snapshot; nhầm run_id với model version; dùng alias thay cho version bất biến trong log prediction; dựa hoàn toàn vào autolog.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Log thêm Spark PipelineModel bằng mlflow.spark; so yêu cầu Java/Spark khi load với artifact sklearn.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
