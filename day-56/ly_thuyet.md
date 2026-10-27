# Ngày 56 — Định nghĩa entity cutoff và hai cửa sổ

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Định nghĩa entity cutoff và hai cửa sổ”. Kết quả cần đạt: Lịch sử T001/T002/T003, tổng 350000; C001=300000, C002=50000.

## Từ mới gắn với bài này

- **Entity (đối tượng dự đoán)**.
- **Cutoff (mốc chốt thông tin)**.
- **Label window (cửa sổ tương lai xác định nhãn)**.

## Tình huống và cách hiểu

**Entity (đối tượng dự đoán)** là khách hàng. **Cutoff (mốc chốt thông tin)** là lúc giả định phải đưa ra quyết định. Feature dùng [cutoff−30 ngày,cutoff), đồng thời dữ liệu phải đến trước cutoff. **Label window (cửa sổ tương lai xác định nhãn)** dùng [cutoff,cutoff+30 ngày).

Không trộn hai cửa sổ: tiền sau cutoff có thể dùng xác định nhãn nhưng không được dùng làm feature của lần dự đoán ấy. Khóa snapshot gồm customer_id và snapshot_date, vì một khách có nhiều thời điểm dự đoán.

Bắt đầu bằng tiny: T004 ngày 5/2 có tiền lớn nhưng cutoff 1/2 không được biết nó trong feature. Giữ bảng khách làm gốc để người không có giao dịch vẫn có dòng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-056/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
events = events_df(spark, "events_tiny.csv")
c = F.to_timestamp(F.lit("2025-02-01T00:00:00Z"))
history = events.filter((F.col("event_ts") >= c - F.expr("INTERVAL 30 DAYS")) & (F.col("event_ts") < c) & (F.col("available_ts") < c))
history.select("event_id", "customer_id", "amount_num").show()
print("Tổng lịch sử:", history.agg(F.sum("amount_num")).first()[0])
```

## Đọc từng phần của ví dụ

Ba điều kiện kiểm soát cửa sổ sự kiện và thông tin sẵn có. T004 không góp 900000 vào feature.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Lịch sử T001/T002/T003, tổng 350000; C001=300000, C002=50000.

## Ba câu kiểm tra hiểu bài

1. Entity có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đối tượng dự đoán.
- Luồng chính: Ba điều kiện kiểm soát cửa sổ sự kiện và thông tin sẵn có. T004 không góp 900000 vào feature.
- Đối chiếu tiêu chí: Lịch sử T001/T002/T003, tổng 350000; C001=300000, C002=50000. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 11 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
