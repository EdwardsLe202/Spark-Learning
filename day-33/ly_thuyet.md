# Ngày 33 — Logical plan và physical plan

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Logical plan và physical plan”. Kết quả cần đạt: Tổng completed vẫn 1100000; có hai cách viết và giải thích plan.

## Từ mới gắn với bài này

- **Logical plan (kế hoạch logic)**.
- **Physical plan (kế hoạch vật lý)**.
- **Catalyst (bộ tối ưu truy vấn Spark SQL)**.

## Tình huống và cách hiểu

**Logical plan (kế hoạch logic)** mô tả bạn muốn lọc, chọn và nhóm những gì. **Physical plan (kế hoạch vật lý)** mô tả cách thực hiện, chẳng hạn đọc file nào và dùng loại join nào. **Catalyst (bộ tối ưu truy vấn Spark SQL)** có thể rút gọn biểu thức và đẩy một số phép lọc xuống sớm.

Vì nhiều cách viết có cùng ý nghĩa, đừng chọn code chỉ từ số dòng lệnh. explain extended giúp xem các lớp kế hoạch. Bắt đầu tìm tên cột và Filter/Aggregate đã quen; chưa cần học mọi chi tiết nội bộ.

Bộ tối ưu không biết toàn bộ nghiệp vụ. Cộng đơn hủy vẫn có thể chạy rất nhanh nhưng sai. Luôn giữ kiểm tra tổng 1100000 cho báo cáo completed, trước và sau khi thử viết lại truy vấn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-033/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
result = orders.filter(F.col("status") == "completed").select("customer_id", "amount").groupBy("customer_id").agg(F.sum("amount").alias("total"))
result.explain("extended")
assert result.agg(F.sum("total")).first()[0] == 1100000
```

## Đọc từng phần của ví dụ

Extended in nhiều lớp plan. Assert bảo vệ ý nghĩa báo cáo trong lúc đọc cách Spark thực thi.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Tổng completed vẫn 1100000; có hai cách viết và giải thích plan.

## Ba câu kiểm tra hiểu bài

1. Logical plan có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: kế hoạch logic.
- Luồng chính: Extended in nhiều lớp plan. Assert bảo vệ ý nghĩa báo cáo trong lúc đọc cách Spark thực thi.
- Đối chiếu tiêu chí: Tổng completed vẫn 1100000; có hai cách viết và giải thích plan. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 09 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
