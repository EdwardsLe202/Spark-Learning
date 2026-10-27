# Ngày 18 — Lý thuyết: Đóng gói và dự đoán hàng loạt

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Tạo batch scoring có version, contract và cách chạy trong môi trường sạch.

## 1. Batch inference tạo dữ liệu có thể truy vết
**Batch inference (dự đoán theo lô)** lấy một tập feature rồi ghi prediction. **Online inference (dự đoán theo yêu cầu)** trả kết quả trong một request. Batch phù hợp danh sách chăm sóc khách hàng mỗi ngày; online phù hợp quyết định tương tác nhanh. Tần suất cần thiết, dữ liệu sẵn có và độ trễ quyết định cách chọn.

Prediction cần customer_id, snapshot_date, score, prediction, model_version, run_id và feature_version. Khi rerun, khóa còn cần chính sách version: thay bản cùng model/snapshot hay giữ lịch sử có khóa mở rộng. Không dùng append rồi trông chờ người đọc tự loại trùng.

## 2. Docker đóng gói môi trường
**Image (mẫu môi trường đóng gói)** chứa runtime và dependency. **Container (tiến trình chạy từ image)** là một lần thực thi. **Volume (vùng lưu trữ gắn bên ngoài container)** giữ dữ liệu khi container bị xóa. **Dockerfile (tệp mô tả cách tạo image)** nên cố định dependency; model có thể gắn ngoài để đổi version mà không sửa code.

Kiến trúc ARM của Apple Silicon khác x86_64. Build thành công trên Mac chưa chứng minh image hoạt động trên server kiến trúc khác. Đối với Spark job, `spark-submit` dùng môi trường có Java/Spark; model sklearn nhỏ có thể chạy bằng Python mà không cần JVM. Đừng load Spark model như thể nó là một file sklearn.

## 3. Phạm vi thực hành
Phần bắt buộc là batch scoring từ artifact đã lưu trong một tiến trình mới, có log và metadata. Dùng môi trường Python sạch trước; Docker là bước đóng gói tiếp theo nếu máy có Docker hoạt động. Không đưa secret, dữ liệu đầu vào lớn hoặc đường dẫn cá nhân vào image. Docker Compose (cấu hình nhiều container) hữu ích khi ghép API và MLflow, nhưng không cần khởi động tất cả dịch vụ để score một file.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
from pyspark.ml import PipelineModel
model_path = ROOT / "artifacts/day-12/model"
if not model_path.exists():
    raise FileNotFoundError("Hãy hoàn thành và lưu model ở ngày 12 trước.")
model = PipelineModel.load(str(model_path))
print("Đã load model Spark; cần feature có cùng schema và preprocessing.")
# TODO: đọc feature snapshot mới, transform, thêm metadata, ghi theo khóa đã chọn.
```

## Năm ý đối chiếu với lộ trình gốc

- 18.1 — Docker image, container, network, volume và kiến trúc ARM hoặc x86.
- 18.2 — Dockerfile, dependency cố định, model artifact và cấu hình ngoài image.
- 18.3 — spark submit, batch scoring và ghi prediction cùng entity, thời gian, model version.
- 18.4 — So sánh batch inference với online inference; tái sử dụng preprocessing.
- 18.5 — Docker Compose cho mô hình học tập; health check và lưu dữ liệu bền vững.

Các ý trên giữ phạm vi phần 18 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Image khác container thế nào?
2. Vì sao prediction cần model_version?
3. Batch rerun nên xử lý đầu ra thế nào?

## Đọc thêm từ nguồn chính thức

- [Docker get started](https://docs.docker.com/get-started/)
- [Spark submit](https://spark.apache.org/docs/3.5.7/submitting-applications.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
