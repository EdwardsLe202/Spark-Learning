# Ngày 23 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 23 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Các số lần lượt 10,5,5,4,1,3; sạch O001/O002/O015, tổng amount_num=390000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Viết lại chuỗi làm sạch vào bai_lam.py theo từng bước, kiểm tra count sau mỗi bước.
2. Bổ sung error_reason cho lỗi cơ bản bằng when: thiếu khách, tiền lỗi, tiền âm, ngày lỗi.
3. Ghi clean và dữ liệu lỗi ra hai đích Parquet riêng dưới artifacts/beginner/day-23/exercise.
4. Đối soát 10=5+1+1+3 và đọc lại clean để kiểm tra tổng 390000.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 23
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Dùng lại when ngày 13, Parquet ngày 16, anti join ngày 19. Thứ tự nhãn lỗi là policy cần ghi rõ.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
# Sau khi đã tạo parsed và valid như ví dụ:
reasoned = parsed.withColumn("error_reason", F.when(F.col("customer_id").isNull() | (F.col("customer_id") == ""), "missing_customer").when(F.col("amount_num").isNull(), "invalid_number").when(F.col("amount_num") < 0, "negative_amount").when(F.col("order_day").isNull(), "invalid_date").otherwise("ok"))
reasoned.filter(F.col("error_reason") != "ok").show()
# Tạo candidates/unique/unknown/clean như phần mẫu rồi kiểm tra:
assert clean.count() == 3
assert clean.agg(F.sum("amount_num")).first()[0] == 390000
clean.write.mode("overwrite").parquet(str(ROOT / "artifacts/beginner/day-23/exercise/clean"))
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Làm được chuỗi có số dòng đối soát đúng, lưu sạch/lỗi riêng và đọc lại 390000.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-23/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
