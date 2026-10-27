# Ngày 67 — Estimator và Transformer trong Spark ML

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Estimator và Transformer trong Spark ML”. Kết quả cần đạt: Có StringIndexer và StringIndexerModel, mapping không fit lại trên validation.

## Từ mới gắn với bài này

- **Estimator (thành phần cần fit)**.
- **Transformer (thành phần transform bảng)**.
- **Model (kết quả đã fit)**.

## Tình huống và cách hiểu

**Estimator (thành phần cần fit)** học từ DataFrame rồi tạo **model (kết quả đã fit)**. **Transformer (thành phần transform bảng)** biến đổi DataFrame; một model đã fit cũng là transformer. Tên fit/transform giống sklearn nhưng đây là API pyspark.ml.

VectorAssembler ghép cột mà không học thống kê. StringIndexer học danh mục nên cần fit; StringIndexerModel áp dụng danh mục đã học. Không gọi fit trên validation để mã của cùng một category thay ý nghĩa.

Fixture spark_snapshot chuẩn bị một bảng feature tham chiếu để ví dụ độc lập với bài làm trước. Lab phải dùng dataset bạn tạo ngày 60 sau khi đã kiểm tra đúng schema.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-067/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from pyspark.ml.feature import StringIndexer, VectorAssembler
train = spark_snapshot(spark)
estimator = StringIndexer(inputCol="plan", outputCol="plan_index", handleInvalid="keep")
model = estimator.fit(train)
model.transform(train).select("plan", "plan_index").show(5)
print(type(estimator).__name__, type(model).__name__)
```

## Đọc từng phần của ví dụ

StringIndexer là estimator, model trả về áp dụng một ánh xạ đã cố định. HandleInvalid keep dành ô cho giá trị mới.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có StringIndexer và StringIndexerModel, mapping không fit lại trên validation.

## Ba câu kiểm tra hiểu bài

1. Estimator có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: thành phần cần fit.
- Luồng chính: StringIndexer là estimator, model trả về áp dụng một ánh xạ đã cố định. HandleInvalid keep dành ô cho giá trị mới.
- Đối chiếu tiêu chí: Có StringIndexer và StringIndexerModel, mapping không fit lại trên validation. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 12 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
