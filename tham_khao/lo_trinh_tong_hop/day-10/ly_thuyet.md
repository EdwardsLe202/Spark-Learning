# Ngày 10 — Lý thuyết: Pipeline tăng dần và Structured Streaming

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Chạy lại một khoảng dữ liệu không tạo trùng và thử phục hồi stream từ file.

## 1. Xử lý mới phải nghĩ tới chạy lại
**Incremental processing (xử lý tăng dần)** xử lý phần dữ liệu mới hoặc thay đổi. **Data interval (khoảng dữ liệu được xử lý)** tách khỏi thời gian chương trình thực sự chạy. **Idempotency (tính lũy đẳng khi chạy lại)** trong lab nghĩa là cùng đầu vào và khoảng xử lý tạo cùng trạng thái đầu ra, không nhân bản ghi.

Một cách đơn giản cho file local là tính lại đầy đủ một ngày rồi ghi thay đích riêng của ngày đó. Cách này không thay thế giao dịch nguyên tử của hệ thống production, nhưng dễ kiểm tra. Không đọc lười từ đúng thư mục sắp overwrite: hãy đọc từ nguồn độc lập. **Backfill (xử lý bù dữ liệu quá khứ)** cần ghi đúng ngày dữ liệu, không dùng ngày chạy hiện tại làm khóa.

## 2. Dữ liệu đến muộn và upsert
**Late-arriving data (dữ liệu đến muộn)** có event_time cũ nhưng ingested_at mới. **Upsert (cập nhật nếu có, thêm nếu chưa có)** cần khóa và quy tắc chọn bản; append vào Parquet không tự upsert. Có thể dựng lại partition đầy đủ từ nguồn hoặc dùng định dạng bảng có hỗ trợ merge. **Schema evolution (thay đổi lược đồ dữ liệu)** phải có chính sách, không tự chấp nhận mọi cột hoặc kiểu mới.

## 3. Streaming có trạng thái
**Structured Streaming (API xử lý luồng trên bảng Spark)** thường xử lý thành **micro-batch (lô rất nhỏ liên tiếp)**. **Source (nguồn)** cấp dữ liệu, **sink (đích)** nhận kết quả. **Checkpoint (trạng thái phục hồi)** lưu tiến độ và trạng thái cần thiết; mỗi truy vấn có vị trí riêng.

**Event time (thời gian sự kiện xảy ra)** khác **processing time (thời gian hệ thống xử lý)**. **Watermark (mốc giới hạn theo tiến độ thời gian sự kiện)** giúp quản lý state và chính sách trễ; không đơn giản là lấy đồng hồ hiện tại trừ một khoảng. Bảo đảm exactly-once phụ thuộc nguồn, đích và cách ghi; checkpoint không tự chống lặp tác động tới mọi API ngoài.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
df = read_events(spark, "events_tiny.csv").withColumn("event_date", F.to_date(F.to_timestamp("event_time")))
for day in ["2025-01-02", "2025-01-15", "2025-01-20", "2025-01-15"]:
    target = output_dir(10) / "daily" / f"event_date={day}"
    # Nguồn tiny độc lập với đích nên không tự overwrite nguồn đang đọc.
    df.filter(F.col("event_date") == day).drop("event_date").write.mode("overwrite").parquet(str(target))
print("Đã chạy ba ngày và chạy lại ngày 15.")
```

## Năm ý đối chiếu với lộ trình gốc

- 10.1 — Batch theo data interval, incremental load và idempotency.
- 10.2 — Late data, dedup, upsert theo khả năng của storage và xử lý schema thay đổi.
- 10.3 — Backfill, retry, checkpoint dữ liệu và kiểm tra chất lượng tại mỗi bước.
- 10.4 — Structured Streaming, micro batch, source, sink và checkpointLocation.
- 10.5 — Event time, processing time, watermark, state và giới hạn bảo đảm xử lý.

Các ý trên giữ phạm vi phần 10 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Mốc event_time khác ingested_at thế nào?
2. Vì sao checkpoint không chống trùng lời gọi API?
3. Watermark có đồng nghĩa đồng hồ hiện tại trừ 10 phút không?

## Đọc thêm từ nguồn chính thức

- [Structured Streaming guide](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
