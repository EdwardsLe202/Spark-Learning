# Ngày 05 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 05 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** order_id/customer_id là string, amount là long; có đúng ba tên cột.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tạo lại bảng ba đơn có schema tường minh trong bai_lam.py.
2. Thêm cột status kiểu string, điền completed vào cả ba tuple.
3. In schema và tên cột, kiểm tra mỗi tuple có bốn giá trị theo đúng thứ tự.
4. Thử sai kiểu amount="abc" trên bản thử, ghi vì sao Spark từ chối; sửa về số để chương trình chạy lại.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 05
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Tên cột ở schema và số phần tử trong tuple phải khớp. Đừng chuyển mã C001 thành số.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
orders = spark.createDataFrame(
    [("O001", "C001", 100000, "completed"), ("O002", "C001", 200000, "completed"), ("O003", "C002", 50000, "completed")],
    "order_id string, customer_id string, amount long, status string",
)
orders.printSchema()
print(orders.columns)
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tự thêm cột status, đọc được schema và biết sửa một lỗi sai kiểu đơn giản.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-05/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
