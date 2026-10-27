# Ngày 12 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 12 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Trước 3, sau 2, tổng 300000. Không tuyên bố dropDuplicates theo khóa luôn chọn đúng phiên bản.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Tự tạo lại bảng mẫu và loại trùng toàn dòng.
2. Thêm đơn O003 của cùng khách cũ theo một bảng bạn tạo; giải thích vì sao mã đơn mới không tự là duplicate.
3. Tạo hai dòng cùng order_id nhưng amount khác nhau. Viết vào ghi chú vì sao chưa thể tự chọn đúng bản chỉ từ khóa.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 12
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Bài 3 cần giải thích, không yêu cầu một lệnh chọn phiên bản mà bạn chưa học.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
orders = spark.createDataFrame([("O001", 100000), ("O001", 100000), ("O002", 200000)], "order_id string, amount long")
clean = orders.distinct()
clean.show()
print(clean.count())  # 2
# Cùng mã nhưng tiền khác cần thêm quy tắc, ví dụ thời gian cập nhật; không chọn tùy ý.
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Loại đúng bản lặp hoàn toàn và nhận ra trường hợp cần quy tắc chọn phiên bản.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-12/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
