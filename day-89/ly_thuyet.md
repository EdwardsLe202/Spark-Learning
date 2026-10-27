# Ngày 89 — Registry version và alias

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Registry version và alias”. Kết quả cần đạt: Truy từ version về run; phân biệt candidate alias với version bất biến.

## Từ mới gắn với bài này

- **Model registry (sổ quản lý model)**.
- **Version (phiên bản cụ thể)**.
- **Alias (bí danh có thể đổi)**.

## Tình huống và cách hiểu

**Model registry (sổ quản lý model)** liên kết model với run và metadata. **Version (phiên bản cụ thể)** là định danh cần ghi vào prediction. **Alias (bí danh có thể đổi)** như candidate giúp chọn phiên bản nhưng không là bằng chứng đã đạt chất lượng.

Promote alias là một quyết định có gate. Nếu cùng tên champion trỏ version khác theo thời gian, log chỉ alias sẽ không đủ tái tạo dự đoán cũ. Luôn resolve và lưu version thực đã dùng.

Mẫu đăng ký model demo và gán candidate trong registry local. Không thay một hệ thống production thật. Lab load theo version và truy ngược về training run, rồi thiết kế điều kiện phát hành.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-089/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import mlflow.sklearn
from mlflow import MlflowClient
mlflow = setup_tracking()
model, train, val = fit_sklearn()
with mlflow.start_run() as run:
    mlflow.sklearn.log_model(model, artifact_path="model")
    version = mlflow.register_model("runs:/" + run.info.run_id + "/model", "course-churn-sklearn")
client = MlflowClient()
client.set_registered_model_alias("course-churn-sklearn", "candidate", version.version)
print({"version": version.version, "run_id": version.run_id})
```

## Đọc từng phần của ví dụ

Version số do registry trả, không tự giả định luôn 1. Alias có thể đổi khi bạn chạy lại mẫu.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Truy từ version về run; phân biệt candidate alias với version bất biến.

## Ba câu kiểm tra hiểu bài

1. Model registry có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: sổ quản lý model.
- Luồng chính: Version số do registry trả, không tự giả định luôn 1. Alias có thể đổi khi bạn chạy lại mẫu.
- Đối chiếu tiêu chí: Truy từ version về run; phân biệt candidate alias với version bất biến. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 15 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
