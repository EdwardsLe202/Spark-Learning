# Ngày 20 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 20 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Ví dụ sai có 11 dòng, tổng 2100000; bảng khóa trùng có C001/count=2.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Tự tạo bad_customers bằng cách thêm bản C001 như mẫu.
2. Viết kiểm tra trước join: nếu có khóa count>1 thì raise ValueError.
3. Chạy với bảng sai để thấy bị chặn; chạy lại với bảng khách chuẩn.
4. Kiểm tra join chuẩn có 8 dòng và tổng 1400000.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 20
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Bạn đã biết groupBy, count, filter. ValueError là cách Python báo lỗi có chủ đích.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
duplicates = customers.groupBy("customer_id").count().filter("count > 1")
if duplicates.count() > 0:
    raise ValueError("Bảng khách có customer_id trùng; dừng trước join")
joined = orders.join(customers, "customer_id", "inner")
assert joined.count() == 8
assert joined.agg(F.sum("amount")).first()[0] == 1400000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Chặn được bảng khách trùng và giải thích được vì sao tổng sai tăng đúng 700000.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-20/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
