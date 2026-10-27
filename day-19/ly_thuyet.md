# Ngày 19 — Giữ cả khách chưa có đơn

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Phân biệt left join và left anti join bằng khách C005.

## 1. Đổi câu hỏi thì đổi phía giữ

Hôm qua xem mỗi đơn kèm tên khách. Hôm nay muốn danh sách tất cả khách, kể cả chưa có đơn. Lấy customers làm trái, báo cáo tổng đơn làm phải. **Left join (ghép giữ mọi dòng phía trái)** sẽ giữ C005 với chỉ số bên phải là NULL vì chưa có đơn.

Hãy tổng hợp orders theo customer_id trước rồi ghép. Phía trái có năm khách, phía phải mỗi mã nhiều nhất một dòng tổng, nên kết quả năm dòng. Nếu ghép trực tiếp với từng đơn, số dòng không còn là một khách một dòng.

## 2. Điền 0 có lý do rõ

Ở bài này C005 không có dòng tổng do không có đơn trong nguồn đầy đủ đã biết. Có thể điền total_amount=0 với ý nghĩa tổng đơn trong bộ dữ liệu này bằng 0. Khác ngày 11: một đơn có tiền thiếu không tự có nghĩa tiền bằng 0.

**Left anti join (giữ dòng trái không có khóa khớp)** giúp tìm riêng các khách chưa có bất kỳ đơn nào. `customers.join(orders, "customer_id", "left_anti")` trả C005. Nó không thêm cột phía phải.

## 3. Xem cấp độ của bảng

Trước khi ghép, ghi mỗi dòng bên trái/phải là gì. Đây là thói quen giúp bạn chọn đúng cách tổng hợp và phát hiện nhiều-nhiều ở ngày sau.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
summary = orders.groupBy("customer_id").agg(F.sum("amount").alias("total_amount"))
result = customers.join(summary, "customer_id", "left").fillna({"total_amount": 0})
result.show()
customers.join(orders, "customer_id", "left_anti").show()
```

## Đọc từng phần của ví dụ

- summary có tối đa một dòng mỗi khách.
- Left join giữ năm khách; fillna chỉ điền chỉ số tổng đã định nghĩa.
- Anti join tìm C005 trực tiếp.

## Kết quả để đối chiếu

Báo cáo có 5 dòng, C005 total_amount=0. Anti join chỉ trả C005.

## Từ mới cần nhận ra hôm nay

- **Left join (ghép giữ mọi dòng phía trái)**.
- **Left anti join (giữ dòng trái không có khóa khớp)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Vì sao đặt customers bên trái?
2. Khi nào được điền tổng 0 ở đây?
3. Anti join thêm cột bên phải không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Muốn giữ tất cả khách.
2. Khi không có dòng tổng vì không có đơn trong nguồn đã biết.
3. Không.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
