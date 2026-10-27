# Ngày 70 — Baseline Logistic Regression bằng Spark

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Baseline Logistic Regression bằng Spark”. Kết quả cần đạt: 120 prediction validation, không fit preprocessing trên validation.

## Từ mới gắn với bài này

- **Logistic regression (hồi quy logistic cho phân loại)**.
- **Probability (xác suất model ước lượng)**.

## Tình huống và cách hiểu

**Logistic regression (hồi quy logistic cho phân loại)** tạo score lớp từ tổ hợp feature. **Probability (xác suất model ước lượng)** không mặc định là xác suất đã được hiệu chỉnh hoàn hảo cho mọi nhóm dữ liệu.

Lắp các stage ngày 67–69 rồi classifier thành một Pipeline. Fit train cutoff 1/2, transform validation 1/4. Pipeline tham chiếu spark_ml_pipeline giúp chạy mẫu, nhưng bài làm cần tự lắp và giải thích thứ tự.

Giữ model Spark riêng với model sklearn. Hai runtime có thể dùng cùng schema nghiệp vụ nhưng không cùng artifact hay xác suất. Chưa dùng test để chọn regParam; bước lựa chọn tới các ngày sau.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-070/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
train, val = spark_snapshot(spark), spark_snapshot(spark, "2025-04-01")
pipeline = spark_ml_pipeline(reg_param=0.1)
model = pipeline.fit(train)
predicted = model.transform(val)
predicted.select("customer_id", "label", "probability", "prediction").show(5, truncate=False)
assert predicted.count() == 120
```

## Đọc từng phần của ví dụ

Fit học toàn pipeline trên train; transform tạo thêm probability/prediction và giữ đủ khách validation.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

120 prediction validation, không fit preprocessing trên validation.

## Ba câu kiểm tra hiểu bài

1. Logistic regression có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: hồi quy logistic cho phân loại.
- Luồng chính: Fit học toàn pipeline trên train; transform tạo thêm probability/prediction và giữ đủ khách validation.
- Đối chiếu tiêu chí: 120 prediction validation, không fit preprocessing trên validation. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 12 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
