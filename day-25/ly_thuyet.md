# Ngày 25 — Chạy lại không làm nhân dữ liệu

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Chứng minh cùng đầu vào chạy hai lần không thêm bản ghi và cập nhật đúng ngày khi nguồn đổi.

## 1. Chạy lại là việc thường gặp

Chương trình có thể bị dừng, nguồn đến muộn hoặc bạn muốn sửa logic cho ngày cũ. **Idempotency (tính lũy đẳng khi chạy lại)** trong lab nghĩa là cùng nguồn và ngày được xử lý lại vẫn cho cùng trạng thái đầu ra, không nhân số đơn.

Giữ cách tính đầy đủ một ngày từ nguồn độc lập rồi overwrite đúng đích ngày ở bài 24. Chạy ngày 3 hai lần vẫn hai đơn của ngày 3. Nếu append cùng tập lần nữa, nó có thể thành bốn dòng; Parquet không tự biết đó là cùng đơn.

## 2. Cập nhật một ngày quá khứ

**Backfill (xử lý bù dữ liệu quá khứ)** làm lại ngày cũ theo nguồn đã chọn. Khi thêm O009 ngày 3 trị giá 20000 vào một bản nguồn thử, chạy lại đầy đủ ngày 3 làm ngày này có ba đơn/270000. Ngày 1 vẫn một đơn/100000. Tổng hai ngày sau cập nhật là bốn đơn/370000.

Đây là thí nghiệm local có một chương trình ghi vào đích riêng. Nó chưa cung cấp mọi bảo đảm giao dịch khi nhiều chương trình cùng ghi hoặc khi bị ngắt giữa lúc thay file. Không gọi nó là hệ thống production hoàn chỉnh.

## 3. Đối soát trước và sau

Kiểm tra số dòng, tập order_id và tổng tiền chứ không chỉ thư mục tồn tại. Nếu nguồn thay thì nội dung đầu ra có thể đổi có chủ đích; idempotency không có nghĩa mọi đầu vào khác nhau đều trả cùng dữ liệu.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
target_root = ROOT / "artifacts/beginner/day-25/daily"
def run_day(day, source):
    part = source.filter(F.col("order_date") == day)
    part.write.mode("overwrite").parquet(str(target_root / ("order_date=" + day)))
run_day("2025-01-01", orders)
run_day("2025-01-03", orders)
run_day("2025-01-03", orders)
loaded = spark.read.parquet(str(target_root))
print("Sau chạy lại:", loaded.count(), loaded.agg(F.sum("amount")).first()[0])
```

## Đọc từng phần của ví dụ

- Nguồn orders không đọc từ đích đang overwrite.
- Lần chạy ngày 3 thứ hai thay đúng ngày 3 bằng cùng nguồn.
- Ba dòng/350000 không đổi; đây là kiểm tra thay vì chỉ tin tên hàm.

## Kết quả để đối chiếu

Ví dụ chạy lại có 3 dòng/350000. Biến thể nguồn thêm O009 ngày 3: 4 dòng/370000, ngày 1 vẫn 100000.

## Từ mới cần nhận ra hôm nay

- **Idempotency (tính lũy đẳng khi chạy lại)**.
- **Backfill (xử lý bù dữ liệu quá khứ)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Append có tự chống trùng order_id không?
2. Vì sao không overwrite ngày bằng chỉ một đơn mới?
3. Idempotency có nghĩa nguồn thay mà kết quả không được đổi không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không.
2. Sẽ mất các đơn cũ của ngày đó.
3. Không; cùng nguồn mới cần tái chạy ổn định, nguồn khác được thay kết quả theo quy tắc.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
