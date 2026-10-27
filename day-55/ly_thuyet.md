# Ngày 55 — ForeachBatch và chống lặp tác động ghi

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “ForeachBatch và chống lặp tác động ghi”. Kết quả cần đạt: Có đầu ra batch Parquet; giải thích được giới hạn bảo đảm source/sink/side effect.

## Từ mới gắn với bài này

- **foreachBatch (xử lý từng micro-batch bằng hàm)**.
- **Batch ID (mã lô trong một query)**.

## Tình huống và cách hiểu

**foreachBatch (xử lý từng micro-batch bằng hàm)** cho bạn dùng thao tác batch để ghi. Nó không tự biến mọi lời gọi API thành exactly once. Nếu query thử lại, hàm có thể được gọi cho lô cần khôi phục.

**Batch ID (mã lô trong một query)** có thể làm một phần khóa idempotency. Nó không phải khóa duy nhất toàn hệ thống: query mới/checkpoint mới có thể bắt đầu lại số lô. Trong bài, mỗi thí nghiệm có thư mục query riêng, mỗi batch có đích riêng.

Hàm mẫu overwrite đúng đích batch và không đọc nguồn từ đích đó. Khi ghi bảng thật hoặc API ngoài, cần transaction/ledger/upsert và khóa nghiệp vụ. Phân biệt chống lặp lô với việc cùng event bị gửi nhiều lần ở nguồn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-055/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
path = stream_workspace(out)
write_stream_file(path, "a.json", [{"event_id": "a", "event_time": "2025-01-01T10:00:00Z", "value": 1}])
def save_batch(df, batch_id):
    df.write.mode("overwrite").parquet(str(path / "batches" / ("batch=" + str(batch_id))))
query = file_stream(spark, path).writeStream.foreachBatch(save_batch).option("checkpointLocation", str(path / "checkpoint")).trigger(availableNow=True).start()
query.awaitTermination()
print("Đã ghi các batch ở", path / "batches")
```

## Đọc từng phần của ví dụ

Batch ID chỉ có nghĩa trong vùng query này. Ghi lại cùng batch thay đúng đích thay vì append vô điều kiện.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có đầu ra batch Parquet; giải thích được giới hạn bảo đảm source/sink/side effect.

## Ba câu kiểm tra hiểu bài

1. foreachBatch có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: xử lý từng micro-batch bằng hàm.
- Luồng chính: Batch ID chỉ có nghĩa trong vùng query này. Ghi lại cùng batch thay đúng đích thay vì append vô điều kiện.
- Đối chiếu tiêu chí: Có đầu ra batch Parquet; giải thích được giới hạn bảo đảm source/sink/side effect. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
