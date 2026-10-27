# Ngày 40 — Built-in Python UDF và pandas UDF

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Built-in Python UDF và pandas UDF”. Kết quả cần đạt: SPARK, NULL, SQL giống giữa hai nhánh; không kết luận tốc độ từ ba dòng.

## Từ mới gắn với bài này

- **Built-in function (hàm Spark có sẵn)**.
- **UDF — User Defined Function (hàm do người dùng định nghĩa)**.
- **Arrow (định dạng trao đổi dữ liệu theo cột)**.

## Tình huống và cách hiểu

**Built-in function (hàm Spark có sẵn)** như upper cho phép Spark hiểu biểu thức. **UDF — User Defined Function (hàm do người dùng định nghĩa)** bằng Python có thể thêm chi phí truyền giữa JVM và Python. Không thay hàm có sẵn chỉ để code trông giống Python quen.

Pandas UDF xử lý theo lô, dùng **Arrow (định dạng trao đổi dữ liệu theo cột)** khi phù hợp. Nó vẫn cần schema, dependency và bộ nhớ cho từng lô. Nhanh hay chậm phải đo với action thật sự dùng cột tính được; count đơn giản có thể không cần tính cột mới.

Ngày này so upper với UDF trên vài tên để kiểm tra ý nghĩa. Bài thực hành thêm pandas UDF sau khi cài requirements-ml. Không gọi API ngoài trong UDF thiếu giới hạn và chống lặp.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-040/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from pyspark.sql.types import StringType
uppercase = F.udf(lambda s: s.upper() if s is not None else None, StringType())
df = spark.createDataFrame([("spark",), (None,), ("sql",)], "name string")
df.select(F.upper("name").alias("builtin"), uppercase("name").alias("python_udf")).show()
```

## Đọc từng phần của ví dụ

Hai hàm giữ NULL và đổi chuỗi giống nhau. Kiểu trả UDF được khai báo StringType.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

SPARK, NULL, SQL giống giữa hai nhánh; không kết luận tốc độ từ ba dòng.

## Ba câu kiểm tra hiểu bài

1. Built-in function có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: hàm Spark có sẵn.
- Luồng chính: Hai hàm giữ NULL và đổi chuỗi giống nhau. Kiểu trả UDF được khai báo StringType.
- Đối chiếu tiêu chí: SPARK, NULL, SQL giống giữa hai nhánh; không kết luận tốc độ từ ba dòng. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 09 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
