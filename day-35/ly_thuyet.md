# Ngày 35 — Lineage broadcast và task retry

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Lineage broadcast và task retry”. Kết quả cần đạt: Có Hà Nội, Đà Nẵng, chưa biết; giải thích được lineage không thay backup nguồn.

## Từ mới gắn với bài này

- **Lineage (quan hệ nguồn gốc phép tính)**.
- **Broadcast variable (biến chỉ đọc phân phối tới task)**.
- **Side effect (tác động ra hệ thống ngoài)**.

## Tình huống và cách hiểu

**Lineage (quan hệ nguồn gốc phép tính)** cho Spark biết cách tính lại một phần dữ liệu từ các bước và nguồn còn tồn tại. Nó không giúp khôi phục nội dung nguồn đã bị xóa hoặc thay đổi ngoài kiểm soát.

**Broadcast variable (biến chỉ đọc phân phối tới task)** phù hợp một bảng tra cứu nhỏ. Accumulator hỗ trợ thống kê nhưng không nên dùng làm sổ cái giao dịch. **Side effect (tác động ra hệ thống ngoài)** như gửi tin hoặc gọi API ghi dữ liệu có thể lặp khi task thử lại.

Trong lab chỉ in và xử lý dictionary nhỏ, không gửi gì ra ngoài. Với hành động thật cần khóa idempotency hoặc thiết kế giao dịch ở bên nhận. Biết task có thể retry quan trọng hơn việc nhớ cấu hình tăng số retry.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-035/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
lookup = spark.sparkContext.broadcast({"HN": "Hà Nội", "DN": "Đà Nẵng"})
items = spark.sparkContext.parallelize(["HN", "DN", "OTHER"], 2)
print(items.map(lambda key: lookup.value.get(key, "chưa biết")).collect())
lookup.destroy()
```

## Đọc từng phần của ví dụ

Dictionary nhỏ được phát để đọc; destroy giải phóng sau dùng. Chưa có tác động ghi tới hệ thống ngoài.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có Hà Nội, Đà Nẵng, chưa biết; giải thích được lineage không thay backup nguồn.

## Ba câu kiểm tra hiểu bài

1. Lineage có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: quan hệ nguồn gốc phép tính.
- Luồng chính: Dictionary nhỏ được phát để đọc; destroy giải phóng sau dùng. Chưa có tác động ghi tới hệ thống ngoài.
- Đối chiếu tiêu chí: Có Hà Nội, Đà Nẵng, chưa biết; giải thích được lineage không thay backup nguồn. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 08 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
