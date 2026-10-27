# Ngày 11 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 11 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Một dòng thiếu là B; count(*)=3, count(amount)=2; tổng số tiền đã biết 100000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tạo đúng bảng A/B/C như ví dụ trong bai_lam.py.
2. Tách missing và known, in cả hai để thấy C=0 thuộc known.
3. Tạo bản filled bằng fillna amount=0, kiểm tra nguồn orders vẫn có NULL.
4. Viết một câu vì sao chưa biết tiền thì không nên mặc định coi như khách mua miễn phí.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 11
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Không lọc known bằng amount > 0, vì cách đó loại cả số 0 hợp lệ. Dùng isNotNull.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
orders = spark.createDataFrame([("A", 100000), ("B", None), ("C", 0)], "order_id string, amount long")
missing = orders.filter(orders["amount"].isNull())
known = orders.filter(orders["amount"].isNotNull())
filled = orders.fillna({"amount": 0})
missing.show()
known.show()  # A và C
filled.show()  # B thành 0 chỉ ở bảng mới
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tách đúng một dòng thiếu, giữ C=0 và giải thích được lý do không điền 0 bừa bãi.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-11/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
