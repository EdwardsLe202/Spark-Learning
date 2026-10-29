# Ngày 22 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 22 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** C001: O001 previous=NULL/running=100000; O002 previous=100000/running=300000; O008 previous=200000/running=700000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Viết lại ví dụ với cửa sổ tăng dần.
2. Xem riêng C002; tự tính previous_amount và running_amount.
3. Kiểm tra O003: NULL/50000; O005: 50000/200000.
4. Giải thích vì sao running total của C002 không cộng đơn C001.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 22
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

PartitionBy tách nhóm khách. Dòng đầu nhóm không có previous là hành vi đúng.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
from pyspark.sql import Window
window = Window.partitionBy("customer_id").orderBy("order_date", "order_id")
frame = window.rowsBetween(Window.unboundedPreceding, Window.currentRow)
result = orders.withColumn("previous_amount", F.lag("amount").over(window)).withColumn("running_amount", F.sum("amount").over(frame))
result.filter(F.col("customer_id") == "C002").show()
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Tính đúng hai đơn C002 và giải thích được nhóm, thứ tự, phạm vi cộng.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-22/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
