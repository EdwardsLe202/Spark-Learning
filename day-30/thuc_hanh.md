# Ngày 30 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 30 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Bài A: 3 đơn/750000. Bài B: 5 khách, C005=0, tổng 1100000. Bài C: O008/O005/O006/O007.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

A. Lọc đơn completed có amount >=150000; tính số đơn và tổng tiền.
B. Tạo báo cáo completed cho tất cả khách, gồm người chưa có đơn. Lưu, đọc lại và kiểm tra.
C. Chọn đơn mới nhất mỗi khách theo order_date rồi order_id; giải thích tiêu chí phụ.
D. Tự chỉ ra một lỗi bạn đã mắc, cách kiểm tra phát hiện và phần cần học tiếp.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 30
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

A quay lại ngày 08/10; B xem 16/19/20; C xem 21. Chỉ mở đáp án sau khi đã ghi code và kết quả của bạn.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
# A
selected = orders.filter((F.col("status") == "completed") & (F.col("amount") >= 150000))
assert selected.count() == 3
assert selected.agg(F.sum("amount")).first()[0] == 750000
# B: dùng lại yêu cầu dự án ngày 29, giữ C005 bằng left join.
# C
from pyspark.sql import Window
window = Window.partitionBy("customer_id").orderBy(F.col("order_date").desc(), F.col("order_id").desc())
latest = orders.withColumn("rn", F.row_number().over(window)).filter(F.col("rn") == 1)
latest.select("customer_id", "order_id").show()
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tự làm A/B/C đúng và giải thích được; có danh sách phần yếu cần ôn thay vì chỉ đánh dấu đủ 30 thư mục.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-30/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
