# Ngày 43 — JDBC object storage và quyền truy cập

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “JDBC object storage và quyền truy cập”. Kết quả cần đạt: SQLite mẫu trả O001/100000. JDBC chỉ đánh dấu xong sau khi đọc được database thật, không chỉ in cấu hình.

## Từ mới gắn với bài này

- **JDBC — Java Database Connectivity (giao diện kết nối database)**.
- **Object storage (kho lưu đối tượng)**.
- **Secret (thông tin bí mật cần bảo vệ)**.

## Tình huống và cách hiểu

**JDBC — Java Database Connectivity (giao diện kết nối database)** cho Spark đọc/ghi hệ quản trị cần driver thích hợp. **Object storage (kho lưu đối tượng)** như lưu trữ S3 dùng khóa đối tượng, không hoạt động y hệt filesystem local. Đường dẫn trông đúng chưa chứng minh connector và quyền đúng.

**Secret (thông tin bí mật cần bảo vệ)** không để trong code, Git hoặc output log. Với fixture SQLite của Python, bạn luyện hợp đồng bảng và câu SQL local; để Spark đọc JDBC thật phải có JAR driver đúng loại. Không gọi sqlite3 của Python là Spark JDBC.

Lab có nhánh database local qua dịch vụ PostgreSQL kèm Compose ở services. Chỉ bật khi tới ngày này; cấp tài khoản chỉ đọc bảng nguồn, và dùng biến môi trường. Cloud thật là nhánh mở rộng có tài khoản và ngân sách riêng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-043/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import sqlite3
with sqlite3.connect(out / "source.db") as connection:
    connection.execute("CREATE TABLE IF NOT EXISTS orders (order_id TEXT PRIMARY KEY, amount INTEGER)")
    connection.execute("INSERT OR REPLACE INTO orders VALUES (?, ?)", ("O001", 100000))
    print(connection.execute("SELECT order_id, amount FROM orders").fetchall())
print("Đây là fixture database local; lab JDBC dùng connector riêng.")
```

## Đọc từng phần của ví dụ

Placeholder ? truyền dữ liệu vào SQL, không nối tùy ý thành câu lệnh. Fixture kiểm tra đầu vào database, chưa chạy Spark JDBC.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

SQLite mẫu trả O001/100000. JDBC chỉ đánh dấu xong sau khi đọc được database thật, không chỉ in cấu hình.

## Ba câu kiểm tra hiểu bài

1. JDBC — Java Database Connectivity có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: giao diện kết nối database.
- Luồng chính: Placeholder ? truyền dữ liệu vào SQL, không nối tùy ý thành câu lệnh. Fixture kiểm tra đầu vào database, chưa chạy Spark JDBC.
- Đối chiếu tiêu chí: SQLite mẫu trả O001/100000. JDBC chỉ đánh dấu xong sau khi đọc được database thật, không chỉ in cấu hình. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 07 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
