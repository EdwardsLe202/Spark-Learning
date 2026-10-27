# Ngày 09 — Lý thuyết: Tối ưu và xử lý lỗi hiệu năng

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Đo baseline, thay một yếu tố và chứng minh đầu ra không đổi.

## 1. Tối ưu bắt đầu bằng phép đo
**Baseline (mốc so sánh ban đầu)** gồm code, dữ liệu, cấu hình và kết quả. Đo một action thực sự chạy phép tính; chỉ đo thời gian tạo DataFrame thường đo kế hoạch. **Logical plan (kế hoạch logic)** diễn tả tính toán; **physical plan (kế hoạch vật lý)** chọn cách làm cụ thể. AQE có thể điều chỉnh sau khi biết thống kê lúc chạy.

**Broadcast join (ghép bằng phát bảng nhỏ tới nơi xử lý)** có thể tránh shuffle bảng lớn khi điều kiện phù hợp. **Sort-merge join (ghép bằng sắp xếp rồi trộn)** thường trao đổi và sắp xếp theo khóa. Broadcast chỉ hợp lý nếu phía được phát đủ nhỏ với bộ nhớ; tự gợi ý broadcast không làm một bảng lớn trở nên nhỏ.

## 2. Nhận diện lệch và thiếu bộ nhớ
**Data skew (phân bố dữ liệu lệch khóa)** khiến một task nhận quá nhiều dòng dù số partition lớn. **Spill (tràn dữ liệu tạm ra đĩa)** cho thấy dữ liệu xử lý không giữ hết trong phần bộ nhớ được dùng. **Out-of-memory — OOM (hết bộ nhớ)** có thể ở driver hoặc phía thực thi; collect/toPandas lớn thường đẩy rủi ro về driver.

**Cache (giữ kết quả để tái sử dụng)** chỉ hữu ích nếu kết quả được dùng lại và lợi ích vượt chi phí lưu. Cache là lazy; một action mới vật hóa dữ liệu. `unpersist()` giải phóng sau khi dùng. Đừng so lần chạy lạnh với lần chạy nóng rồi quy mọi khác biệt cho thay đổi code.

## 3. Giảm chi phí không cần thiết
**Built-in function (hàm có sẵn trong Spark)** giúp bộ máy hiểu biểu thức. **Python UDF — User-Defined Function (hàm do người dùng viết bằng Python)** có thể thêm chi phí trao đổi giữa Python và JVM. Pandas UDF dùng lô qua Arrow nhưng vẫn có chi phí và điều kiện kiểu. Tối ưu cần giữ nguyên ý nghĩa, schema và kết quả; nhanh mà sai không đạt yêu cầu.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
from time import perf_counter
df = spark.range(100000).withColumn("key", F.when(F.col("id") < 90000, 0).otherwise(F.col("id") % 10))
t0 = perf_counter()
summary = df.groupBy("key").count()
rows = summary.orderBy("key").collect()  # Chỉ có tối đa 10 dòng.
print("seconds:", round(perf_counter() - t0, 3))
print(rows)
summary.explain("formatted")
```

## Năm ý đối chiếu với lộ trình gốc

- 09.1 — explain, logical plan, physical plan; vai trò tối ưu truy vấn và AQE.
- 09.2 — Broadcast join, sort merge join; kích thước dữ liệu và điều kiện lựa chọn.
- 09.3 — Data skew, task chậm, spill và lỗi thiếu bộ nhớ ở driver hoặc executor.
- 09.4 — cache, persist, unpersist; chọn điểm tái sử dụng và đo lợi ích.
- 09.5 — Small files, số partition, built in function, Python UDF, pandas UDF và Arrow.

Các ý trên giữ phạm vi phần 09 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Cache một lần dùng có thể tốn hơn thế nào?
2. Nhiều partition có chữa khóa bị skew không?
3. Cần kiểm tra gì ngoài runtime?

## Đọc thêm từ nguồn chính thức

- [Spark SQL performance tuning](https://spark.apache.org/docs/3.5.7/sql-performance-tuning.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
