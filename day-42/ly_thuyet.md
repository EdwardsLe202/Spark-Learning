# Ngày 42 — Partition pruning predicate pushdown và catalog

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Partition pruning predicate pushdown và catalog”. Kết quả cần đạt: Ngày 2025-01-03 có 2 đơn; chỉ nhận xét cơ chế xuất hiện trong plan.

## Từ mới gắn với bài này

- **Partition pruning (bỏ qua thư mục phân vùng)**.
- **Predicate pushdown (đẩy điều kiện xuống bộ đọc)**.
- **Catalog (danh mục quản lý bảng)**.

## Tình huống và cách hiểu

**Partition pruning (bỏ qua thư mục phân vùng)** dùng điều kiện trên cột phân vùng để tránh đọc thư mục không liên quan. **Predicate pushdown (đẩy điều kiện xuống bộ đọc)** có thể bỏ qua một phần dữ liệu bên trong file. Đó là hai cơ chế khác nhau.

Ghi Parquet partitionBy order_date để đọc theo ngày, rồi tìm PartitionFilters trong plan. Tránh dùng cột có hàng triệu giá trị làm thư mục chỉ vì nó là khóa. File ít mà quá nhỏ vẫn có chi phí.

**Catalog (danh mục quản lý bảng)** giữ tên, schema và metadata; một temp view chưa phải catalog bền vững có quản lý lịch sử. Parquet chỉ là định dạng file, chưa tự cung cấp transaction hay upsert toàn bảng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-042/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
target = out / "by_date"
orders.write.mode("overwrite").partitionBy("order_date").parquet(str(target))
result = spark.read.parquet(str(target)).filter(F.col("order_date") == F.lit("2025-01-03").cast("date"))
result.explain("formatted")
print("Ngày 3:", result.count())
```

## Đọc từng phần của ví dụ

Ngày phân vùng có thể được suy luận lại thành date khi đọc Parquet. Điều kiện có kiểu tương thích.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ngày 2025-01-03 có 2 đơn; chỉ nhận xét cơ chế xuất hiện trong plan.

## Ba câu kiểm tra hiểu bài

1. Partition pruning có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: bỏ qua thư mục phân vùng.
- Luồng chính: Ngày phân vùng có thể được suy luận lại thành date khi đọc Parquet. Điều kiện có kiểu tương thích.
- Đối chiếu tiêu chí: Ngày 2025-01-03 có 2 đơn; chỉ nhận xét cơ chế xuất hiện trong plan. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 07 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).

## Chế độ ghi và tên bảng

**Append (ghi thêm)** có thể gây trùng khi rerun; **overwrite (ghi thay)** thay đúng phạm vi đích; **errorifexists (báo lỗi khi đã có đích)** giúp tránh ghi đè; **ignore (bỏ qua khi đích đã tồn tại)** không cập nhật kết quả. Thử bốn mode ở đích riêng rồi đọc lại, không thử trên nguồn.

Catalog quản lý tên/metadata; `spark.catalog.listTables()` cho xem bảng trong phiên/catalog đang dùng. Delta và Apache Iceberg là hai hướng định dạng bảng có quản lý; khóa chọn Delta để thực hành sâu, không cài mọi connector cùng lúc.
