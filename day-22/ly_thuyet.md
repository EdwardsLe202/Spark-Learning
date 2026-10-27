# Ngày 22 — Xem đơn trước và tổng tích lũy

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Dùng lag và cửa sổ theo dòng để tính lịch sử có thứ tự.

## 1. Dùng lại cách nhóm và sắp xếp

Giữ nhóm theo khách như ngày 21 nhưng sắp ngày tăng dần. **Lag (lấy giá trị của dòng trước)** cho biết số tiền đơn trước của cùng khách. Với C001: O001 không có đơn trước nên NULL; O002 thấy 100000; O008 thấy 200000.

Nếu bỏ partitionBy customer_id, đơn trước có thể của khách khác. Thứ tự là một phần ý nghĩa bài toán, không chỉ cách trình bày kết quả.

## 2. Tổng từ đầu nhóm tới hiện tại

**Running total (tổng tích lũy đến dòng hiện tại)** của C001 là 100000, 300000, 700000. **Window frame (phạm vi dòng đưa vào phép tính)** trong bài dùng `rowsBetween(Window.unboundedPreceding, Window.currentRow)`: từ đầu nhóm tới dòng đang xét.

Cửa sổ theo dòng khác cửa sổ theo số ngày. “Hai đơn gần nhất” không tự có nghĩa “hai ngày”. Bài này chưa dùng rangeBetween; hãy chắc chắn mô tả được các dòng được cộng trước.

## 3. Vẫn giữ từng đơn

Lag và running total thêm thông tin lịch sử cho mỗi đơn, nên bảng vẫn tám dòng. Các khách khác bắt đầu tổng lại từ đơn đầu của họ. Chỉ dùng tất cả đơn trong ví dụ này; nếu yêu cầu chỉ completed, lọc trước khi định nghĩa nguồn cho cửa sổ.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
from pyspark.sql import Window
window = Window.partitionBy("customer_id").orderBy("order_date", "order_id")
frame = window.rowsBetween(Window.unboundedPreceding, Window.currentRow)
result = orders.withColumn("previous_amount", F.lag("amount").over(window)).withColumn("running_amount", F.sum("amount").over(frame))
result.filter(F.col("customer_id") == "C001").select("order_id", "amount", "previous_amount", "running_amount").show()
```

## Đọc từng phần của ví dụ

- Lag dùng thứ tự window; tổng dùng window có frame rõ ràng.
- Dòng đầu C001 có previous_amount=NULL, không phải thiếu lỗi nguồn.
- Tổng cuối C001 bằng tổng ba đơn 700000.

## Kết quả để đối chiếu

C001: O001 previous=NULL/running=100000; O002 previous=100000/running=300000; O008 previous=200000/running=700000.

## Từ mới cần nhận ra hôm nay

- **Lag (lấy giá trị của dòng trước)**.
- **Running total (tổng tích lũy đến dòng hiện tại)**.
- **Window frame (phạm vi dòng đưa vào phép tính)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Lag đầu nhóm NULL có nhất thiết dữ liệu lỗi không?
2. Hai dòng có nghĩa hai ngày không?
3. Tổng tích lũy có làm mất dòng đơn không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không, chưa có dòng trước.
2. Không.
3. Không.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
