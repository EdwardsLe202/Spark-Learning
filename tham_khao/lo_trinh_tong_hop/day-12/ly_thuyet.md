# Ngày 12 — Lý thuyết: Pipeline Machine Learning với Spark

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Fit trên train, lưu toàn pipeline và dự đoán lại sau khi load.

## 1. Mỗi thành phần làm việc khác nhau
**Estimator (thành phần cần học từ dữ liệu)** có `fit`, tạo ra **Model (mô hình đã học)**. **Transformer (thành phần biến đổi bảng)** có `transform`; một model đã fit cũng là transformer. **Pipeline (chuỗi thành phần xử lý)** có thể gồm nhiều estimator và transformer; `fit(train)` tạo **PipelineModel (pipeline đã học)**.

Ví dụ: **Imputer (bộ điền dữ liệu thiếu)** học giá trị thay thế, **StringIndexer (bộ ánh xạ nhóm sang chỉ số)** học các nhóm, **OneHotEncoder (bộ mã hóa nhóm thành vector chỉ báo)** biểu diễn nhóm, **VectorAssembler (bộ ghép các cột thành vector)** tạo cột features. **Logistic regression (hồi quy logistic)** học xác suất một lớp theo đặc trưng. Chỉ VectorAssembler không cần học thống kê từ dữ liệu.

## 2. Giữ cùng ý nghĩa đầu vào
**Categorical feature (đặc trưng phân loại)** như plan cần mã hóa; mã số 0, 1 không tự biểu thị khoảng cách có ý nghĩa. Cần xử lý **unseen category (giá trị nhóm chưa từng gặp)** bằng cấu hình phù hợp, chẳng hạn StringIndexer handleInvalid="keep". **Sparse vector (vector thưa)** lưu các phần tử khác 0 để tiết kiệm bộ nhớ; **dense vector (vector đặc)** lưu mọi phần tử.

**Scaling (chuẩn hóa thang đo)** thường giúp thuật toán nhạy với thang đo. Không phải mọi tree model đều cần scaling. Nếu recency thiếu, chốt cách điền trước khi ghép vector và giữ quy tắc này trong pipeline. Không fit lại encoder trên validation vì cùng số vector có thể mang ý nghĩa khác.

## 3. Lưu đủ để dùng lại
Lưu classifier riêng sẽ bỏ mất bước tạo đầu vào. Lưu toàn PipelineModel, danh sách cột, kiểu dữ liệu và phiên bản thư viện. `save` của Spark tạo thư mục artifact, không phải một file pickle nhỏ. Sau khi load, so xác suất trên fixture cố định trong sai số số học, không chỉ so nhãn 0/1. Bài này dùng pyspark.ml, API dựa trên DataFrame của MLlib.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
train = spark.createDataFrame([(1.0,0.0),(2.0,0.0),(3.0,1.0),(4.0,1.0)], "events_30d double, label double")
pipeline = Pipeline(stages=[VectorAssembler(inputCols=["events_30d"], outputCol="features"), LogisticRegression(maxIter=10)])
model = pipeline.fit(train)
model.transform(train).select("events_30d", "probability", "prediction").show(truncate=False)
# Đây chỉ là dữ liệu minh họa API; chưa phải model churn của dự án.
```

## Năm ý đối chiếu với lộ trình gốc

- 12.1 — Phân biệt Estimator, Transformer, Model và Pipeline trong pyspark.ml.
- 12.2 — Imputer, StringIndexer, OneHotEncoder, VectorAssembler và xử lý category chưa gặp.
- 12.3 — Scaling khi phù hợp thuật toán; vector đặc trưng thưa và đặc.
- 12.4 — Logistic regression, tree model, regression và clustering ở mức ứng dụng.
- 12.5 — fit, transform, save, load; giữ nhất quán tên cột, schema và preprocessing.

Các ý trên giữ phạm vi phần 12 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Fit trả về gì?
2. Vì sao lưu encoder cùng classifier?
3. Category mới cần chính sách gì?

## Đọc thêm từ nguồn chính thức

- [Spark ML pipelines](https://spark.apache.org/docs/3.5.7/ml-pipeline.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
