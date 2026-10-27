# Ngày 44 — Delta Lake transaction và time travel

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Delta Lake transaction và time travel”. Kết quả cần đạt: Hiện tại 7 dòng, version trước delete 8 dòng; có history thực tế.

## Từ mới gắn với bài này

- **ACID transaction (giao dịch bảo đảm tính nhất quán)**.
- **Time travel (đọc phiên bản dữ liệu cũ)**.

## Tình huống và cách hiểu

Parquet không tự quản lý phiên bản bảng. Delta Lake thêm transaction log để theo dõi trạng thái và thao tác bảng. **ACID transaction (giao dịch bảo đảm tính nhất quán)** là tập thuộc tính hệ quản lý bảng cung cấp theo thiết kế; không có nghĩa mọi hệ thống ngoài cùng tham gia giao dịch ấy.

**Time travel (đọc phiên bản dữ liệu cũ)** dùng versionAsOf để đọc trạng thái trước thay đổi. Khả năng đọc lại còn phụ thuộc file lịch sử vẫn được giữ; xóa dữ liệu cũ có thể làm mất khả năng quay về. Đừng dùng time travel thay mọi chính sách backup.

Repo chọn Delta 3.3.2 cho Spark 3.5.x. Cài requirements-delta và chạy riêng session Delta; lần đầu có thể tải JAR. Không dùng connector latest tùy ý với Spark cố định.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-044/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
target = out / "orders_delta"
orders.write.format("delta").mode("overwrite").save(str(target))
from delta.tables import DeltaTable
table = DeltaTable.forPath(spark, str(target))
version = table.history(1).select("version").first()[0]
table.delete("order_id = 'O004'")
print("Hiện tại:", spark.read.format("delta").load(str(target)).count())
print("Trước xóa:", spark.read.format("delta").option("versionAsOf", version).load(str(target)).count())
```

## Đọc từng phần của ví dụ

History lấy version cụ thể ngay trước delete. Giữ đường dẫn riêng của ngày để không đụng nguồn hoặc bảng ngày khác.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Hiện tại 7 dòng, version trước delete 8 dòng; có history thực tế.

## Ba câu kiểm tra hiểu bài

1. ACID transaction có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: giao dịch bảo đảm tính nhất quán.
- Luồng chính: History lấy version cụ thể ngay trước delete. Giữ đường dẫn riêng của ngày để không đụng nguồn hoặc bảng ngày khác.
- Đối chiếu tiêu chí: Hiện tại 7 dòng, version trước delete 8 dòng; có history thực tế. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 07 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
