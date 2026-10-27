# Ngày 17 — Viết lại phép tính bằng Spark SQL

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Tạo tên bảng tạm và đối chiếu SQL với DataFrame API.

## 1. Dùng SQL đã quen

**Spark SQL (giao diện truy vấn SQL của Spark)** cho phép bạn viết SELECT, WHERE, GROUP BY trên bảng Spark. **Temporary view (bảng nhìn tạm trong phiên)** đặt tên cho DataFrame: `orders.createOrReplaceTempView("orders_view")`. Tên này giúp câu SQL tìm được bảng trong phiên hiện tại; nó chưa phải tạo một cơ sở dữ liệu bền vững trên máy.

`spark.sql("...")` trả DataFrame giống kết quả của các phép biến đổi trước đó. Vì vậy bạn vẫn gọi show, count hoặc write trên nó. Viết SQL không làm dữ liệu tự chuyển về pandas.

## 2. Đối chiếu hai cách diễn đạt

Câu `WHERE status = 'completed'` cùng ý nghĩa với filter đã học. GROUP BY customer_id cùng ý nghĩa với groupBy. SUM(amount) cùng ý nghĩa F.sum. **Order by (sắp xếp dòng theo cột)** giúp xem kết quả theo khóa. Để so fixture nhỏ dễ đọc, dùng ORDER BY customer_id hoặc `orderBy("customer_id")`; không dựa vào thứ tự xuất hiện tình cờ.

Khi so sánh kết quả, trước tiên kiểm tra tên cột và kiểu, rồi các giá trị theo khóa. Bài này không yêu cầu thuộc mọi cú pháp SQL; hãy dùng kinh nghiệm SQL của bạn để kiểm tra một phép tính Spark quen.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
orders.createOrReplaceTempView("orders_view")
result = spark.sql("""
    SELECT customer_id, SUM(amount) AS total_amount
    FROM orders_view
    WHERE status = 'completed'
    GROUP BY customer_id
    ORDER BY customer_id
""")
result.show()
```

## Đọc từng phần của ví dụ

- createOrReplaceTempView đặt tên để SQL tham chiếu trong phiên.
- spark.sql chạy truy vấn và trả DataFrame.
- ORDER BY chỉ giúp xem cùng thứ tự khóa; tổng tiền không đổi.

## Kết quả để đối chiếu

Bốn khách theo thứ tự C001–C004, tổng lần lượt 700000, 200000, 120000, 80000.

## Từ mới cần nhận ra hôm nay

- **Temporary view (bảng nhìn tạm trong phiên)**.
- **Spark SQL (giao diện truy vấn SQL của Spark)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Spark SQL có trả DataFrame không?
2. Temp view có phải lưu file không?
3. Vì sao sắp xếp trước khi so hai list dòng?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Có.
2. Không; nó đặt tên trong phiên.
3. Vì thứ tự dòng chưa được bảo đảm nếu không orderBy.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
