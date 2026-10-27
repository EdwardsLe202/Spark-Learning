# Ngày 31 — Driver và executor qua báo cáo đã biết

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Driver và executor qua báo cáo đã biết”. Kết quả cần đạt: Master local[2], tổng 1400000. Sơ đồ phân biệt tiến trình và máy.

## Từ mới gắn với bài này

- **Driver (tiến trình điều phối)**.
- **Executor (tiến trình thực thi)**.

## Tình huống và cách hiểu

Ở ngày 29, bạn viết một báo cáo rồi yêu cầu Spark trả kết quả. **Driver (tiến trình điều phối)** chạy chương trình chính, giữ kế hoạch và yêu cầu thực thi. **Executor (tiến trình thực thi)** chạy các phần việc được giao trong triển khai cluster. Dữ liệu lớn cần được xử lý ở nơi thực thi, tránh đưa toàn bộ về driver.

Hãy xem driver như người giao việc, còn executor như người xử lý từng chồng đơn. Số executor không phải số đơn. Trong local[2], Spark chạy trên một máy; hai luồng chưa tạo thành hai máy độc lập. Worker là nơi chạy tiến trình thực thi, còn cluster manager cấp tài nguyên.

Ví dụ chỉ lấy bảng tổng một dòng về Python. first ở đây hợp lý vì kích thước đã được thu nhỏ; collect toàn nguồn có thể gây hết RAM driver. Bạn cần nói rõ điều đã chạy local và điều mới là thiết kế cluster.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-031/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
print("Ứng dụng:", spark.sparkContext.appName)
print("Chế độ:", spark.sparkContext.master)
summary = orders.agg(F.sum("amount").alias("total"))
print("Một dòng tổng về driver:", summary.first()["total"])
print("UI khi phiên còn chạy:", spark.sparkContext.uiWebUrl)
```

## Đọc từng phần của ví dụ

Đọc master để biết đây là local. agg thu nhỏ tám đơn thành một dòng trước khi first lấy kết quả về Python.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Master local[2], tổng 1400000. Sơ đồ phân biệt tiến trình và máy.

## Ba câu kiểm tra hiểu bài

1. Driver có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tiến trình điều phối.
- Luồng chính: Đọc master để biết đây là local. agg thu nhỏ tám đơn thành một dòng trước khi first lấy kết quả về Python.
- Đối chiếu tiêu chí: Master local[2], tổng 1400000. Sơ đồ phân biệt tiến trình và máy. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 03 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).

## Spark Classic và Spark Connect ở mức nhận diện

**Spark Classic (cách chạy ứng dụng Spark thông thường)** dùng Python phối hợp JVM driver qua gateway. **Spark Connect (cách client gửi kế hoạch tới server Spark tách biệt)** không có cùng phạm vi API thấp như RDD. Khóa dùng Classic cho các lab RDD; đừng đổi cách kết nối rồi giả định mọi API vẫn hoạt động. Không cần triển khai Connect để hoàn thành bài này.
