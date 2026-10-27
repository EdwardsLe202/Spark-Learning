# Ngày 24 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 24 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Đầu ra hai ngày có 3 đơn, tổng 350000; thư mục ngày 1 vẫn còn sau khi ghi ngày 3.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tự viết hàm nhận day và output_root làm tham số.
2. Chạy ngày 2025-01-03 và 2025-01-05 vào đích exercise của bạn.
3. Kiểm tra mỗi ngày có 2 đơn, tổng cả hai ngày 520000.
4. Thử ngày không có dữ liệu; ghi lỗi có chủ đích, không tạo báo cáo trống rồi báo thành công.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 24
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Ngày 3 tổng 250000, ngày 5 tổng 270000. Giữ đích exercise tách với ví dụ.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
def run_day(day, output_root):
    part = orders.filter(F.col("order_date") == day)
    if part.count() == 0:
        raise ValueError("Thiếu dữ liệu cho " + day)
    part.write.mode("overwrite").parquet(str(output_root / ("order_date=" + day)))
out = ROOT / "artifacts/beginner/day-24/exercise"
run_day("2025-01-03", out)
run_day("2025-01-05", out)
loaded = spark.read.parquet(str(out))
assert loaded.count() == 4
assert loaded.agg(F.sum("amount")).first()[0] == 520000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Chạy hai ngày được 4 dòng/520000, đích ngày cũ còn và ngày thiếu bị báo rõ.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-24/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
