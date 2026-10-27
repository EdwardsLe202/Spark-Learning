# Ngày 04 — Lý thuyết: DataFrame và Spark SQL căn bản

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Tạo schema, viết phép lọc bằng hai API và đối chiếu kết quả đã sắp xếp.

## 1. Một bảng cần hợp đồng về kiểu
**DataFrame (bảng dữ liệu có cấu trúc)** gồm các cột có tên và kiểu. **Schema (lược đồ dữ liệu)** ghi rõ các cột và kiểu ấy. `StructType` mô tả toàn bảng; `StructField` mô tả từng cột. Dữ liệu CSV bắt đầu là văn bản, nên đọc chuỗi rồi chuyển kiểu có kiểm tra giúp thấy rõ lỗi nguồn.

**Column expression (biểu thức cột)** mô tả phép tính cho các dòng. `F.col("amount") + 1000` không lấy từng số về Python mà tạo một phần kế hoạch. `select` chọn cột, `alias` đặt tên, `withColumn` tạo hoặc thay một cột. Các phép biến đổi tạo DataFrame mới; phải gán kết quả nếu muốn dùng tiếp.

## 2. Viết điều kiện đúng
**Type casting (chuyển kiểu dữ liệu)** dùng `cast`; khi parse sai, kết quả hoặc lỗi phụ thuộc cấu hình, chẳng hạn chế độ ANSI. Với bài học, kiểm tra riêng chuỗi sai kiểu thay vì mặc định chúng biến thành số 0. `when(...).otherwise(...)` tương tự CASE WHEN trong SQL.

Điều kiện kết hợp dùng `&`, `|`, `~` và đặt ngoặc cho từng vế. Toán tử `and` của Python không thay thế được điều kiện cột Spark. Chuỗi `"amount"` là tên, `F.col("amount")` là biểu thức, còn `1000` là giá trị Python được Spark đưa vào biểu thức.

## 3. SQL và DataFrame dùng cùng bộ máy
**Temporary view (bảng nhìn tạm)** đặt tên cho DataFrame trong phiên để truy vấn bằng `spark.sql`. SQL và DataFrame API có thể biểu đạt cùng phép biến đổi. Spark không bảo đảm thứ tự dòng khi chưa `orderBy`; so sánh hai kết quả theo khóa hoặc sắp xếp đủ cột trước khi kiểm tra. Chỉ `collect()` dữ liệu fixture nhỏ có giới hạn để đối chiếu.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
df = read_events(spark, "events_tiny.csv").withColumn("amount", F.col("amount").cast("long"))
result = df.filter(F.col("amount") >= 100000).select("event_id", "amount")
result.orderBy("event_id").show()
df.createOrReplaceTempView("events")
spark.sql("SELECT event_id, amount FROM events WHERE amount >= 100000 ORDER BY event_id").show()
```

## Năm ý đối chiếu với lộ trình gốc

- 04.1 — Tạo DataFrame, StructType, StructField; tên cột và kiểu dữ liệu.
- 04.2 — select, alias, filter, withColumn, drop và biểu thức Column.
- 04.3 — cast, when, otherwise, hàm số học; phân biệt biểu thức cột với giá trị Python.
- 04.4 — Temp view và spark.sql; dùng SQL quen thuộc để kiểm tra kết quả.
- 04.5 — show, count, schema, explain; thứ tự dòng chỉ được xác định khi có sắp xếp phù hợp.

Các ý trên giữ phạm vi phần 04 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Column khác một giá trị Python thế nào?
2. select và withColumn tạo gì?
3. Tại sao phải orderBy trước khi so sánh fixture?

## Đọc thêm từ nguồn chính thức

- [DataFrame quickstart](https://spark.apache.org/docs/3.5.7/api/python/getting_started/quickstart_df.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
