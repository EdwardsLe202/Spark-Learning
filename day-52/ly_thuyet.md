# Ngày 52 — Event time khác processing time trong stream

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Event time khác processing time trong stream”. Kết quả cần đạt: Event time vẫn năm 2025; processing time theo lần chạy thực tế, không có số thời gian cố định.

## Từ mới gắn với bài này

- **Processing time (thời gian hệ thống xử lý)**.
- **Late data (dữ liệu đến muộn)**.

## Tình huống và cách hiểu

**Processing time (thời gian hệ thống xử lý)** là lúc job nhận và xử lý dữ liệu. **Late data (dữ liệu đến muộn)** có event time cũ nhưng tới ở batch sau. Báo cáo theo thời gian sự kiện và theo thời gian xử lý có thể cho hai cách nhóm khác nhau.

Ví dụ sự kiện lúc 10:00 được xử lý khi bạn chạy bài hiện tại. Không sửa event time sang hiện tại để làm nó trông mới. Việc chấp nhận trễ bao lâu là policy, chưa tự giải quyết chỉ bằng parse timestamp.

Current_timestamp trong query batch đánh dấu thời điểm thực thi cho lần ấy. Bài dùng batch nhỏ để nhìn hai cột, rồi lab áp dụng vào stream đã biết. Không dùng đồng hồ máy để giả định watermark là now trừ một khoảng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-052/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
df = spark.createDataFrame([("late-1", "2025-01-01T10:00:00Z")], "event_id string, event_time string")
df.withColumn("event_ts", F.to_timestamp("event_time")).withColumn("processed_at", F.current_timestamp()).show(truncate=False)
```

## Đọc từng phần của ví dụ

Event_ts giữ thời gian nguồn, processed_at là thời điểm chạy. Hai cột trả lời hai câu hỏi khác nhau.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Event time vẫn năm 2025; processing time theo lần chạy thực tế, không có số thời gian cố định.

## Ba câu kiểm tra hiểu bài

1. Processing time có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: thời gian hệ thống xử lý.
- Luồng chính: Event_ts giữ thời gian nguồn, processed_at là thời điểm chạy. Hai cột trả lời hai câu hỏi khác nhau.
- Đối chiếu tiêu chí: Event time vẫn năm 2025; processing time theo lần chạy thực tế, không có số thời gian cố định. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
