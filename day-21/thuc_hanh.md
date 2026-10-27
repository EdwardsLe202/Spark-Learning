# Ngày 21 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 21 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** C001→O008; C002→O005; C003→O006; C004→O007. ranked có 8 dòng, latest có 4.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tự viết chọn đơn mới nhất như mẫu.
2. Đổi desc thành asc ở cả hai cột để chọn đơn sớm nhất mỗi khách.
3. Kiểm tra C001→O001, C002→O003, C003→O004, C004→O007.
4. Ghi sự khác nhau giữa giữ mới nhất và loại bản trùng hoàn toàn.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 21
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Không cần max rồi join lại. Chỉ đổi thứ tự, đánh row_number và giữ rn=1.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
from pyspark.sql import Window
window = Window.partitionBy("customer_id").orderBy(F.col("order_date").asc(), F.col("order_id").asc())
first_orders = orders.withColumn("rn", F.row_number().over(window)).filter(F.col("rn") == 1)
first_orders.select("customer_id", "order_id").show()
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tự chọn được đơn đầu và cuối, giải thích đúng bước nào giảm số dòng.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-21/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
