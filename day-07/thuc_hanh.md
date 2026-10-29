# Ngày 07 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 07 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** result có order_id, amount_vnd và 8 dòng; orders vẫn có 5 cột.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Chọn customer_id, order_date, amount từ bảng nguồn.
2. Đổi tên amount thành money_vnd trong kết quả này.
3. In tên cột và số dòng của cả nguồn lẫn kết quả; giải thích phần nào đổi.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 07
```

**Bài làm đã hoàn thiện:** [bai_lam.py](bai_lam.py) có đầy đủ các bước trên cùng giải thích. Chạy lệnh để đối chiếu kết quả, rồi tự thử thay một giá trị nếu muốn luyện thêm.

Chọn customer_id/order_date/money_vnd; bảng kết quả có 3 cột và 8 dòng, nguồn vẫn có 5 cột và 8 dòng.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Dùng orders["amount"].alias("money_vnd") bên trong select; không cần vòng lặp từng đơn.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
result = orders.select("customer_id", "order_date", orders["amount"].alias("money_vnd"))
result.show()
print(result.columns)  # customer_id, order_date, money_vnd
print(result.count())  # 8
print(orders.columns)  # nguồn vẫn 5 cột
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Tự chọn ba cột, đổi tên tiền và xác nhận số dòng không đổi.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-07/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
