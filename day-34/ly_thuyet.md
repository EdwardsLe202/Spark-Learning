# Ngày 34 — RDD với word count nhỏ

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “RDD với word count nhỏ”. Kết quả cần đạt: Ban đầu ml=1, spark=2, sql=2; sau thêm câu sql sql thì sql=4.

## Từ mới gắn với bài này

- **RDD — Resilient Distributed Dataset (tập dữ liệu phân tán có thể tính lại)**.
- **reduceByKey (tổng hợp giá trị theo khóa)**.

## Tình huống và cách hiểu

**RDD — Resilient Distributed Dataset (tập dữ liệu phân tán có thể tính lại)** là nền tảng thấp hơn DataFrame. Mỗi phần tử có thể là một đối tượng Python. map biến từng phần tử; flatMap có thể tạo nhiều phần tử; reduceByKey kết hợp các giá trị có cùng khóa.

Ví dụ tách câu thành từ, gắn mỗi từ số 1 rồi cộng theo từ. Hãy viết tay các cặp trước khi chạy: spark xuất hiện hai lần, sql hai lần, ml một lần. Với dữ liệu có schema, DataFrame thường giúp Spark hiểu và tối ưu tốt hơn; không chuyển mọi bài sang RDD chỉ vì vừa học nó.

Bài dùng Spark Classic local đã có. RDD không có cùng phạm vi hỗ trợ với mọi cách kết nối Spark. Lưu phiên bản và cách chạy khi báo lỗi.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-034/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
rdd = spark.sparkContext.parallelize(["spark sql", "spark ml", "sql"], 2)
pairs = rdd.flatMap(lambda s: s.split()).map(lambda word: (word, 1))
counts = pairs.reduceByKey(lambda a, b: a + b)
print(sorted(counts.collect()))
```

## Đọc từng phần của ví dụ

FlatMap làm số phần tử tăng theo số từ. Collect chỉ nhận ba cặp kết quả nhỏ đã tổng hợp.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ban đầu ml=1, spark=2, sql=2; sau thêm câu sql sql thì sql=4.

## Ba câu kiểm tra hiểu bài

1. RDD — Resilient Distributed Dataset có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tập dữ liệu phân tán có thể tính lại.
- Luồng chính: FlatMap làm số phần tử tăng theo số từ. Collect chỉ nhận ba cặp kết quả nhỏ đã tổng hợp.
- Đối chiếu tiêu chí: Ban đầu ml=1, spark=2, sql=2; sau thêm câu sql sql thì sql=4. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 08 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
