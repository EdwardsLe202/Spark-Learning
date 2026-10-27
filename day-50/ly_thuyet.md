# Ngày 50 — Structured Streaming từ file hữu hạn

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Structured Streaming từ file hữu hạn”. Kết quả cần đạt: 2 dòng, tổng value=3; file input không bị sửa sau khi đã xử lý.

## Từ mới gắn với bài này

- **Structured Streaming (xử lý luồng trên bảng)**.
- **Source / Sink (nguồn / đích)**.
- **Micro-batch (lô nhỏ liên tiếp)**.

## Tình huống và cách hiểu

**Structured Streaming (xử lý luồng trên bảng)** dùng nhiều phép biến đổi DataFrame quen thuộc nhưng nguồn có thể tiếp tục xuất hiện dữ liệu. **Source / sink (nguồn / đích)** là nơi đọc và ghi. Bài dùng file JSON local để không cần Kafka.

**Micro-batch (lô nhỏ liên tiếp)** xử lý các phần dữ liệu mới. Trigger availableNow xử lý phần đang có rồi kết thúc, thuận tiện cho thí nghiệm. Schema phải tường minh; không đoán kiểu từ một stream thay đổi không kiểm soát.

Mỗi lần mẫu tạo một vùng thí nghiệm mới; trong vùng ấy file input bất biến và checkpoint được giữ. Đầu ra Parquet là sink bền vững cho lần restart sau, khác memory sink chỉ dùng xem tạm.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-050/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
path = stream_workspace(out)
write_stream_file(path, "part-1.json", [{"event_id": "a", "event_time": "2025-01-01T10:00:00Z", "value": 1}, {"event_id": "b", "event_time": "2025-01-01T10:01:00Z", "value": 2}])
progress = run_file_stream(spark, path)
print("Đầu ra:", spark.read.parquet(str(path / "output")).count())
print("Batch cuối:", progress.get("batchId") if progress else None)
```

## Đọc từng phần của ví dụ

run_file_stream chứa readStream/writeStream đầy đủ trong course_support.py. AvailableNow kết thúc, không treo vô hạn.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

2 dòng, tổng value=3; file input không bị sửa sau khi đã xử lý.

## Ba câu kiểm tra hiểu bài

1. Structured Streaming có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: xử lý luồng trên bảng.
- Luồng chính: run_file_stream chứa readStream/writeStream đầy đủ trong course_support.py. AvailableNow kết thúc, không treo vô hạn.
- Đối chiếu tiêu chí: 2 dòng, tổng value=3; file input không bị sửa sau khi đã xử lý. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
