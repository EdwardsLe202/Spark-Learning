# Ngày 48 — Upsert bằng Delta merge

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Upsert bằng Delta merge”. Kết quả cần đạt: Ba khóa E1/E2/E3, tổng 240; có kiểm tra khóa nguồn.

## Từ mới gắn với bài này

- **Upsert (cập nhật nếu có và thêm nếu chưa)**.
- **Merge (ghép thay đổi vào bảng theo khóa)**.

## Tình huống và cách hiểu

Append vào file không tự cập nhật event_id đã tồn tại. **Upsert (cập nhật nếu có và thêm nếu chưa)** cần khóa và quy tắc chọn nguồn. **Merge (ghép thay đổi vào bảng theo khóa)** của Delta giúp biểu đạt hai trường hợp matched/not matched.

Nguồn của một lần merge phải có tối đa một dòng cho khóa theo quy tắc đã chốt. Nhiều phiên bản cùng khớp một đích cần được chuẩn hóa trước. Nếu dữ liệu có updated_at, đừng để một phiên bản cũ ghi đè bản mới.

Fixture có E1=100,E2=50; thay đổi E1=120,E3=70. Merge hai lần cùng thay đổi vẫn phải có ba khóa và tổng 240. Điều này kiểm tra tác dụng lặp của cập nhật, không bảo đảm mọi side effect ngoài bảng đều exactly once.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-048/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from delta.tables import DeltaTable
path = out / "events"
spark.createDataFrame([("E1", 100), ("E2", 50)], "event_id string, amount long").write.format("delta").mode("overwrite").save(str(path))
changes = spark.createDataFrame([("E1", 120), ("E3", 70)], "event_id string, amount long")
for _ in range(2):
    DeltaTable.forPath(spark, str(path)).alias("t").merge(changes.alias("s"), "t.event_id = s.event_id").whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
result = spark.read.format("delta").load(str(path))
result.show()
assert result.count() == 3
```

## Đọc từng phần của ví dụ

Khóa xác định dòng đích. Merge lần hai không tạo E1/E3 thêm lần nữa.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ba khóa E1/E2/E3, tổng 240; có kiểm tra khóa nguồn.

## Ba câu kiểm tra hiểu bài

1. Upsert có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: cập nhật nếu có và thêm nếu chưa.
- Luồng chính: Khóa xác định dòng đích. Merge lần hai không tạo E1/E3 thêm lần nữa.
- Đối chiếu tiêu chí: Ba khóa E1/E2/E3, tổng 240; có kiểm tra khóa nguồn. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
