# Ngày 08 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 08 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Ví dụ giữ O002, O005, O008. Nếu chỉ lọc completed thì có 7 đơn.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Lọc riêng customer_id bằng C001: dự đoán mã đơn rồi chạy.
2. Lọc completed và amount > 150000. So với ví dụ >=, đơn nào mất đi?
3. Lọc status=cancelled và mô tả đúng đơn còn lại.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 08
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

C001 có O001, O002, O008. Khi đổi >= thành >, hãy kiểm tra đơn đúng bằng ngưỡng.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
orders.filter(orders["customer_id"] == "C001").show()  # O001, O002, O008
orders.filter((orders["status"] == "completed") & (orders["amount"] > 150000)).show()  # O002, O008
orders.filter(orders["status"] == "cancelled").show()  # O004
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tự viết hai điều kiện đúng ngoặc và giải thích được việc O005 được giữ hoặc bị loại.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-08/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
