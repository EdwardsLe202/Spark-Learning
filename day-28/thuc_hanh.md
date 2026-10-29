# Ngày 28 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 28 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Hai nhánh tổng 1100000. Có thời gian đo thật; không bắt buộc cache nhanh hơn.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Chạy một lượt làm nóng rồi đo ba lần không cache.
2. Đo riêng chi phí cache.count và ba lần đọc lại, cuối cùng unpersist.
3. Lưu từng runtime, cấu hình máy và cùng kết quả tổng tiền.
4. Viết vì sao dữ liệu này chưa đủ để kết luận tốc độ ở quy mô lớn.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 28
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Có thể dùng vòng for ba lần và perf_counter; đừng chỉ đo tạo DataFrame.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
from time import perf_counter
completed = orders.filter(F.col("status") == "completed")
completed.count()
for _ in range(3):
    start = perf_counter()
    total = completed.agg(F.sum("amount")).first()[0]
    print(total, perf_counter() - start)
# Làm nhánh cache tương tự, ghi riêng thời gian vật hóa và unpersist sau cùng.
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Có bảng ba lần đo mỗi nhánh, cùng kết quả và nêu đúng giới hạn của thí nghiệm.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-28/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
