# Ngày 15 — Ngày tháng và khoảng thời gian

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Đổi chuỗi ngày sang date và lọc một khoảng có biên rõ ràng.

## 1. Chuỗi ngày và ngày thật

**Date (kiểu ngày lịch)** cho biết năm, tháng, ngày để thực hiện phép toán theo lịch. Cột order_date hiện là string. `F.to_date("order_date", "yyyy-MM-dd")` chuyển chuỗi như 2025-01-03 thành ngày. Một chuỗi sai như not-a-date cần được nhận diện, không mặc định là ngày hiện tại.

Ta giữ order_date gốc và thêm order_day. Cách này giống giữ amount_raw ở ngày 13. Kiểm tra schema để thấy order_day là date; show có thể in hai kiểu trông giống nhau nên chỉ nhìn chữ chưa đủ.

## 2. Chọn rõ mốc đầu và cuối

**Inclusive / exclusive (bao gồm / loại trừ mốc biên)** mô tả dòng ở đúng ngày ranh giới có được giữ không. Khoảng `[2025-01-03, 2025-01-06)` lấy từ ngày 3 trở đi và trước ngày 6: ngày 3,4,5. Điều kiện dùng >= ở đầu và < ở cuối.

Trong nguồn: O002/O003 ngày 3, O004 ngày 4, O005/O006 ngày 5. Có 5 đơn. O007 ngày 6 bị loại dù chỉ cách một ngày. Nếu bạn chỉ cần completed trong khoảng này, phải thêm điều kiện trạng thái; đó là một yêu cầu khác.

## 3. Giới hạn hôm nay

Ngày lịch chưa có giờ và múi giờ như timestamp. Chúng ta chưa tính các cửa sổ giờ hay dữ liệu đến muộn. Hôm nay chỉ chuyển kiểu, lọc biên và kiểm tra bằng vài mã đơn.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
dated = orders.withColumn("order_day", F.to_date("order_date", "yyyy-MM-dd"))
result = dated.filter((F.col("order_day") >= F.lit("2025-01-03").cast("date")) & (F.col("order_day") < F.lit("2025-01-06").cast("date")))
result.select("order_id", "order_day").show()
print("Số đơn:", result.count())
```

## Đọc từng phần của ví dụ

- to_date tạo cột date từ chuỗi định dạng năm-tháng-ngày.
- F.lit tạo một giá trị cố định trong biểu thức Spark; cast date làm hai phía cùng kiểu.
- Khoảng lấy 3,4,5 tháng 1 nên có năm đơn.

## Kết quả để đối chiếu

O002, O003, O004, O005, O006; tổng 5 đơn. Nguồn có 8 đơn.

## Từ mới cần nhận ra hôm nay

- **Date (kiểu ngày lịch)**.
- **Inclusive / Exclusive (bao gồm / loại trừ mốc biên)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. String và date có thể in giống nhau không?
2. Khoảng [a,b) có giữ b không?
3. Phải xem gì để biết cột đã chuyển kiểu?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Có.
2. Không.
3. printSchema.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
