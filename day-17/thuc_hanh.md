# Ngày 17 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 17 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Bốn khách theo thứ tự C001–C004, tổng lần lượt 700000, 200000, 120000, 80000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Viết SQL nhóm theo status, tính số đơn và tổng tiền.
2. Viết cùng phép tính bằng DataFrame API.
3. orderBy status ở hai kết quả, đối chiếu tên và giá trị.
4. Giải thích bảng tạm có còn sau khi dừng SparkSession không.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 17
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Dùng bảng nguồn đầy đủ tám đơn để có cả completed lẫn cancelled.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
orders.createOrReplaceTempView("orders_view")
sql_result = spark.sql("SELECT status, COUNT(*) AS n, SUM(amount) AS total FROM orders_view GROUP BY status ORDER BY status")
api_result = orders.groupBy("status").agg(F.count("*").alias("n"), F.sum("amount").alias("total")).orderBy("status")
sql_result.show()
api_result.show()
# Đối chiếu hai dòng status đã tính tay; chưa cần đưa bảng về Python bằng collect.
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Viết được cùng một báo cáo bằng SQL/API với hai dòng kết quả khớp nhau.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-17/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
