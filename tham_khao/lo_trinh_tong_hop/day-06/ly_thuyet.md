# Ngày 06 — Lý thuyết: Join tổng hợp và window function

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Ghép bảng không nhân tiền ngoài ý muốn và chọn dòng mới nhất có quy tắc.

## 1. Join đúng cú pháp vẫn có thể sai nghiệp vụ
**Join (phép ghép bảng)** kết hợp các dòng theo điều kiện. **Cardinality (quan hệ số lượng giữa các khóa)** cho biết một khách hàng có một hay nhiều dòng ở mỗi phía. Nếu phía trái có hai giao dịch và phía phải có hai bản ghi cùng customer_id, phép ghép có thể tạo bốn dòng. Tổng tiền tăng không có nghĩa doanh thu tăng.

**Inner join (ghép phần khớp)** giữ cặp khớp; **left join (ghép giữ phía trái)** còn giữ dòng trái không khớp và điền NULL bên phải. **Full outer join (ghép giữ hai phía)** giữ cả hai. **Left semi join (lọc trái có khóa khớp)** không thêm cột phía phải; **left anti join (lọc trái không có khóa khớp)** hữu ích tìm khách hàng không tồn tại. Kiểm tra khóa phía dimension trước khi join.

## 2. Tổng hợp và cửa sổ trả kết quả khác nhau
**Aggregation (phép tổng hợp)** với groupBy làm nhiều dòng thành một dòng mỗi nhóm. **Window function (hàm cửa sổ)** tính trên nhóm dòng liên quan nhưng thường giữ từng dòng đầu vào. `partitionBy` trong Window chia nhóm logic theo khách hàng; nó không có nghĩa ghi các thư mục dữ liệu.

`row_number` đánh số duy nhất trong nhóm; `rank` có thể đồng hạng và có khoảng nhảy. Chọn dòng mới nhất cần `orderBy` timestamp giảm dần và một khóa phụ có ý nghĩa. `lag` xem giá trị dòng trước theo thứ tự đã định.

## 3. Định nghĩa cửa sổ rõ ràng
**Row-based window (cửa sổ theo vị trí dòng)** dùng rowsBetween; ba dòng gần nhất không đồng nghĩa ba ngày. **Range-based window (cửa sổ theo khoảng giá trị)** dùng rangeBetween; khi tính theo giây phải sắp xếp bằng cột số biểu diễn thời gian. Các dòng cùng giá trị sắp xếp có thể cùng nằm trong range. Luôn viết trước biên bao gồm và loại trừ rồi mới chọn cách triển khai.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
from pyspark.sql import Window
w = Window.partitionBy("event_id").orderBy(F.col("ingested_at").desc(), F.col("amount").desc())
latest = read_events(spark, "events_dirty.csv").withColumn("rn", F.row_number().over(w)).filter("rn = 1")
latest.filter("event_id = 'D002'").show()
customers = read_customers(spark)
print("Số khóa customer:", customers.select("customer_id").distinct().count())
```

## Năm ý đối chiếu với lộ trình gốc

- 06.1 — groupBy, agg, distinct và các phép tổng hợp điều kiện.
- 06.2 — Inner, left, full, semi và anti join; kiểm tra khóa và cardinality.
- 06.3 — Join làm nhân số dòng; cột trùng tên, NULL và khóa không khớp.
- 06.4 — Window partitionBy, orderBy, row_number, rank, lag và lead.
- 06.5 — rowsBetween và rangeBetween; cách xác định cửa sổ thời gian và xử lý giá trị bằng nhau.

Các ý trên giữ phạm vi phần 06 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Vì sao left join làm tổng tiền tăng?
2. Khi nào dùng semi thay inner?
3. rowsBetween(-2,0) có phải ba ngày không?

## Đọc thêm từ nguồn chính thức

- [PySpark Window](https://spark.apache.org/docs/3.5.7/api/python/reference/pyspark.sql/api/pyspark.sql.Window.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
