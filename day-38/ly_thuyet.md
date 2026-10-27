# Ngày 38 — Broadcast join và sort merge join

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Broadcast join và sort merge join”. Kết quả cần đạt: Cùng 8 đơn/1400000; ghi plan thực tế thay vì yêu cầu một loại join cố định.

## Từ mới gắn với bài này

- **Broadcast join (ghép bằng phát bảng nhỏ)**.
- **Sort merge join (ghép bằng sắp xếp và trộn)**.

## Tình huống và cách hiểu

**Broadcast join (ghép bằng phát bảng nhỏ)** có thể giảm việc trao đổi bảng lớn khi bảng tham chiếu đủ nhỏ. **Sort merge join (ghép bằng sắp xếp và trộn)** thường cần dữ liệu phân phối và sắp theo khóa. Loại thực tế còn phụ thuộc điều kiện join và thống kê.

F.broadcast là gợi ý, không làm một bảng quá lớn tự vừa RAM. So hai kế hoạch với cùng quan hệ khóa và cùng kết quả. Với fixture nhỏ, Spark có thể tự broadcast rồi nên hai plan trông gần nhau là hợp lệ.

Không chọn kỹ thuật chỉ vì tên nghe nhanh. Nếu muốn so baseline sort merge, có thể tạm giảm ngưỡng broadcast trong bài làm rồi phục hồi cấu hình. Ghi rõ thay đổi, không để ảnh hưởng các phép đo khác.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-038/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
small = spark.createDataFrame([("C001", "vip"), ("C002", "normal")], "customer_id string, tier string")
regular = orders.join(small, "customer_id", "left")
hinted = orders.join(F.broadcast(small), "customer_id", "left")
regular.explain()
hinted.explain()
assert regular.count() == hinted.count() == 8
```

## Đọc từng phần của ví dụ

Left join giữ tám đơn; gợi ý chỉ đổi cách thực thi, không đổi ý nghĩa tier.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Cùng 8 đơn/1400000; ghi plan thực tế thay vì yêu cầu một loại join cố định.

## Ba câu kiểm tra hiểu bài

1. Broadcast join có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: ghép bằng phát bảng nhỏ.
- Luồng chính: Left join giữ tám đơn; gợi ý chỉ đổi cách thực thi, không đổi ý nghĩa tier.
- Đối chiếu tiêu chí: Cùng 8 đơn/1400000; ghi plan thực tế thay vì yêu cầu một loại join cố định. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 09 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
