# Ngày 03 — Lý thuyết: Kiến trúc và cách Spark thực thi

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Giải thích driver, task và lazy evaluation bằng một phép tổng hợp có quan sát.

## 1. Ai điều phối, ai tính toán?
**Driver (tiến trình điều phối)** chạy chương trình chính và lập lịch công việc. **Executor (tiến trình thực thi)** chạy các phần việc và giữ dữ liệu được giao trong triển khai cluster. **Worker node (máy chạy tác vụ)** có thể chứa executor; **cluster manager (bộ quản lý tài nguyên cụm máy)** cấp tài nguyên. Chúng là các vai trò khác nhau. Trong local mode, việc thực thi diễn ra trên một máy và không mô phỏng đầy đủ mạng hay lỗi của cluster.

**Partition (phần dữ liệu để xử lý song song)** là đơn vị chia dữ liệu. **Task (tác vụ nhỏ)** xử lý một partition trong một stage. Nhiều partition có thể tạo nhiều task nhưng số task chạy đồng thời còn bị giới hạn bởi số luồng và tài nguyên.

## 2. Viết kế hoạch trước, thực hiện sau
**Transformation (phép biến đổi)** như `select` và `filter` trả về một DataFrame biểu diễn kế hoạch mới. **Lazy evaluation (thực thi trì hoãn)** nghĩa là Spark thường chờ tới **action (thao tác yêu cầu kết quả)** như `count`, `show` hay ghi file mới thực thi phần tính toán cần thiết. Việc đọc schema hoặc liệt kê file vẫn có thể làm một số công việc sớm, nên đừng hiểu lazy là tuyệt đối không làm gì.

Một **job (công việc thực thi)** có thể chia thành nhiều **stage (giai đoạn thực thi)**. Khi cần phân phối lại dữ liệu để nhóm theo khóa, Spark thường tạo **shuffle (trao đổi dữ liệu giữa các partition)**, tạo ranh giới stage. `groupBy` thường cần shuffle; `filter` riêng lẻ thường không cần.

## 3. Đọc bằng chứng
`explain("formatted")` cho thấy **execution plan (kế hoạch thực thi)**. Spark UI cho thấy việc đã chạy, số task và thời gian. Với **Adaptive Query Execution — AQE (điều chỉnh kế hoạch khi chạy)**, số partition cuối có thể khác cấu hình ban đầu. Spark Connect tách client khỏi server; bài RDD trong repo dùng Spark Classic, tức cách chạy phiên Spark thông thường ở local.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
df = spark.range(0, 100, 1, 4)
result = df.withColumn("bucket", F.col("id") % 3).groupBy("bucket").count()
result.explain("formatted")
result.orderBy("bucket").show()
print("Partition đầu vào:", df.rdd.getNumPartitions())
```

## Năm ý đối chiếu với lộ trình gốc

- 03.1 — Driver, executor, worker và cluster manager; trách nhiệm từng thành phần.
- 03.2 — Partition là gì; task xử lý dữ liệu và mức song song.
- 03.3 — Transformation, action và lazy evaluation qua ví dụ đọc lọc nhóm.
- 03.4 — Application, job, stage và task; nhận biết nơi xuất hiện shuffle.
- 03.5 — SparkSession, Spark Classic và Spark Connect ở mức khái niệm; giới hạn của local mode.

Các ý trên giữ phạm vi phần 03 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Nếu không có action, đoạn nào có thể chưa thực thi?
2. Vì sao groupBy thường cần trao đổi dữ liệu?
3. Tăng partition có luôn giảm thời gian không?

## Đọc thêm từ nguồn chính thức

- [Cluster overview](https://spark.apache.org/docs/3.5.7/cluster-overview.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
