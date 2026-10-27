# Ngày 15 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 15 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** O002, O003, O004, O005, O006; tổng 5 đơn. Nguồn có 8 đơn.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tạo order_day và xem printSchema.
2. Lọc [2025-01-05, 2025-01-07), dự đoán mã đơn rồi kiểm tra.
3. Thêm điều kiện completed và tính tổng amount của khoảng này.
4. Ghi vì sao ngày 07 không được lấy.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 15
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Ngày 5 có O005/O006, ngày 6 có O007; cả ba completed. Đừng lấy O008 ngày 7.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
dated = orders.withColumn("order_day", F.to_date("order_date", "yyyy-MM-dd"))
result = dated.filter((F.col("order_day") >= F.lit("2025-01-05").cast("date")) & (F.col("order_day") < F.lit("2025-01-07").cast("date")) & (F.col("status") == "completed"))
result.show()
print(result.agg(F.sum("amount")).first()[0])  # 350000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Lọc đúng ba đơn ngày 5–6 và tổng 350000, giải thích được biên loại ngày 7.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-15/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
