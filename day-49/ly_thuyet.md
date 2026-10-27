# Ngày 49 — Backfill và thay đổi schema có kiểm soát

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Backfill và thay đổi schema có kiểm soát”. Kết quả cần đạt: E1 channel=NULL, E2=app; chỉ chấp nhận thay đổi đã có policy.

## Từ mới gắn với bài này

- **Schema evolution (thay đổi lược đồ)**.
- **Compatibility (tính tương thích)**.

## Tình huống và cách hiểu

**Schema evolution (thay đổi lược đồ)** có thể là thêm cột, đổi kiểu hoặc đổi ý nghĩa. **Compatibility (tính tương thích)** phải được kiểm tra với người đọc phía sau. Một cột mới có giá trị thiếu khác một cột tiền đổi đơn vị mà tên vẫn giữ.

Khi backfill, khóa ngày và version nguồn phải rõ. Không dùng schema mới để đọc dữ liệu cũ rồi âm thầm điền giá trị làm thay ý nghĩa. Định nghĩa cột bắt buộc, cột tùy chọn và chính sách dừng.

Ví dụ unionByName allowMissingColumns thêm cột channel còn thiếu ở bản cũ. Đây là phép kết hợp bảng có chủ đích, không phải lời hứa rằng mọi schema drift được phép. Ghi riêng cảnh báo trước khi ghi đích.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-049/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
old = spark.createDataFrame([("E1", 100)], "event_id string, amount long")
new = spark.createDataFrame([("E2", 200, "app")], "event_id string, amount long, channel string")
combined = old.unionByName(new, allowMissingColumns=True)
combined.show()
required = {"event_id", "amount"}
assert required <= set(combined.columns)
```

## Đọc từng phần của ví dụ

Bản cũ có channel=NULL, còn tiền giữ kiểu số nguyên và cùng đơn vị.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

E1 channel=NULL, E2=app; chỉ chấp nhận thay đổi đã có policy.

## Ba câu kiểm tra hiểu bài

1. Schema evolution có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: thay đổi lược đồ.
- Luồng chính: Bản cũ có channel=NULL, còn tiền giữ kiểu số nguyên và cùng đơn vị.
- Đối chiếu tiêu chí: E1 channel=NULL, E2=app; chỉ chấp nhận thay đổi đã có policy. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
