# Ngày 16 — Lưu và đọc lại kết quả Parquet

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Ghi một bảng kết quả vào đích thử riêng và đọc lại đúng số dòng.

## 1. In bảng chưa phải lưu kết quả

Show giúp nhìn dữ liệu, nhưng khi chương trình kết thúc bạn cần một nơi lưu để đọc lại. **Parquet (định dạng lưu dữ liệu theo cột)** giữ cả cấu trúc kiểu và dữ liệu, thuận tiện cho Spark đọc lại. Hôm nay không so hiệu năng CSV/Parquet trên vài dòng.

`df.write.parquet(path)` ghi dữ liệu. Với Spark, path thường là một thư mục có các tệp part-... và metadata. Đọc bằng `spark.read.parquet(path)` tại cùng thư mục; đừng mở riêng một file phần rồi cho rằng đó luôn là toàn bộ kết quả.

## 2. Ghi đè có phạm vi

**Overwrite (ghi thay thế dữ liệu ở đích)** được chọn bằng `.mode("overwrite")`. Đích trong ví dụ chỉ là `artifacts/beginner/day-16/completed`. Bạn được chạy lại và thay dữ liệu thử ở đó. Không dùng data/beginner làm đích, không ghi đè thư mục cha chứa các ngày khác.

Sau ghi, đọc lại rồi kiểm tra số dòng, schema và tổng tiền. Nếu chỉ kiểm tra thư mục tồn tại, bạn chưa biết dữ liệu ghi có đủ hay đúng không. Code ngày này chủ động ghi thay toàn bộ đích nhỏ riêng, chưa phải bảng có giao dịch quản lý cập nhật.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
target = ROOT / "artifacts" / "beginner" / "day-16" / "completed"
completed = orders.filter(F.col("status") == "completed")
completed.write.mode("overwrite").parquet(str(target))
loaded = spark.read.parquet(str(target))
print("Đọc lại:", loaded.count())
loaded.printSchema()
```

## Đọc từng phần của ví dụ

- target là thư mục đầu ra, khác thư mục nguồn.
- write ghi 7 đơn completed; read lấy lại chúng.
- loaded là DataFrame mới đọc từ Parquet, không phụ thuộc biến completed còn ở bộ nhớ.

## Kết quả để đối chiếu

Đọc lại 7 dòng, tổng amount=1100000; kiểu amount vẫn là long. CSV nguồn không thay đổi.

## Từ mới cần nhận ra hôm nay

- **Parquet (định dạng lưu dữ liệu theo cột)**.
- **Overwrite (ghi thay thế dữ liệu ở đích)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Path Parquet là một file bắt buộc không?
2. Overwrite thay ở đâu?
3. Thư mục tồn tại đã đủ chứng minh đúng chưa?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không, Spark thường ghi thư mục gồm nhiều phần.
2. Đúng đích path đã truyền.
3. Chưa; phải đọc và kiểm tra nội dung.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
