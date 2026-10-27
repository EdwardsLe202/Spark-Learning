# Ngày 27 — Partition và chi phí shuffle

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Đổi cách chia công việc nhưng giữ nguyên kết quả của bảng.

## 1. Chia công việc, không chia ý nghĩa dữ liệu

**Partition (phần dữ liệu để xử lý song song)** là phần Spark giao cho công việc thực thi. Tám đơn có thể được chia thành hai hoặc bốn phần nhưng vẫn là tám đơn. Số phần không phải số khách hay số máy.

**Repartition (chia lại dữ liệu thành các partition)** bằng `orders.repartition(2)` thường cần phân phối lại dữ liệu. `F.spark_partition_id()` cho biết mã partition tại điểm tính biểu thức; nó chỉ dùng quan sát, không phải mã bền vững của đơn hàng để lưu làm khóa nghiệp vụ.

## 2. Khi nào cần di chuyển dữ liệu?

**Shuffle (phân phối lại dữ liệu giữa các phần xử lý)** thường xuất hiện khi phải gom cùng khóa để groupBy hoặc join theo cách cần phân phối lại. Nó có chi phí trao đổi, sắp xếp và đọc/ghi trung gian. Trên một máy vẫn có chi phí dù chưa trao đổi qua mạng nhiều máy.

Tăng số partition không tự tăng tài nguyên phần cứng và có thể tăng chi phí quản lý. Bảng tám dòng chỉ dùng quan sát tính đúng; không chứng minh partition nào tốt nhất cho dữ liệu thật.

## 3. Khác thư mục lưu trữ

Thư mục `order_date=...` ở ngày 24 tổ chức dữ liệu lưu. Partition thực thi tổ chức công việc lúc chạy. Hai khái niệm có liên quan nhưng không ánh xạ một-một cố định. Đừng đếm thư mục rồi mặc định đó là số tác vụ của mọi truy vấn.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
two = orders.repartition(2)
observed = two.withColumn("execution_partition", F.spark_partition_id())
observed.groupBy("execution_partition").count().show()
print("Số đơn sau chia:", two.count())
two.groupBy("customer_id").agg(F.sum("amount").alias("total")).show()
```

## Đọc từng phần của ví dụ

- Repartition thay cách chia, không loại đơn.
- Bảng đếm partition giúp quan sát số dòng phân bố tại phép tính.
- Tổng theo khách trên toàn nguồn vẫn C001=700000, C002=200000, C003=420000, C004=80000.

## Kết quả để đối chiếu

Số đơn vẫn 8, tổng 1400000. Không yêu cầu từng partition chứa đúng số dòng cố định trong mọi môi trường.

## Từ mới cần nhận ra hôm nay

- **Partition (phần dữ liệu để xử lý song song)**.
- **Shuffle (phân phối lại dữ liệu giữa các phần xử lý)**.
- **Repartition (chia lại dữ liệu thành các partition)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Bốn partition có nghĩa bốn máy không?
2. Repartition có được làm đổi tổng tiền không?
3. Partition thực thi có luôn là thư mục không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không.
2. Không.
3. Không.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
