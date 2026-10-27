# Ngày 46 — Data interval và hai loại thời gian

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Data interval và hai loại thời gian”. Kết quả cần đạt: Tiny ngày 20 chỉ có T002; biên end loại trừ.

## Từ mới gắn với bài này

- **Event time (thời gian sự kiện xảy ra)**.
- **Ingestion time (thời gian dữ liệu được nhận)**.

## Tình huống và cách hiểu

**Event time (thời gian sự kiện xảy ra)** trả lời giao dịch thuộc ngày nào. **Ingestion time (thời gian dữ liệu được nhận)** trả lời hệ thống biết giao dịch từ lúc nào. Một đơn hôm qua có thể được nhận hôm nay; gộp hai mốc sẽ làm sai dữ liệu theo ngày hoặc feature tại quá khứ.

Data interval là khoảng đầu vào mà job chịu trách nhiệm, không phải đồng hồ lúc chạy. Dùng biên [start,end) để hai ngày liên tiếp không đếm đôi sự kiện đúng mốc nửa đêm. Múi giờ của bài là UTC.

Ví dụ thêm hai cột timestamp từ chuỗi gốc. Parse phải được kiểm tra; không bỏ toàn bộ timestamp lỗi rồi mất dấu. Bạn đã học tách lỗi ở khóa nền, giờ áp dụng vào sự kiện có thời gian sẵn có.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-046/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
events = events_df(spark, "events_tiny.csv")
start = F.to_timestamp(F.lit("2025-01-20T00:00:00Z"))
end = F.to_timestamp(F.lit("2025-01-21T00:00:00Z"))
result = events.filter((F.col("event_ts") >= start) & (F.col("event_ts") < end))
result.select("event_id", "event_ts", "available_ts").show(truncate=False)
```

## Đọc từng phần của ví dụ

events_df giữ chuỗi nguồn và tạo event_ts/available_ts. Interval lấy đúng ngày 20, không lấy đầu ngày 21.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Tiny ngày 20 chỉ có T002; biên end loại trừ.

## Ba câu kiểm tra hiểu bài

1. Event time có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: thời gian sự kiện xảy ra.
- Luồng chính: events_df giữ chuỗi nguồn và tạo event_ts/available_ts. Interval lấy đúng ngày 20, không lấy đầu ngày 21.
- Đối chiếu tiêu chí: Tiny ngày 20 chỉ có T002; biên end loại trừ. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).

## Window theo thời gian và theo số dòng

`rowsBetween(-2, 0)` lấy vị trí ba dòng, không phải ba ngày. **Range-based window (cửa sổ theo khoảng giá trị)** dùng cột số thời gian để định nghĩa khoảng; các dòng cùng giá trị thời gian có thể cùng được lấy.

```python
seconds = events.withColumn("event_seconds", F.col("event_ts").cast("long"))
w = Window.partitionBy("customer_id").orderBy("event_seconds").rangeBetween(-7 * 86400, 0)
seconds.withColumn("spend_7d_inclusive", F.sum("amount_num").over(w)).select("event_id", "spend_7d_inclusive").show()
```

Ví dụ dùng hai biên bao gồm theo API rangeBetween, khác quy tắc feature [cutoff−30 ngày,cutoff) đã chốt ở ngày56. Test timestamp bằng nhau và dòng đúng biên để không nhầm hai định nghĩa.
