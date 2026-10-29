# Ngày 14 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 14 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Báo cáo 4 khách, tổng 1100000; đối soát số đơn 8=7+1 và tổng tiền 1400000=1100000+300000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Đóng file ví dụ, tự viết lại báo cáo trong bai_lam.py.
2. Viết thêm báo cáo cancelled và đối soát cả số đơn lẫn tiền.
3. Thử bỏ filter completed trên bản sai, chạy kiểm tra tổng để thấy lỗi bị bắt; rồi sửa lại.
4. Giải thích từng bước bằng một câu, không chỉ ghi “chạy thành công”.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 14
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Bạn đã có toàn bộ API ở ngày 06, 08, 10. Không cần học hàm mới để hoàn thành.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
completed = orders.filter(F.col("status") == "completed")
cancelled = orders.filter(F.col("status") == "cancelled")
summary = completed.groupBy("customer_id").agg(F.sum("amount").alias("total_amount"), F.count("*").alias("order_count"))
assert completed.count() + cancelled.count() == orders.count()
assert completed.agg(F.sum("amount")).first()[0] == 1100000
assert cancelled.agg(F.sum("amount")).first()[0] == 300000
summary.show()
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Tự dựng được báo cáo và chứng minh một lỗi bỏ lọc bị kiểm tra phát hiện.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-14/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
