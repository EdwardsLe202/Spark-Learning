# Ngày 02 — Lý thuyết: Môi trường Spark trên macOS

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Chạy Spark từ terminal mới, đọc ghi Parquet và ghi lại bộ phiên bản.

## 1. Ba thành phần phải khớp nhau
**Runtime (môi trường thực thi)** của bài Spark gồm Python, Java và thư viện PySpark. Python là nơi bạn viết lệnh; **JVM — Java Virtual Machine (máy ảo Java)** chạy bộ máy Spark. Repo chọn Python 3.11, Java 17 và PySpark 3.5.7 làm bộ học cố định. Đây là bộ phiên bản của bài học, không phải tuyên bố phiên bản mới nhất.

**Virtual environment (môi trường Python riêng)** giống một hộp dụng cụ cho repo: cài PySpark vào hộp này để tránh đụng thư viện dự án khác. Lệnh `python -m pip` dùng pip của đúng Python đang chạy. `JAVA_HOME` chỉ tới thư mục JDK; `PYSPARK_PYTHON` chỉ tới Python cho tiến trình thực hiện việc. Hai biến này có nhiệm vụ khác nhau.

## 2. Tạo và kết thúc phiên Spark
**SparkSession (đối tượng làm việc với bảng và SQL trong Spark)** là cửa vào chính. `master("local[2]")` cho phép dùng hai luồng làm việc trên máy hiện tại. `getOrCreate()` lấy phiên đang tồn tại hoặc tạo mới. Dùng `try/finally` hoặc tiện ích `spark_session` của repo để luôn gọi `stop()` khi xong.

**Smoke check (kiểm tra khởi động tối thiểu)** cần đi xuyên luồng: tạo bảng, tính tổng, ghi file, đọc lại và đối chiếu. Chỉ import thành công chưa chứng minh Java hay quá trình đọc ghi hoạt động.

## 3. Dữ liệu đầu ra
**Parquet (định dạng lưu dữ liệu theo cột)** thường là một thư mục có nhiều file phần, không nhất thiết một file duy nhất. Spark UI thường mở ở `http://localhost:4040` khi phiên còn sống; khi cổng bận có thể chuyển cổng khác. Ghi địa chỉ thực tế từ log. Chỉ thêm notebook sau khi script chạy được để dễ phân biệt lỗi môi trường với lỗi notebook.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
from spark_lab import output_dir
out = output_dir(2) / "smoke_parquet"
df = spark.createDataFrame([("A", 2), ("B", 3)], "name string, value int")
assert df.agg(F.sum("value")).first()[0] == 5
df.write.mode("overwrite").parquet(str(out))
assert spark.read.parquet(str(out)).count() == 2
print("Smoke check: 2 dòng, tổng = 5")
```

## Năm ý đối chiếu với lộ trình gốc

- 02.1 — Kiểm tra chip Intel hay Apple Silicon, RAM, dung lượng trống và kiến trúc terminal.
- 02.2 — Chọn bộ phiên bản Java, Python và PySpark tương thích theo tài liệu chính thức.
- 02.3 — Tạo môi trường Python riêng, ghi dependency và cấu hình JAVA_HOME khi cần.
- 02.4 — Tạo SparkSession, dùng notebook và file Python; dừng session đúng cách.
- 02.5 — Kiểm tra local mode, Spark UI, log và các lỗi khởi động thường gặp.

Các ý trên giữ phạm vi phần 02 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Vì sao notebook import được nhưng terminal không import được?
2. local[2] có nghĩa hai máy không?
3. Vì sao cần stop phiên?

## Đọc thêm từ nguồn chính thức

- [PySpark installation 3.5.7](https://spark.apache.org/docs/3.5.7/api/python/getting_started/install.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
