# Ngày 19 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 19 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Báo cáo có 5 dòng, C005 total_amount=0. Anti join chỉ trả C005.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tạo báo cáo theo khách nhưng chỉ tính completed.
2. Left join với tất cả customers và điền tổng 0 cho người không có đơn hoàn tất.
3. Kiểm tra C003=120000, C005=0 và tổng báo cáo=1100000.
4. Dùng anti join tìm khách không có đơn bất kỳ; so với bảng báo cáo.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 19
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Lọc completed trước groupBy. Bảng customers phải ở bên trái để giữ C005.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
summary = orders.filter(F.col("status") == "completed").groupBy("customer_id").agg(F.sum("amount").alias("total_amount"))
result = customers.join(summary, "customer_id", "left").fillna({"total_amount": 0})
result.show()
assert result.count() == 5
assert result.agg(F.sum("total_amount")).first()[0] == 1100000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tạo báo cáo 5 khách có C005=0 và giải thích được khác biệt inner/left/anti.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-19/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
