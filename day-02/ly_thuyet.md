# Ngày 02 — Làm cùng bài toán bằng Python quen thuộc

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Lọc đơn và tính tổng bằng list/dict trước khi chuyển sang Spark.

## 1. Đổi bảng thành Python

Giữ nguyên ba đơn ngày 01. Mỗi dictionary có ba trường, tương ứng ba cột. Cả list chứa ba dictionary tương ứng ba dòng. **Record (một bản ghi)** ở đây chỉ là một đơn hàng; từ này gần nghĩa một dòng trong bảng.

`orders[0]["amount"]` lấy tiền của đơn đầu. Giá trị 100000 là số nguyên để cộng; chuỗi `"100000"` là văn bản và cần chuyển kiểu trước khi tính toán. Bài này dùng sẵn số nguyên để tập trung vào thao tác.

## 2. Lọc là giữ dòng thỏa điều kiện

**Filter (lọc các dòng theo điều kiện)** nghĩa là kiểm tra từng đơn và giữ đơn cần. Điều kiện `order["customer_id"] == "C001"` đúng với O001, O002; sai với O003. Giữ hai đơn này không sửa các đơn nguồn, chỉ tạo danh sách kết quả khác.

Sau lọc, `sum(order["amount"] for order in selected)` cộng amount của các đơn đã giữ. Bạn có thể viết vòng for dài hơn nếu dễ hiểu; mục tiêu là thấy được đầu vào → điều kiện → kết quả.

## 3. Vì sao chưa dùng Spark ngay?

Bạn đã biết câu hỏi nghiệp vụ và kết quả. Tới ngày học Spark, phần mới sẽ là cách viết yêu cầu cho Spark, thay vì vừa phải hiểu bài toán vừa học cú pháp. Không cần tự viết vòng lặp phân tán hay cài thêm thư viện hôm nay.

Nếu một đoạn list comprehension chưa quen, thay bằng `selected = []` rồi vòng `for`, `if` và `append`. Hai cách cần cho cùng hai đơn. Hãy tự viết một lần thay vì chỉ chạy file mẫu.

## Ví dụ có thể chạy nguyên file

Ví dụ hôm nay dùng Python thông thường; ngày 01 có thể làm hoàn toàn trên giấy.

```python
orders = [
    {"order_id": "O001", "customer_id": "C001", "amount": 100000},
    {"order_id": "O002", "customer_id": "C001", "amount": 200000},
    {"order_id": "O003", "customer_id": "C002", "amount": 50000},
]
selected = [order for order in orders if order["customer_id"] == "C001"]
print("Các đơn của C001:", selected)
print("Tổng của C001:", sum(order["amount"] for order in selected))
```

## Đọc từng phần của ví dụ

- orders là dữ liệu đầu vào giống bảng hôm qua.
- selected giữ những dictionary có customer_id bằng C001.
- sum chỉ cộng amount trong selected nên kết quả là 300000, không phải tổng toàn bảng.

## Kết quả để đối chiếu

Có hai đơn trong selected: O001, O002. Tổng C001 = 300000.

## Từ mới cần nhận ra hôm nay

- **Record (một bản ghi)**.
- **Filter (lọc các dòng theo điều kiện)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Bước lọc có tự cộng tiền không?
2. Vì sao amount nên là số?
3. Thêm một đơn có nhất thiết thêm khách mới không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không; lọc và cộng là hai bước khác nhau.
2. Để thực hiện phép toán số đúng ý nghĩa.
3. Không, có thể là đơn của khách đã tồn tại.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
