# Ngày 97 — Batch scoring Spark và prediction metadata

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Batch scoring Spark và prediction metadata”. Kết quả cần đạt: 120 prediction có metadata; code inference của bạn không gọi fit.

## Từ mới gắn với bài này

- **Batch inference (dự đoán theo lô)**.
- **Prediction key (khóa của bản dự đoán)**.

## Tình huống và cách hiểu

**Batch inference (dự đoán theo lô)** dùng model đã chốt cho tập feature mới. **Prediction key (khóa của bản dự đoán)** trong bài gồm customer_id, snapshot_date, model_version. Nếu muốn giữ nhiều lần chạy cùng model cần thêm run hoặc release theo policy.

Không fit lại preprocessing lúc score. Nhánh Spark dùng PipelineModel đã lưu ngày 72; nhánh sklearn dùng artifact riêng cho API. Score cần metadata để truy về nguồn, không chỉ một cột 0/1 không có mã khách.

CLI batch_spark.py load model và feature, kiểm tra trùng khóa rồi ghi đích riêng. Chạy lại cùng nguồn ghi thay đúng dataset của version/ngày, không append vô điều kiện.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-097/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from pyspark.ml.functions import vector_to_array
model = spark_ml_pipeline().fit(spark_snapshot(spark))
features = build_features_spark(spark, "2025-07-01", include_labels=False)
scored = model.transform(features).withColumn("score", vector_to_array("probability")[1]).withColumn("model_version", F.lit("spark-demo-v1"))
result = scored.select("customer_id", "snapshot_date", "score", "prediction", "model_version")
result.show(3)
assert result.count() == 120
```

## Đọc từng phần của ví dụ

Mẫu tự tạo model demo để minh họa; bài làm phải load artifact đã chọn, không train trong CLI inference.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

120 prediction có metadata; code inference của bạn không gọi fit.

## Ba câu kiểm tra hiểu bài

1. Batch inference có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: dự đoán theo lô.
- Luồng chính: Mẫu tự tạo model demo để minh họa; bài làm phải load artifact đã chọn, không train trong CLI inference.
- Đối chiếu tiêu chí: 120 prediction có metadata; code inference của bạn không gọi fit. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 18 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
