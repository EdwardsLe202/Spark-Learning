# Ngày 02 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python3 scripts/run_day.py 02 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Có hai đơn trong selected: O001, O002. Tổng C001 = 300000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Đổi điều kiện thành C002, dự đoán kết quả rồi chạy.
2. Giữ các đơn có amount >= 100000 và in order_id.
3. Thêm đơn O004 của C002 có amount=70000. Tính tổng toàn bảng.
4. Viết lại một phép lọc bằng vòng for thông thường.

Chạy file bài làm bằng:

```bash
python3 scripts/run_day.py 02
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Chỉ thay một điều kiện trước. Trong bài 2, dấu >= giữ cả giá trị bằng 100000.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
selected = [o for o in orders if o["customer_id"] == "C002"]
print(sum(o["amount"] for o in selected))  # 50000 trước khi thêm O004
print([o["order_id"] for o in orders if o["amount"] >= 100000])  # O001, O002
orders.append({"order_id": "O004", "customer_id": "C002", "amount": 70000})
print(sum(o["amount"] for o in orders))  # 420000
selected = []
for order in orders:
    if order["customer_id"] == "C001":
        selected.append(order)
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Tự lọc C002 được 50000 và thêm O004 tính được tổng 420000 bằng Python.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-02/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
