# Ngày 15 — Lý thuyết: Theo dõi thí nghiệm và quản lý mô hình

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Truy ngược một model tới run, code và snapshot dữ liệu bằng MLflow.

## 1. Ghi lại đủ để trả lời “kết quả từ đâu?”
**Experiment tracking (theo dõi thí nghiệm)** ghi cấu hình và kết quả mỗi lần chạy. Trong MLflow, **experiment (nhóm thí nghiệm)** chứa các **run (lần thực thi)**. **Parameter (tham số cấu hình)** như regParam khác **metric (chỉ số đo)** như recall. **Tag (nhãn metadata)** ghi thông tin như commit hoặc data version; **artifact (tệp đầu ra cần lưu)** có thể là model, schema, biểu đồ hoặc báo cáo.

Chỉ log đường dẫn CSV không bảo đảm tái lập, vì nội dung ở đường dẫn đó có thể đổi. Repo cung cấp manifest với **SHA-256 (hàm băm định danh nội dung)**; giữ thêm bản snapshot bất biến hoặc quy trình tạo dữ liệu. Một hash giúp kiểm chứng nhưng không tự khôi phục nội dung đã mất.

## 2. Lưu model kèm hợp đồng
**Model signature (mô tả kiểu đầu vào và đầu ra)** và **input example (ví dụ đầu vào)** giúp người khác biết cách gọi model. Log thủ công các thông tin quan trọng trước khi dùng **autologging (ghi thí nghiệm tự động)**, vì tự động không biết hết định nghĩa nhãn hay quy tắc dữ liệu của bạn.

**Model registry (sổ quản lý model)** lưu các **model version (phiên bản mô hình)**. **Alias (bí danh trỏ tới một phiên bản)** như candidate hoặc champion giúp ứng dụng chọn model, nhưng có thể đổi nên prediction cần lưu version cụ thể đã dùng. Thay alias là quyết định phát hành, không phải phép màu kiểm định chất lượng.

## 3. Nơi lưu metadata và tệp
**Backend store (kho metadata thí nghiệm)** có thể là SQLite trong lab; **artifact store (kho tệp đầu ra)** giữ file. Repo cố định MLflow 2.22.0 để ví dụ có hành vi rõ; dùng URI SQLite tường minh thay vì phụ thuộc mặc định giữa các phiên bản. Chạy UI local để so sánh; không cần mở server ra mạng.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
import mlflow
from spark_lab import ROOT, output_dir
store = ROOT / "artifacts" / "mlflow.db"
store.parent.mkdir(exist_ok=True)
mlflow.set_tracking_uri("sqlite:///" + str(store))
mlflow.set_experiment("spark-learning-churn")
with mlflow.start_run(run_name="metadata-demo") as run:
    mlflow.log_param("seed", 42)
    mlflow.set_tag("data_manifest", "data/raw/manifest.json")
    mlflow.log_artifact(str(ROOT / "data/raw/manifest.json"))
    print("run_id:", run.info.run_id)
```

## Năm ý đối chiếu với lộ trình gốc

- 15.1 — MLflow experiment, run, parameter, metric, tag và artifact.
- 15.2 — Ghi thông tin pipeline Spark và mô hình từ thư viện khác; hiểu giới hạn autolog.
- 15.3 — Lưu model signature, input example, dependency và metadata dữ liệu.
- 15.4 — Registry, version, alias; chọn model candidate theo điều kiện đánh giá.
- 15.5 — Backend store, artifact store, local server và nguyên tắc quản lý quyền truy cập.

Các ý trên giữ phạm vi phần 15 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Backend store khác artifact store thế nào?
2. Hash có tự tái tạo file không?
3. Vì sao prediction ghi version thay vì chỉ alias?

## Đọc thêm từ nguồn chính thức

- [MLflow 2.22 tracking](https://mlflow.org/docs/2.22.0/tracking/)
- [MLflow model registry](https://mlflow.org/docs/2.22.0/model-registry.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
