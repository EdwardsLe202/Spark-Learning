# Ngày 07 — Lý thuyết: Đọc ghi và tổ chức lưu trữ

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Ghi Parquet theo ngày và biết chính xác phạm vi overwrite.

## 1. Định dạng file ảnh hưởng cách đọc
**CSV — Comma-Separated Values (văn bản phân cách bằng dấu phẩy)** dễ xem nhưng cần parse kiểu, xử lý dấu phân cách và giá trị thiếu. JSON diễn tả cấu trúc lồng nhau nhưng thường tốn dung lượng và chi phí parse. Parquet lưu theo cột, giữ schema và hỗ trợ bỏ qua phần dữ liệu không cần. Lợi ích thực tế còn tùy kích thước, cách ghi và truy vấn.

**Partition pruning (bỏ qua thư mục phân vùng không liên quan)** dùng điều kiện như event_date để giảm dữ liệu đọc. **Predicate pushdown (đẩy điều kiện lọc xuống bộ đọc)** giúp bộ đọc bỏ qua một số phần dữ liệu. Chúng là hai cơ chế khác nhau; xem plan thay vì chỉ suy từ thời gian chạy.

## 2. Ghi dữ liệu là một thay đổi trạng thái
**Append (ghi thêm)** phù hợp khi bảo đảm dữ liệu mới chưa có; chạy lại có thể tạo trùng. **Overwrite (ghi thay thế)** có thể thay cả đích đang trỏ tới. **Error if exists (báo lỗi nếu tồn tại)** giúp tránh ghi đè ngoài ý muốn; ignore giữ đích cũ. Trong lab, mọi đích nằm dưới artifacts của ngày, tuyệt đối không dùng đường dẫn nguồn làm đích.

Phân vùng thư mục theo ngày thường có ích khi đọc theo khoảng ngày. Phân vùng theo customer_id với rất nhiều khóa dễ tạo **small files (nhiều file nhỏ)** và quá nhiều thư mục. Không có con số partition đúng cho mọi máy.

## 3. File khác bảng
**Catalog (danh mục quản lý bảng)** giữ tên bảng và metadata. **Data lake (kho dữ liệu trên lưu trữ dạng file hoặc đối tượng)** chưa tự có transaction chỉ vì dùng Parquet. Delta Lake hoặc Apache Iceberg bổ sung quản lý bảng và giao dịch theo khả năng từng hệ thống. **JDBC (giao diện kết nối cơ sở dữ liệu cho Java)** và **object storage (lưu trữ đối tượng)** cần connector, quyền và cấu hình phù hợp; ngày này tập trung file local để giữ phần bắt buộc gọn.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
df = read_events(spark, "events_tiny.csv").withColumn("event_date", F.to_date(F.to_timestamp("event_time")))
out = output_dir(7) / "by_date"
df.write.mode("overwrite").partitionBy("event_date").parquet(str(out))
selected = spark.read.parquet(str(out)).filter("event_date = DATE '2025-01-20'")
selected.explain("formatted")
selected.show()
```

## Năm ý đối chiếu với lộ trình gốc

- 07.1 — CSV, JSON, Parquet; schema rõ ràng và chi phí đọc theo cột.
- 07.2 — Chế độ append, overwrite, error và ignore; kiểm tra đích trước khi ghi.
- 07.3 — Partition theo thư mục, partition pruning và predicate pushdown.
- 07.4 — JDBC, object storage, data lake; quyền truy cập và quản lý thông tin kết nối.
- 07.5 — Catalog, metadata, bảng và giới thiệu Delta Lake hoặc Iceberg cho transaction và lịch sử.

Các ý trên giữ phạm vi phần 07 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Pruning khác pushdown thế nào?
2. Vì sao Parquet không tự là bảng có transaction?
3. Vì sao tránh partition theo khóa có hàng triệu giá trị?

## Đọc thêm từ nguồn chính thức

- [Parquet data source](https://spark.apache.org/docs/3.5.7/sql-data-sources-parquet.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
