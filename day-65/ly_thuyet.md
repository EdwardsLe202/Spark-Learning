# Ngày 65 — Lắp pipeline scikit-learn

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Lắp pipeline scikit-learn”. Kết quả cần đạt: Có preprocess/classifier; score trong [0,1], không yêu cầu giá trị đẹp.

## Từ mới gắn với bài này

- **Preprocessing (tiền xử lý)**.
- **Pipeline (chuỗi bước fit và transform)**.
- **ColumnTransformer (xử lý các nhóm cột)**.

## Tình huống và cách hiểu

**Preprocessing (tiền xử lý)** biến dữ liệu thô thành đầu vào model: điền thiếu, chuẩn hóa số và mã hóa nhóm. **Pipeline (chuỗi bước fit và transform)** giữ các bước ấy cùng classifier. **ColumnTransformer (xử lý các nhóm cột)** tách cột số và cột phân loại.

Chỉ lưu classifier sẽ bỏ mất ý nghĩa vector đầu vào. Pipeline tham chiếu có SimpleImputer median, StandardScaler cho số, OneHotEncoder cho plan/region, rồi LogisticRegression. Mở hàm sklearn_pipeline để đọc đủ cấu hình; không coi helper như hộp không cần hiểu.

Hôm nay tập trung luồng đầu vào/đầu ra. Ngày sau kiểm tra fit chỉ train. Label không đi vào preprocessing và mã khách vẫn giữ bên ngoài để ghép prediction.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-065/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
pipeline = sklearn_pipeline()
train = snapshot_pd()
pipeline.fit(train[FEATURES], train.label)
print("Các bước:", list(pipeline.named_steps))
print("Ba score:", pipeline.predict_proba(train[FEATURES].head(3))[:, 1].tolist())
```

## Đọc từng phần của ví dụ

Pipeline fit cả preprocessing và classifier từ cùng tập train. Predict_proba lớp 1 là score churn.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có preprocess/classifier; score trong [0,1], không yêu cầu giá trị đẹp.

## Ba câu kiểm tra hiểu bài

1. Preprocessing có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tiền xử lý.
- Luồng chính: Pipeline fit cả preprocessing và classifier từ cùng tập train. Predict_proba lớp 1 là score churn.
- Đối chiếu tiêu chí: Có preprocess/classifier; score trong [0,1], không yêu cầu giá trị đẹp. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 14 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
