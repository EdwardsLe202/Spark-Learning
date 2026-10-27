# Ngày 18 — Ghép đơn hàng với thông tin khách

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Dùng inner join để thêm tên khách và vùng vào mỗi đơn.

## 1. Vì sao cần bảng thứ hai?

Orders có mã khách nhưng chưa có tên/vùng. File customers.csv có C001=An/HN, C002=Binh/HCM, C003=Chi/DN, C004=Dung/HN, C005=Ha/HCM. Mỗi khách có đúng một dòng. **Join (ghép bảng theo điều kiện)** dùng customer_id để bổ sung thông tin cho đơn.

C001 có ba đơn và một dòng khách, nên ba đơn đều có name=An. Mỗi dòng kết quả vẫn là một đơn. Đây là quan hệ nhiều đơn ứng với một khách; không thêm đơn mới chỉ vì bổ sung tên.

## 2. Inner join giữ dòng nào?

**Inner join (chỉ giữ các khóa khớp hai phía)** không tạo dòng riêng cho khách chưa mua hàng. C005 có trong customers nhưng không có đơn ở orders, nên không xuất hiện trong kết quả ghép hôm nay.

`orders.join(customers, on="customer_id", how="inner")` dùng một cột trùng tên làm khóa. Đây không phải ghép theo số thứ tự dòng hay tên hiển thị. Nếu phía customers có nhiều bản cùng mã, kết quả có thể nhân số dòng; ngày 20 dành riêng để bắt lỗi này.

## 3. Kiểm tra ý nghĩa trước sau

Vì mọi customer_id ở nguồn tám đơn đều tồn tại trong bảng khách, join chuẩn giữ tám đơn và tổng 1400000. Đối soát trước/sau giúp biết phép ghép có thêm thông tin đúng như mong muốn không.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
joined = orders.join(customers, on="customer_id", how="inner")
joined.select("order_id", "customer_id", "name", "region", "amount").show()
print("Số dòng:", joined.count())
```

## Đọc từng phần của ví dụ

- Bộ đọc customers có schema riêng ba cột.
- Join khớp theo mã, không theo vị trí dòng.
- select chọn các cột liên quan để dễ thấy tên/vùng đã được bổ sung.

## Kết quả để đối chiếu

8 dòng; O001/O002/O008 thuộc An/HN; tổng tiền vẫn 1400000. C005 không có đơn.

## Từ mới cần nhận ra hôm nay

- **Join (ghép bảng theo điều kiện)**.
- **Inner join (chỉ giữ các khóa khớp hai phía)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Join theo mã hay thứ tự dòng?
2. Một dòng joined là khách hay đơn?
3. Vì sao C005 bị vắng?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Theo mã customer_id.
2. Một đơn có thêm thông tin khách.
3. Không có đơn khớp.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
