# Ngày 14 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường `requirements-ml.txt`; dùng artifact từ các ngày được nêu trong lab.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-14/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Cài requirements-ml.txt. Xuất ba snapshot ngày 11 thành CSV nhỏ hoặc Parquet và đọc bằng pandas.
2. Trong bai_lam.py, ghép SimpleImputer, OneHotEncoder(handle_unknown="ignore"), ColumnTransformer và LogisticRegression thành sklearn Pipeline. Fit chỉ train.
3. Đánh giá validation bằng precision/recall và average_precision_score; ghi rõ đây là AP của sklearn, không mặc định bằng areaUnderPR của Spark.
4. Lưu pipeline bằng joblib vào artifacts/day-14/model.joblib, kèm input_example.json, feature_schema.json, model_metadata.json có code/data version. Load trong tiến trình mới và so xác suất.
5. Giữ ba feature số events_30d, spend_30d, recency_days và hai cột region, plan làm contract cho API ngày 21.

## Cách chạy

```bash
python scripts/run_day.py 14
```

Lưu đầu ra tự tạo ở `artifacts/day-14/` bằng `output_dir(14)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Có model.joblib của sklearn với đủ preprocessing, schema và ví dụ đầu vào. Inference không cần mở SparkSession. Chỉ load artifact do chính bạn tạo và tin cậy.

## Lỗi dễ gặp và cách điều tra

Cho rằng sklearn.fit tự phân tán; limit quá lớn nhưng quá nhiều cột vẫn hết RAM; lưu model rồi bỏ quên danh sách và thứ tự feature.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thiết kế xuất shard Parquet cho deep learning, ghi giới hạn số dòng mỗi shard và cách xử lý dataset lớn hơn RAM.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
