# Ngày 68 — Imputer scaler và vector đặc trưng

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Imputer scaler và vector đặc trưng”. Kết quả cần đạt: Vector ba chiều có dữ liệu hợp lệ, preprocessing chỉ fit train.

## Từ mới gắn với bài này

- **Imputer (bộ điền thiếu)**.
- **Scaling (chuẩn hóa thang đo)**.
- **VectorAssembler (bộ ghép cột thành vector)**.

## Tình huống và cách hiểu

**Imputer (bộ điền thiếu)** học quy tắc thay NULL/NaN trên train. **Scaling (chuẩn hóa thang đo)** giúp một số thuật toán không bị đơn vị tiền hàng trăm nghìn lấn các biến nhỏ. **VectorAssembler (bộ ghép cột thành vector)** cần đầu vào số phù hợp.

Chọn mean hay median có lý do. Recency thiếu do không có hoạt động không tự bằng vừa hoạt động hôm nay. Có thể thêm cờ thiếu nếu bạn định nghĩa và đánh giá; đừng tự đổi chính sách khi serving.

StandardScaler với withMean có thể làm vector thưa thành đặc, tăng bộ nhớ. Trong mẫu ba cột số nhỏ điều đó không đáng kể; với hàng triệu category cần cân nhắc. Tree model thường không cần scaling như model tuyến tính.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-068/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import Imputer, VectorAssembler, StandardScaler
train = spark_snapshot(spark)
pipeline = Pipeline(stages=[Imputer(inputCols=["recency_days"], outputCols=["recency_filled"]), VectorAssembler(inputCols=["events_30d", "spend_30d", "recency_filled"], outputCol="raw_features"), StandardScaler(inputCol="raw_features", outputCol="features", withMean=False)])
model = pipeline.fit(train)
model.transform(train).select("raw_features", "features").show(3, truncate=False)
```

## Đọc từng phần của ví dụ

Imputer tạo cột riêng, assembler ghép theo thứ tự, scaler học trên train. Giữ thứ tự feature như một phần contract.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Vector ba chiều có dữ liệu hợp lệ, preprocessing chỉ fit train.

## Ba câu kiểm tra hiểu bài

1. Imputer có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: bộ điền thiếu.
- Luồng chính: Imputer tạo cột riêng, assembler ghép theo thứ tự, scaler học trên train. Giữ thứ tự feature như một phần contract.
- Đối chiếu tiêu chí: Vector ba chiều có dữ liệu hợp lệ, preprocessing chỉ fit train. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 12 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
