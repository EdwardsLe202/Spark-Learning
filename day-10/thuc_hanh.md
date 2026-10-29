# Ngày 10 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 10 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** C001: 700000/3; C002: 200000/2; C003: 120000/1; C004: 80000/1. Tổng 1100000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Tự viết lại báo cáo theo khách mà không nhìn ví dụ.
2. Làm một báo cáo khác theo status gồm số đơn và tổng tiền.
3. Kiểm tra completed có 7 đơn/1100000, cancelled có 1 đơn/300000.
4. Giải thích một dòng của mỗi báo cáo đang biểu diễn điều gì.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 10
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Bài 2 dùng bảng orders ban đầu, groupBy("status"). Không dùng completed vì như vậy đã mất nhóm cancelled.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
result = orders.groupBy("status").agg(F.count("*").alias("order_count"), F.sum("amount").alias("total_amount"))
result.show()
# completed: 7, 1100000; cancelled: 1, 300000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Tự groupBy status được hai nhóm với số đơn và tổng tiền đúng.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-10/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
