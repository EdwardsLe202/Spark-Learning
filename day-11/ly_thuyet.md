# Ngày 11 — Giá trị thiếu và cách lọc NULL

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Phân biệt thiếu tiền với tiền bằng 0; dùng isNull và fillna có lý do.

## 1. Chưa biết số tiền không phải số 0

**NULL (giá trị thiếu hoặc chưa biết)** biểu diễn việc không có giá trị trong cột. Trong dữ liệu Python dùng None để tạo giá trị này. Số 0 là số đã biết, còn NULL nói rằng chưa biết; chuỗi rỗng là văn bản không có ký tự, cũng khác NULL.

Ví dụ hôm nay có A=100000, B=None, C=0. Chỉ B thiếu; C vẫn là một số tiền hợp lệ. Một phép lọc amount > 0 chỉ giữ A: C không lớn hơn 0, B không có thông tin để điều kiện đúng.

## 2. Dùng phương thức phù hợp

`df["amount"].isNull()` kiểm tra thiếu. `isNotNull()` giữ giá trị đã biết. Không dùng so sánh bằng None như một phép so bằng số thông thường. `fillna({"amount": 0})` tạo bảng có số 0 ở những amount thiếu, nhưng đó là một quyết định thay dữ liệu.

Với tiền đơn hàng, chưa biết tiền mà tự điền 0 có thể làm báo cáo hiểu sai. Trong lab ta chỉ thử để thấy hành vi, không khẳng định điền 0 luôn đúng. Cách an toàn để quan sát là tách dòng thiếu thành bảng riêng rồi báo số lượng cần xử lý.

## 3. Đếm và cộng khi có thiếu

`count()` của DataFrame đếm cả ba dòng. `F.count("amount")` chỉ đếm giá trị amount không NULL, tức hai. `sum` bỏ qua các giá trị NULL trong ví dụ có cả số hợp lệ, nên tổng 100000 không chứng minh rằng cả ba đơn đều có số tiền đầy đủ. Luôn báo thêm số dòng thiếu.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file.

```python
orders = spark.createDataFrame([("A", 100000), ("B", None), ("C", 0)], "order_id string, amount long")
missing = orders.filter(orders["amount"].isNull())
missing.show()
orders.agg(F.count("*").alias("rows"), F.count("amount").alias("known_amounts"), F.sum("amount").alias("total")).show()
```

## Đọc từng phần của ví dụ

- Bảng riêng ba dòng giúp nhìn rõ None/0.
- isNull chỉ tìm B.
- rows=3, known_amounts=2, total=100000; số dòng và số giá trị biết là khác nhau.

## Kết quả để đối chiếu

Một dòng thiếu là B; count(*)=3, count(amount)=2; tổng số tiền đã biết 100000.

## Từ mới cần nhận ra hôm nay

- **NULL (giá trị thiếu hoặc chưa biết)**.
- **isNull (kiểm tra giá trị thiếu)**.
- **fillna (điền giá trị thiếu theo quy tắc)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. NULL có bằng 0 không?
2. count(amount) đếm mấy giá trị trong mẫu?
3. fillna có tự biết nghiệp vụ không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không.
2. Hai giá trị không NULL.
3. Không; người viết phải chọn quy tắc phù hợp.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
