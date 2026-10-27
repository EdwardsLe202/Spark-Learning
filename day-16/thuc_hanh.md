# Ngày 16 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 16 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Đọc lại 7 dòng, tổng amount=1100000; kiểu amount vẫn là long. CSV nguồn không thay đổi.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tự ghi bảng completed vào thư mục exercise trong artifacts/beginner/day-16.
2. Đọc lại và kiểm tra số dòng, tổng tiền, schema.
3. Chạy lại cùng chương trình và xác nhận vẫn 7 dòng.
4. Xem thư mục trong trình soạn thảo: có một hay nhiều file phần? Ghi điều thực thấy, không khẳng định mọi lần ghi luôn có cùng số file.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 16
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Dùng đích exercise riêng cho bài làm để không lẫn với ví dụ. Không tự chọn thư mục gốc repo làm đích.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
target = ROOT / "artifacts" / "beginner" / "day-16" / "exercise"
result = orders.filter(F.col("status") == "completed")
result.write.mode("overwrite").parquet(str(target))
loaded = spark.read.parquet(str(target))
assert loaded.count() == 7
assert loaded.agg(F.sum("amount")).first()[0] == 1100000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Ghi/đọc lại 7 đơn, chạy hai lần vẫn 7, nguồn không bị sửa.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-16/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
