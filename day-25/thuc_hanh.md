# Ngày 25 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 25 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Ví dụ chạy lại có 3 dòng/350000. Biến thể nguồn thêm O009 ngày 3: 4 dòng/370000, ngày 1 vẫn 100000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Tự thử chạy lại ngày 3 với overwrite, đối soát số dòng và tổng.
2. Dùng một đích append thử riêng để thấy cùng hai đơn ghi hai lần thành 4 dòng. Không dùng đích chính.
3. Thêm O009/C005/2025-01-03/20000/completed vào bản nguồn DataFrame bằng unionByName.
4. Xử lý lại đầy đủ ngày 3 từ nguồn mới, kiểm tra ngày 1 không đổi. Không ghi sửa data/beginner/orders.csv.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 25
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Nguồn mới cần cùng schema với orders. Tính lại đầy đủ ngày từ nguồn mới, không chỉ overwrite bằng riêng một đơn đến muộn.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
extra = spark.createDataFrame([("O009", "C005", "2025-01-03", 20000, "completed")], orders.schema)
new_source = orders.unionByName(extra)
# Dùng lại run_day đã viết trong ví dụ, đích thuộc bài làm của bạn:
run_day("2025-01-03", new_source)
loaded = spark.read.parquet(str(target_root))
assert loaded.count() == 4
assert loaded.agg(F.sum("amount")).first()[0] == 370000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Chứng minh được chạy lại không nhân dòng và thay đúng ngày khi thêm một đơn đến muộn.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-25/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
