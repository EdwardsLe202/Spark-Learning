# Ngày 32 — Theo dõi job stage task trong Spark UI

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Theo dõi job stage task trong Spark UI”. Kết quả cần đạt: Ba nhóm đều count=40; có ghi chép thực tế từ UI, không yêu cầu số stage cố định.

## Từ mới gắn với bài này

- **Job (công việc thực thi)**.
- **Stage (giai đoạn thực thi)**.
- **Task (tác vụ xử lý một partition)**.

## Tình huống và cách hiểu

**Job (công việc thực thi)** phát sinh khi Spark cần kết quả. Nó có thể chia thành **stage (giai đoạn thực thi)**, mỗi stage gồm các **task (tác vụ xử lý một partition)**. Những tên này mô tả tổ chức công việc, không phải ba bảng dữ liệu khác nhau.

Một groupBy thường cần gom cùng khóa từ nhiều phần dữ liệu nên có ranh giới shuffle. Một action không bắt buộc luôn tương ứng đúng một job trong mọi cấu hình, đặc biệt khi có các bước thích nghi. Hôm nay ghi số thực tế trên UI thay vì thuộc một con số.

UI chỉ tồn tại khi ứng dụng còn sống. File mẫu không tự chờ vô hạn; khi làm lab, thêm input trong khối with để giữ phiên. Khi xem xong nhấn Enter để stop. Không dùng các số đo local để khẳng định tốc độ cluster.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-032/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
df = spark.range(120, numPartitions=4).withColumn("key", F.col("id") % 3)
result = df.groupBy("key").count()
print("UI:", spark.sparkContext.uiWebUrl)
result.show()
print("Thêm input vào bài làm để quan sát UI trước khi stop.")
```

## Đọc từng phần của ví dụ

Bốn partition nguồn tạo việc song song; groupBy gom ba khóa. URL chỉ mở được lúc phiên còn sống.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ba nhóm đều count=40; có ghi chép thực tế từ UI, không yêu cầu số stage cố định.

## Ba câu kiểm tra hiểu bài

1. Job có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: công việc thực thi.
- Luồng chính: Bốn partition nguồn tạo việc song song; groupBy gom ba khóa. URL chỉ mở được lúc phiên còn sống.
- Đối chiếu tiêu chí: Ba nhóm đều count=40; có ghi chép thực tế từ UI, không yêu cầu số stage cố định. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 03 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
