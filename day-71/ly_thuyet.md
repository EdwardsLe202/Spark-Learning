# Ngày 71 — Chọn thuật toán theo loại bài toán

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Chọn thuật toán theo loại bài toán”. Kết quả cần đạt: Có so sánh cùng split; phân biệt phân loại, hồi quy số và gom nhóm.

## Từ mới gắn với bài này

- **Decision tree (cây quyết định)**.
- **Regression (dự đoán số)**.
- **Clustering (gom nhóm không có nhãn)**.

## Tình huống và cách hiểu

**Decision tree (cây quyết định)** chia dữ liệu theo điều kiện feature để dự đoán. **Regression (dự đoán số)** dùng khi target là giá trị liên tục; **clustering (gom nhóm không có nhãn)** tìm cấu trúc, không tự đồng nghĩa các nhóm có ý nghĩa nghiệp vụ.

Không biến bài churn thành KMeans rồi so accuracy phân loại như cùng nhiệm vụ. MLlib hỗ trợ một tập thuật toán cụ thể; chọn theo target, tài nguyên, tính giải thích và cách phục vụ. Tree thường không cần scaling nhưng vẫn cần xử lý thiếu và mã hóa phù hợp.

Bài cốt lõi so cây nhỏ với logistic trên cùng split. Regression/KMeans là nhánh bổ sung để bạn nhận diện phạm vi, không cần tuning ba họ thuật toán trong một buổi.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-071/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
base = spark_ml_pipeline()
pipeline = Pipeline(stages=base.getStages()[:-1] + [DecisionTreeClassifier(maxDepth=2, seed=42)])
model = pipeline.fit(spark_snapshot(spark))
model.transform(spark_snapshot(spark, "2025-04-01")).select("label", "prediction").show(5)
```

## Đọc từng phần của ví dụ

Tái dùng đúng preprocessing, chỉ đổi classifier. Điều đó giúp so ảnh hưởng thuật toán thay vì đổi nhiều yếu tố cùng lúc.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có so sánh cùng split; phân biệt phân loại, hồi quy số và gom nhóm.

## Ba câu kiểm tra hiểu bài

1. Decision tree có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: cây quyết định.
- Luồng chính: Tái dùng đúng preprocessing, chỉ đổi classifier. Điều đó giúp so ảnh hưởng thuật toán thay vì đổi nhiều yếu tố cùng lúc.
- Đối chiếu tiêu chí: Có so sánh cùng split; phân biệt phân loại, hồi quy số và gom nhóm. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 12 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
