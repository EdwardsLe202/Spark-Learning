# Ngày 06 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 06 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** 8 đơn, 5 cột. amount là long; order_date vẫn là string; O004 có status=cancelled.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Mở orders.csv bằng trình soạn thảo và tìm dòng tên cột.
2. Chạy ví dụ, tìm O004 và mô tả trạng thái của nó.
3. Trong bai_lam.py, in tên cột và số đơn. Viết vào ghi chú file có bao nhiêu dòng vật lý nếu tính cả header.
4. Đổi đường dẫn sang tên file không tồn tại trên bản thử để nhận ra lỗi đường dẫn; sửa lại sau đó.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 06
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Dữ liệu có 8 dòng, nhưng file có 9 dòng nếu tính cả dòng tên cột.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
print(orders.columns)
print(orders.count())  # 8
orders.show(truncate=False)
# O004 bị hủy; CSV có 9 dòng tính cả header.
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Đọc được CSV đúng 8 dòng, tìm thấy O004, biết đâu là đường dẫn và đâu là tên cột.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-06/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
