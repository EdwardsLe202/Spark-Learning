# Ngày 53 — Watermark và tiến độ thời gian sự kiện

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Watermark và tiến độ thời gian sự kiện”. Kết quả cần đạt: Có progress eventTime và giải thích thứ tự batch; không áp một số dòng sink cố định ở lượt đầu.

## Từ mới gắn với bài này

- **Watermark (mốc tiến độ theo thời gian sự kiện)**.
- **State (trạng thái giữ giữa các batch)**.

## Tình huống và cách hiểu

**Watermark (mốc tiến độ theo thời gian sự kiện)** giúp quản lý **state (trạng thái giữ giữa các batch)** và chính sách dữ liệu trễ. Nó dựa vào tiến độ event time quan sát được, không đơn giản là đồng hồ hiện tại trừ 10 phút.

Cần nhiều lượt dữ liệu để quan sát mốc tiến. Đừng đòi một bản ghi muộn chắc chắn bị loại ngay trong batch đầu. Điều kiện bảo đảm nhận/loại và lúc dọn state phụ thuộc phép toán, watermark đã tiến tới đâu và query.

Ví dụ khởi tạo một stream có watermark và tổng hợp cửa sổ. Progress chứa eventTime để bạn ghi số thực tế. Đầu ra append có thể chưa có cửa sổ đóng; file rỗng chưa tự chứng minh mất dữ liệu.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-053/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
path = stream_workspace(out)
write_stream_file(path, "a.json", [{"event_id": "a", "event_time": "2025-01-01T10:00:00Z", "value": 1}])
source = file_stream(spark, path).withColumn("event_ts", F.to_timestamp("event_time"))
result = source.withWatermark("event_ts", "10 minutes").groupBy(F.window("event_ts", "5 minutes")).agg(F.sum("value").alias("total"))
query = result.writeStream.format("parquet").outputMode("append").option("path", str(path / "output")).option("checkpointLocation", str(path / "checkpoint")).trigger(availableNow=True).start()
query.awaitTermination()
print((query.lastProgress or {}).get("eventTime", {}))
```

## Đọc từng phần của ví dụ

Thêm timestamp trước withWatermark. Query append chỉ ghi kết quả khi điều kiện hoàn tất cửa sổ được đáp ứng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có progress eventTime và giải thích thứ tự batch; không áp một số dòng sink cố định ở lượt đầu.

## Ba câu kiểm tra hiểu bài

1. Watermark có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mốc tiến độ theo thời gian sự kiện.
- Luồng chính: Thêm timestamp trước withWatermark. Query append chỉ ghi kết quả khi điều kiện hoàn tất cửa sổ được đáp ứng.
- Đối chiếu tiêu chí: Có progress eventTime và giải thích thứ tự batch; không áp một số dòng sink cố định ở lượt đầu. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
