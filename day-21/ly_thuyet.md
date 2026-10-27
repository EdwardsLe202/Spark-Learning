# Ngày 21 — Chọn đơn mới nhất cho mỗi khách

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Dùng window và row_number để chọn một dòng theo thứ tự xác định.

## 1. Giữ thông tin của đúng một đơn

GroupBy max ngày có thể cho ngày mới nhất, nhưng chưa lấy đủ order_id và amount của chính đơn ấy. **Window function (hàm tính trên nhóm dòng liên quan)** cho phép đánh số các đơn của từng khách rồi giữ dòng số 1.

`Window.partitionBy("customer_id")` đặt nhóm logic theo khách. `orderBy(F.col("order_date").desc(), F.col("order_id").desc())` sắp ngày mới trước, nếu cùng ngày thì mã đơn giảm dần làm tiêu chí phụ. Với chuỗi YYYY-MM-DD sạch của fixture, thứ tự từ điển khớp lịch; nguồn tổng quát nên dùng date đã parse ở ngày 15.

## 2. Đánh số rồi lọc

**row_number (số thứ tự duy nhất trong nhóm)** bắt đầu 1 trong từng khách. `F.row_number().over(window)` tạo biểu thức đánh số; withColumn đặt vào rn. Sau đó filter rn=1 chọn đơn mới nhất theo quy tắc.

Đây không phải dropDuplicates chọn tùy ý. Nếu nguồn có nhiều bản hoàn toàn bằng tất cả tiêu chí sắp xếp, cần chính sách bổ sung; đừng tuyên bố luôn quyết định duy nhất trong mọi nguồn. Fixture dùng order_id khác nhau nên quy tắc đủ rõ.

## 3. Window không tự giảm dòng

Sau khi thêm rn vẫn có tám đơn. Chỉ bước filter rn=1 làm còn bốn dòng. Phân biệt điều này với groupBy sẽ giúp bạn đọc đúng các bài cửa sổ tiếp theo.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
from pyspark.sql import Window
window = Window.partitionBy("customer_id").orderBy(F.col("order_date").desc(), F.col("order_id").desc())
ranked = orders.withColumn("rn", F.row_number().over(window))
ranked.select("customer_id", "order_id", "order_date", "rn").show()
latest = ranked.filter(F.col("rn") == 1)
latest.select("customer_id", "order_id").show()
```

## Đọc từng phần của ví dụ

- partitionBy nhóm theo khách, không phải ghi thư mục dữ liệu.
- desc đưa ngày mới trước; mã đơn là tiêu chí phụ.
- rn=1 giữ một đơn mỗi khách, cả completed và cancelled nếu đó là đơn mới nhất của nguồn đã chọn.

## Kết quả để đối chiếu

C001→O008; C002→O005; C003→O006; C004→O007. ranked có 8 dòng, latest có 4.

## Từ mới cần nhận ra hôm nay

- **Window function (hàm tính trên nhóm dòng liên quan)**.
- **row_number (số thứ tự duy nhất trong nhóm)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Thêm rn có tự giảm 8 dòng xuống 4 không?
2. Vì sao có tiêu chí phụ?
3. PartitionBy trong Window có ghi file không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không; filter mới giảm.
2. Để quyết định thứ tự khi ngày bằng nhau.
3. Không.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
