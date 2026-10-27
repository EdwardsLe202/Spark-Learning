# Ngày 05 — Tên cột và kiểu dữ liệu

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Đọc printSchema và hiểu vì sao số tiền cần kiểu số.

## 1. Tên cột chưa đủ mô tả dữ liệu

**Schema (lược đồ tên cột và kiểu)** giống nhãn hướng dẫn của bảng: order_id là văn bản, amount là số. **String (kiểu chuỗi văn bản)** lưu mã như O001; **long (kiểu số nguyên 64 bit)** dùng cho số tiền nguyên trong bài. Mã có chữ và số vẫn là mã, không phải số để cộng.

Hôm qua Spark tự đoán kiểu từ list Python. Hôm nay bạn ghi rõ schema bằng chuỗi `order_id string, customer_id string, amount long`. Cách này nói trước cấu trúc mong muốn. Nó không tự sửa mọi giá trị sai; Python string "100000" và số 100000 khác nhau khi tạo DataFrame với schema số tường minh.

## 2. Đọc kết quả printSchema

`printSchema()` in tên và kiểu của từng cột. `nullable = true` nói cột cho phép biểu diễn giá trị thiếu, không có nghĩa mọi dòng hiện tại đều thiếu. Ta học cách xử lý thiếu ở ngày 11.

`orders.columns` là danh sách tên cột, dùng để kiểm tra bạn gõ đúng tên. `amount` và `Amount` có thể chịu ảnh hưởng cấu hình phân biệt hoa thường; trong khóa học hãy dùng chính xác tên mẫu, không dựa vào sự tự sửa của hệ thống.

## 3. Giữ bài toán nhỏ

Bài này chưa cần tự khai báo StructType hay học mọi kiểu Spark. Bạn chỉ cần đọc được ba tên cột và kiểu của chúng. Về sau có ngày, số thập phân và dữ liệu lồng nhau; mỗi phần được thêm khi dùng tới.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file.

```python
orders = spark.createDataFrame(
    [("O001", "C001", 100000), ("O002", "C001", 200000), ("O003", "C002", 50000)],
    "order_id string, customer_id string, amount long",
)
orders.printSchema()
print("Tên cột:", orders.columns)
```

## Đọc từng phần của ví dụ

- Tham số schema dạng chuỗi nằm sau dữ liệu, chỉ rõ ba kiểu theo thứ tự.
- printSchema hiển thị cấu trúc; không phải dữ liệu từng đơn.
- columns chỉ liệt kê tên, không trả tổng tiền hay danh sách giá trị.

## Kết quả để đối chiếu

order_id/customer_id là string, amount là long; có đúng ba tên cột.

## Từ mới cần nhận ra hôm nay

- **Schema (lược đồ tên cột và kiểu)**.
- **String (kiểu chuỗi văn bản)**.
- **Long (kiểu số nguyên 64 bit)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Schema mô tả tên hay cả kiểu?
2. Mã C001 nên là string hay long?
3. nullable=true có nghĩa tất cả giá trị thiếu không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Cả tên và kiểu.
2. String.
3. Không; đó là khả năng biểu diễn thiếu của cột.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
