# Ngày 04 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 04 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Hiện ba đơn O001, O002, O003 và dòng `Số dòng: 3`. Thứ tự hiển thị không phải thứ tự được bảo đảm cho mọi phép xử lý.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Chạy vi_du.py bằng lệnh trong bài này, tìm đúng ba dòng đơn hàng giữa các dòng log.
2. Sao chép ba dòng rows/createDataFrame/show vào vùng tự làm của bai_lam.py.
3. Thêm O004, C002, 70000 và in lại bảng/count.
4. Đổi tên biến orders thành my_orders nhất quán; kiểm tra vẫn chạy.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 04
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Đừng đổi master hoặc cài thêm thư viện. Chỉ thêm một tuple và dùng tên biến nhất quán.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
rows = [("O001", "C001", 100000), ("O002", "C001", 200000), ("O003", "C002", 50000), ("O004", "C002", 70000)]
my_orders = spark.createDataFrame(rows, ["order_id", "customer_id", "amount"])
my_orders.show()
print(my_orders.count())  # 4
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tự thêm đơn được 4 dòng, biết phân biệt phiên làm việc và bảng.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-04/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
