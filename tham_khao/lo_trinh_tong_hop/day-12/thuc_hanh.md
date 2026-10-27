# Ngày 12 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-12/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy ví dụ và phân loại từng stage là estimator hay transformer.
2. Thay train minh họa bằng snapshot train ngày 11; giữ validation và test độc lập. Đổi cột churn sang label kiểu double nếu cần.
3. Thêm Imputer cho recency, StringIndexer và OneHotEncoder cho plan/region, VectorAssembler và LogisticRegression. Chốt thứ tự các feature.
4. Fit chỉ train, transform validation; lưu PipelineModel vào artifacts/day-12/model. Viết phần load bằng PipelineModel.load và chạy ở tiến trình mới.
5. Thử category lạ trên bản sao fixture, kiểm tra không lỗi và lưu dự đoán trước/sau load để đối chiếu.

## Cách chạy

```bash
python scripts/run_day.py 12
```

Lưu đầu ra tự tạo ở `artifacts/day-12/` bằng `output_dir(12)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Có artifact pipeline, schema đầu vào, code train/load. Số dòng prediction bằng số dòng validation; xác suất từng lớp nằm trong [0,1] và tổng xấp xỉ 1. Không yêu cầu một điểm số đẹp trên dữ liệu giả lập.

## Lỗi dễ gặp và cách điều tra

Fit scaler trên toàn dữ liệu; chỉ lưu classifier; thiếu cột đầu vào khi load; nhầm transform với huấn luyện thêm.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thử một decision tree với cùng split và data contract; giải thích vì sao quy trình lưu và đánh giá vẫn cần giữ nguyên.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
