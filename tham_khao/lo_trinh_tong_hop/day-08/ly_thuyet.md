# Ngày 08 — Lý thuyết: Partition shuffle và nền tảng RDD

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Đọc được chi phí shuffle và viết một word count nhỏ bằng hai API.

## 1. Hai nghĩa của partition
Partition thực thi chia công việc trong bộ máy Spark. Partition thư mục tổ chức dữ liệu trên đĩa. Chúng liên quan tới cách đọc ghi nhưng không ánh xạ một-một cố định. `repartition(4, "customer_id")` phân phối dữ liệu cho thực thi; `write.partitionBy("event_date")` tổ chức đầu ra theo giá trị ngày.

**Narrow dependency (phụ thuộc hẹp)** cho phép một partition đầu ra lấy dữ liệu từ phạm vi nhỏ của đầu vào, như nhiều phép filter. **Wide dependency (phụ thuộc rộng)** cần phân phối lại dữ liệu, như groupBy theo khóa. Shuffle có chi phí serialize, truyền hoặc ghi đọc dữ liệu; trên một máy vẫn có chi phí dù không truyền qua mạng nhiều máy.

## 2. Chọn repartition hay coalesce
**Repartition (phân phối lại thành các partition mới)** thường gây shuffle và dùng để tăng, giảm hoặc chia lại theo khóa. **Coalesce (gộp bớt partition)** thường giảm số partition mà tránh shuffle đầy đủ; dễ giữ lại mất cân bằng. Gộp mọi thứ về một partition có thể làm một task chịu toàn bộ công việc. Với lab nhỏ, mục tiêu là thấy số task và tính đúng, không ép một kỹ thuật luôn nhanh hơn.

## 3. RDD giúp hiểu nền tảng
**RDD — Resilient Distributed Dataset (tập dữ liệu phân tán có khả năng tính lại)** hỗ trợ map, filter, reduceByKey. **Lineage (quan hệ nguồn gốc phép tính)** cho Spark biết cách tính lại dữ liệu bị mất từ nguồn còn tồn tại. Nó không thay thế việc lưu nguồn bền vững.

**Broadcast variable (biến chỉ đọc được phân phối để dùng lại)** khác gợi ý broadcast join của SQL dù cùng ý tưởng giảm trao đổi lặp. **Accumulator (biến tích lũy phục vụ thống kê)** không nên làm sổ cái nghiệp vụ. **Side effect (tác động ra ngoài phép tính)** như gọi API có thể lặp khi task được thử lại; cần idempotency ở hệ thống nhận.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
words = spark.sparkContext.parallelize(["spark sql", "spark ml", "sql"], 2)
counts = words.flatMap(lambda s: s.split()).map(lambda w: (w, 1)).reduceByKey(lambda a, b: a + b)
print(sorted(counts.collect()))
df = spark.range(20).repartition(4)
print("repartition:", df.rdd.getNumPartitions())
print("coalesce:", df.coalesce(2).rdd.getNumPartitions())
```

## Năm ý đối chiếu với lộ trình gốc

- 08.1 — Partition trong thực thi khác với partition theo thư mục lưu trữ.
- 08.2 — Narrow và wide dependency; các thao tác thường tạo shuffle.
- 08.3 — repartition và coalesce; ảnh hưởng đến song song và kích thước đầu ra.
- 08.4 — RDD, map, filter, reduceByKey, lineage và khả năng tính lại dữ liệu.
- 08.5 — Broadcast variable, accumulator và rủi ro side effect khi task chạy lại.

Các ý trên giữ phạm vi phần 08 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Hai loại partition khác nhau thế nào?
2. Vì sao reduceByKey phải gom theo khóa?
3. Task retry ảnh hưởng API bên ngoài ra sao?

## Đọc thêm từ nguồn chính thức

- [RDD programming guide](https://spark.apache.org/docs/3.5.7/rdd-programming-guide.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
