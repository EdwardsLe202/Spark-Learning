# Ngày 88 — Model signature input example và dependency

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Model signature input example và dependency”. Kết quả cần đạt: Model sklearn load từ run URI và cho cùng score trong tolerance.

## Từ mới gắn với bài này

- **Model signature (mô tả kiểu đầu vào/đầu ra)**.
- **Input example (mẫu đầu vào)**.
- **Dependency environment (môi trường thư viện)**.

## Tình huống và cách hiểu

**Model signature (mô tả kiểu đầu vào/đầu ra)** giúp biết model nhận bảng gì. **Input example (mẫu đầu vào)** là ví dụ có thể dùng để thử. **Dependency environment (môi trường thư viện)** cần đủ phiên bản để load artifact.

Model đã lưu phải có preprocessing và tên flavor đúng. Nhánh sklearn không cần JVM; nhánh Spark thường cần Spark/Java. Không hứa chuyển đổi Spark model sang định dạng nhẹ luôn được hỗ trợ hoặc tương đương.

Ví dụ log sklearn pipeline cùng signature, sau đó load lại theo run URI. Lab thử thêm Spark flavor và đọc yêu cầu runtime. Kiểm tra fixture trước/sau log để không chỉ dựa vào việc thư mục model tồn tại.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-088/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import mlflow.sklearn
from mlflow.models import infer_signature
mlflow = setup_tracking()
model, train, val = fit_sklearn()
example = train[FEATURES].head(3)
with mlflow.start_run(run_name="model-contract") as run:
    mlflow.sklearn.log_model(model, artifact_path="model", signature=infer_signature(example, model.predict(example)), input_example=example)
    uri = "runs:/" + run.info.run_id + "/model"
    loaded = mlflow.sklearn.load_model(uri)
    assert np.allclose(model.predict_proba(example), loaded.predict_proba(example))
    print(uri)
```

## Đọc từng phần của ví dụ

Infer_signature dùng đầu vào thật và đầu ra đúng loại model.predict. Load theo run bất biến cho lần thí nghiệm này.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Model sklearn load từ run URI và cho cùng score trong tolerance.

## Ba câu kiểm tra hiểu bài

1. Model signature có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mô tả kiểu đầu vào/đầu ra.
- Luồng chính: Infer_signature dùng đầu vào thật và đầu ra đúng loại model.predict. Load theo run bất biến cho lần thí nghiệm này.
- Đối chiếu tiêu chí: Model sklearn load từ run URI và cho cùng score trong tolerance. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 15 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
