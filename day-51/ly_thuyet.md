# Ngày 51 — Dừng và phục hồi bằng checkpoint

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Dừng và phục hồi bằng checkpoint”. Kết quả cần đạt: Cuối cùng vẫn 2 dòng a/b, không tăng ở lượt không có file mới.

## Từ mới gắn với bài này

- **Checkpoint (trạng thái phục hồi)**.
- **Offset (vị trí tiến độ của nguồn)**.

## Tình huống và cách hiểu

**Checkpoint (trạng thái phục hồi)** ghi tiến độ nguồn và các trạng thái cần cho query. **Offset (vị trí tiến độ của nguồn)** cho hệ thống biết phần nào đã được xử lý. Không dùng một checkpoint chung cho hai query độc lập.

Lần đầu đọc file a, sau đó thêm file b tên mới và khởi động lại cùng query/checkpoint/sink. File cũ không được tính lại như dữ liệu mới. Nếu sửa hoặc xóa nguồn đã xử lý, bạn đã phá giả định của thí nghiệm.

Xóa checkpoint không phải cách sửa mọi lỗi: nó có thể làm đọc lại toàn nguồn. Một số thay đổi query không tương thích trạng thái cũ cần migration hoặc query mới có kế hoạch. Bài này chỉ restart query giữ nguyên cấu trúc.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-051/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
path = stream_workspace(out)
write_stream_file(path, "a.json", [{"event_id": "a", "event_time": "2025-01-01T10:00:00Z", "value": 1}])
run_file_stream(spark, path)
write_stream_file(path, "b.json", [{"event_id": "b", "event_time": "2025-01-01T10:01:00Z", "value": 2}])
run_file_stream(spark, path)
run_file_stream(spark, path)
loaded = spark.read.parquet(str(path / "output"))
print("Sau restart và chạy lại:", loaded.count())
```

## Đọc từng phần của ví dụ

Ba lượt query cùng checkpoint; chỉ hai file mới xuất hiện. Query kết thúc trước khi lượt tiếp theo bắt đầu.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Cuối cùng vẫn 2 dòng a/b, không tăng ở lượt không có file mới.

## Ba câu kiểm tra hiểu bài

1. Checkpoint có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: trạng thái phục hồi.
- Luồng chính: Ba lượt query cùng checkpoint; chỉ hai file mới xuất hiện. Query kết thúc trước khi lượt tiếp theo bắt đầu.
- Đối chiếu tiêu chí: Cuối cùng vẫn 2 dòng a/b, không tăng ở lượt không có file mới. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
