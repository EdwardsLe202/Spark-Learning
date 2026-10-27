# Ngày 10 — Tổng hợp tiền theo từng khách

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Dùng groupBy và agg để tạo một dòng kết quả cho mỗi khách.

## 1. Từ đơn hàng sang báo cáo khách hàng

Nguồn có tám đơn; C001 có ba đơn. **Group (nhóm theo khóa)** đặt các đơn có cùng customer_id vào một nhóm logic. **Aggregation (tổng hợp nhiều dòng)** tạo chỉ số như tổng tiền và số đơn của từng nhóm. Kết quả đổi cấp độ: một dòng bây giờ là một khách, không còn một đơn.

Để tính doanh thu của đơn đã hoàn tất, phải filter status trước khi groupBy. Nếu nhóm toàn bộ rồi gọi đó là doanh thu hoàn tất, đơn O004 bị hủy vẫn bị cộng. Viết rõ tập dòng cần tính giúp tránh lỗi nghiệp vụ.

## 2. Hàm sum và count trong Spark

`from pyspark.sql import functions as F` nhập nhóm hàm Spark và đặt tên ngắn F. `F.sum("amount")` nói cộng cột amount; `F.count("*")` nói đếm các dòng. F không phải tên một cột. Trong `agg`, dùng alias đặt tên như total_amount và order_count để đọc kết quả dễ hơn.

`groupBy("customer_id").agg(...)` giảm số dòng theo số nhóm. Nó khác withColumn hôm qua vốn giữ tám đơn. Với dữ liệu completed có bốn khách, kết quả có bốn dòng.

## 3. Tính tay một nhóm trước

C001: 100000 + 200000 + 400000 = 700000, có ba đơn. C002: 50000 + 150000 = 200000, hai đơn. C003 chỉ giữ O006=120000 vì O004 đã hủy. C004 có O007=80000. Tổng bốn khách = 1100000.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
completed = orders.filter(orders["status"] == "completed")
summary = completed.groupBy("customer_id").agg(
    F.sum("amount").alias("total_amount"),
    F.count("*").alias("order_count"),
)
summary.show()
```

## Đọc từng phần của ví dụ

- completed là nguồn đã lọc; chỉ 7 đơn đi vào báo cáo.
- groupBy chọn customer_id làm khóa nhóm.
- agg tính hai chỉ số, alias cho tên dễ đọc.
- Kết quả có 4 khách; C001 tổng 700000 với 3 đơn.

## Kết quả để đối chiếu

C001: 700000/3; C002: 200000/2; C003: 120000/1; C004: 80000/1. Tổng 1100000.

## Từ mới cần nhận ra hôm nay

- **Group (nhóm theo khóa)**.
- **Aggregation (tổng hợp nhiều dòng)**.
- **Alias (tên thay thế trong kết quả)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Một dòng summary còn là một đơn không?
2. Vì sao filter trước tổng hợp?
3. F.sum khác orders.count ở đâu?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không, là một khách.
2. Để chỉ cộng các đơn thuộc tập cần báo cáo.
3. F.sum cộng số tiền; count đếm dòng.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
