# Ngày 69 — Category chưa gặp và one-hot encoding

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Category chưa gặp và one-hot encoding”. Kết quả cần đạt: Category mới được transform theo keep, không tự học lại mapping.

## Từ mới gắn với bài này

- **Unseen category (giá trị nhóm chưa gặp)**.
- **One-hot encoding (mã hóa nhóm bằng vector chỉ báo)**.
- **Sparse vector (vector thưa)**.

## Tình huống và cách hiểu

**Unseen category (giá trị nhóm chưa gặp)** xuất hiện khi plan mới hoặc vùng mới tới sau training. Pipeline cần quyết định giữ nhóm unknown hay báo lỗi hợp đồng. Đừng fit lại indexer trên request mới.

**One-hot encoding (mã hóa nhóm bằng vector chỉ báo)** tránh ngụ ý rằng mã 2 có khoảng cách gấp đôi mã 1. **Sparse vector (vector thưa)** tiết kiệm bằng cách chỉ giữ phần khác 0. Số chiều phụ thuộc danh mục và cấu hình encoder, không đoán cố định từ vài dòng show.

Bài dùng handleInvalid keep ở indexer. Bản ghi mới đi qua cùng pipeline đã học; kiểm tra thành công chưa chứng minh model dự đoán tốt cho nhóm chưa gặp. Cần metric theo nhóm và theo dõi tỷ lệ unknown.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-069/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder
train = spark_snapshot(spark)
pipeline = Pipeline(stages=[StringIndexer(inputCol="plan", outputCol="idx", handleInvalid="keep"), OneHotEncoder(inputCol="idx", outputCol="encoded")])
model = pipeline.fit(train)
new = train.limit(1).withColumn("plan", F.lit("new_plan"))
model.transform(new).select("plan", "idx", "encoded").show(truncate=False)
```

## Đọc từng phần của ví dụ

Không có fit ở dòng dự đoán. New_plan dùng nhóm dự phòng theo cấu hình đã chọn.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Category mới được transform theo keep, không tự học lại mapping.

## Ba câu kiểm tra hiểu bài

1. Unseen category có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: giá trị nhóm chưa gặp.
- Luồng chính: Không có fit ở dòng dự đoán. New_plan dùng nhóm dự phòng theo cấu hình đã chọn.
- Đối chiếu tiêu chí: Category mới được transform theo keep, không tự học lại mapping. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 12 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
