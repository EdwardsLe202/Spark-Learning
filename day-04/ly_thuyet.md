# Ngày 04 — Tạo bảng Spark đầu tiên

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Tạo DataFrame ba dòng, hiển thị bảng và đếm dòng.

## 1. Cùng bảng ngày 01, cách làm mới

**PySpark (giao diện Python của Spark)** cho bạn viết yêu cầu xử lý dữ liệu bằng Python. **SparkSession (phiên làm việc với Spark)** là đối tượng để tạo/đọc bảng và gửi yêu cầu. Ta đặt biến tên `spark` cho đối tượng ấy; tên biến có thể khác, nhưng dùng thống nhất giúp đọc ví dụ.

**DataFrame (bảng dữ liệu có cấu trúc)** là cách Spark biểu diễn một bảng có cột. Dữ liệu ba đơn vẫn có ý nghĩa như ngày 01. List Python là đầu vào dùng tạo bảng; DataFrame là đối tượng Spark trả về để bạn thao tác. `df` chỉ là tên biến viết ngắn của DataFrame.

## 2. Đọc phần mở phiên

`from pyspark.sql import SparkSession` lấy lớp cần dùng. Chuỗi `SparkSession.builder.master("local[2]").appName("...").getOrCreate()` tạo hoặc lấy phiên. `local[2]` cho phép chạy hai luồng trên máy hiện tại, không có nghĩa hai máy. `appName` đặt tên ứng dụng để dễ nhận ra trong log.

Bạn có thể dùng nguyên phần mở/đóng phiên trong các bài đầu. Bài cần tập trung là createDataFrame, show, count. Dấu `try/finally` trong file mẫu bảo đảm gọi stop kể cả khi lệnh ở giữa lỗi; đó là cơ chế Python, không phải một phép biến đổi dữ liệu.

## 3. Ba lệnh hôm nay

`createDataFrame(rows, ["order_id", "customer_id", "amount"])` tạo bảng từ danh sách tuple. Thứ tự tên cột khớp vị trí giá trị trong tuple: mã đơn, mã khách, số tiền. `show()` in vài dòng để xem. `count()` trả số dòng dữ liệu, không cộng amount. `spark.stop()` kết thúc phiên khi đã dùng xong.

Nếu terminal có nhiều dòng log nhưng cuối cùng hiển thị đúng bảng và số 3, đó có thể là thông tin khởi động bình thường. Nếu chương trình kết thúc với lỗi, tìm dòng nguyên nhân theo hướng dẫn, không chỉ chụp dòng cuối. Bạn chưa cần hiểu kiến trúc thực thi hay tối ưu hiệu năng hôm nay.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file.

```python
rows = [("O001", "C001", 100000), ("O002", "C001", 200000), ("O003", "C002", 50000)]
orders = spark.createDataFrame(rows, ["order_id", "customer_id", "amount"])
orders.show()
print("Số dòng:", orders.count())
```

## Đọc từng phần của ví dụ

- rows là ba tuple Python đã biết ý nghĩa từ ngày 02.
- createDataFrame trả bảng orders có ba cột; thứ tự cột lấy từ danh sách tên.
- show hiển thị, count đếm ba đơn; chưa tính doanh thu.
- Toàn bộ import, tạo phiên và stop đã có trong vi_du.py; đoạn này nằm bên trong phiên đó.

## Kết quả để đối chiếu

Hiện ba đơn O001, O002, O003 và dòng `Số dòng: 3`. Thứ tự hiển thị không phải thứ tự được bảo đảm cho mọi phép xử lý.

## Từ mới cần nhận ra hôm nay

- **PySpark (giao diện Python của Spark)**.
- **SparkSession (phiên làm việc với Spark)**.
- **DataFrame (bảng dữ liệu có cấu trúc)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. count có cộng tiền không?
2. orders và spark là cùng một loại đối tượng không?
3. local[2] là mấy máy?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không, count đếm dòng.
2. Không; orders là DataFrame, spark là SparkSession.
3. Một máy, cho phép hai luồng làm việc.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
