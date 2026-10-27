# Ngày 29 — Dự án nhỏ báo cáo doanh thu

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Tự ghép các phép đã học thành một chương trình đọc, kiểm tra, báo cáo và lưu.

## 1. Một dự án đủ nhỏ để tự hiểu toàn bộ

**Deliverable (sản phẩm bàn giao có thể kiểm tra)** là báo cáo doanh thu theo khách và vùng từ tám đơn cùng năm khách. Không thêm học máy vào dự án này. Mục tiêu là tự dựng luồng từ file tới kết quả và giải thích từng quyết định.

Yêu cầu: kiểm tra bảng khách không trùng khóa; chỉ cộng completed; giữ cả khách chưa có đơn; ghi báo cáo khách và báo cáo vùng ra Parquet; đọc lại và kiểm tra. Tất cả thao tác đã học; phần mới là tự tổ chức chúng thành một chương trình.

## 2. Chốt kết quả trước

Báo cáo khách có năm dòng: C001=700000, C002=200000, C003=120000, C004=80000, C005=0. Báo cáo vùng có HN=780000, HCM=200000, DN=120000. Cả hai tổng 1100000.

Không cộng tiền sau khi ghép customers trùng mã. Đừng bỏ C005 bằng inner join khi yêu cầu giữ tất cả khách. Ghi rõ mỗi dòng báo cáo là một khách hoặc một vùng, khác bảng nguồn mỗi dòng là một đơn.

## 3. Viết cách chạy cho chính mình ngày mai

Dùng một thư mục đầu ra riêng dưới artifacts/beginner/day-29. Viết lệnh, đầu vào, quy tắc completed, các kiểm tra và kết quả trong ghi chú. Có thể xem mẫu sau khi đã tự thử; không có yêu cầu dựng ba hệ thống cùng lúc.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
if customers.groupBy("customer_id").count().filter("count > 1").count() > 0:
    raise ValueError("Khách trùng khóa")
summary = orders.filter(F.col("status") == "completed").groupBy("customer_id").agg(F.sum("amount").alias("total_amount"))
report = customers.join(summary, "customer_id", "left").fillna({"total_amount": 0})
regional = report.groupBy("region").agg(F.sum("total_amount").alias("total_amount"))
report.orderBy("customer_id").show()
regional.show()
```

## Đọc từng phần của ví dụ

- Mẫu minh họa phần ghép báo cáo, chưa làm hết phần lưu/đọc lại của bài tự làm.
- Kiểm tra khóa trước join bảo vệ tổng tiền.
- Tổng theo vùng được tính từ báo cáo khách có khóa duy nhất.

## Kết quả để đối chiếu

5 dòng khách, 3 dòng vùng, cùng tổng 1100000; C005=0. Các số cụ thể ở phần lý thuyết.

## Từ mới cần nhận ra hôm nay

- **Deliverable (sản phẩm bàn giao có thể kiểm tra)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Vì sao dùng left join ở báo cáo khách?
2. Vì sao báo cáo vùng không bằng 1400000?
3. Cần lưu gì để ngày mai tự chạy lại?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Giữ cả khách không có đơn.
2. Chỉ tính completed, loại 300000 của đơn hủy.
3. Code, lệnh, nguồn, quy tắc và kết quả kiểm tra.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
