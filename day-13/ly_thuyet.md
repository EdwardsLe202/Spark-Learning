# Ngày 13 — Đọc số tiền sai kiểu và ghi lý do lỗi

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Cast chuỗi sang số và tách các giá trị không parse được hoặc âm.

## 1. Văn bản có thể trông giống số

**Parse (diễn giải văn bản thành kiểu mong muốn)** biến "100000" thành số 100000. **Cast (chuyển kiểu dữ liệu)** là phép chuyển dùng trong bài: `F.col("amount_raw").cast("long")`. `F.col` tạo biểu thức cột bằng tên, cùng vai trò với df["amount_raw"] đã dùng.

Các chuỗi "abc" hoặc rỗng không biểu thị số tiền hợp lệ. Để quan sát, bài này bật `spark.sql.ansi.enabled=false`: các chuỗi mẫu không chuyển được thành long sẽ cho NULL. Cấu hình khác có thể làm Spark ném lỗi; bạn không nên mặc định mọi môi trường đều xử lý y hệt.

## 2. Chuyển được sang số chưa có nghĩa hợp lệ

-10000 chuyển thành số được, nhưng bài toán đơn hàng quy định tiền không âm. **Validation (kiểm tra dữ liệu theo quy tắc)** cần kiểm tra cả cast thành công và amount >= 0. `when(...).otherwise(...)` chọn nhãn tùy điều kiện, tương tự if/else cho từng dòng bảng.

Ta tạo cột error_reason: invalid_number nếu amount NULL; negative_amount nếu âm; ok nếu đạt hai điều kiện. Nếu có nhiều quy tắc, thứ tự when quyết định lý do ưu tiên. Bài này chưa kiểm tra mọi lỗi của hệ thống thật.

## 3. Giữ nguồn để điều tra

Đặt tên amount_raw cho chuỗi gốc và amount cho số đã chuyển. Khi lỗi, bạn xem lại chuỗi ban đầu để biết sai gì. Tách dòng lỗi thành DataFrame riêng; không đổi abc thành 0 để che lỗi.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file.

```python
spark.conf.set("spark.sql.ansi.enabled", "false")
orders = spark.createDataFrame([("A", "100000"), ("B", "abc"), ("C", "-10000"), ("D", "")], "order_id string, amount_raw string")
parsed = orders.withColumn("amount", F.col("amount_raw").cast("long"))
result = parsed.withColumn("error_reason", F.when(F.col("amount").isNull(), "invalid_number").when(F.col("amount") < 0, "negative_amount").otherwise("ok"))
result.show()
```

## Đọc từng phần của ví dụ

- amount_raw được giữ để thấy văn bản gốc.
- withColumn thêm amount đã cast; when tạo nhãn kiểm tra.
- A hợp lệ; B/D lỗi số; C chuyển kiểu được nhưng âm.

## Kết quả để đối chiếu

A:100000/ok; B:NULL/invalid_number; C:-10000/negative_amount; D:NULL/invalid_number.

## Từ mới cần nhận ra hôm nay

- **Cast (chuyển kiểu dữ liệu)**.
- **Parse (diễn giải văn bản thành kiểu mong muốn)**.
- **Validation (kiểm tra dữ liệu theo quy tắc)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Chuỗi abc có nên thay thành số 0 không?
2. Cast được số âm có đủ điều kiện clean chưa?
3. Vì sao giữ amount_raw?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không, cần giữ lý do lỗi.
2. Chưa, bài này cấm số âm.
3. Để truy lại và giải thích giá trị nguồn.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
