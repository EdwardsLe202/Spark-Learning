# Ngày 01 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 01 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Bảng có 3 dòng dữ liệu, 3 cột; 2 mã khách khác nhau. Tổng tiền 350000; riêng C001 là 300000.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Viết một câu mô tả dòng O002.
2. Tính tiền của C002.
3. Giả sử thêm đơn O004 của C002 trị giá 70000. Bảng mới có mấy đơn, mấy khách và tổng tiền bao nhiêu?
4. Viết một câu ngắn: file đơn hàng giữ gì, còn Spark giúp làm gì?

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 01
```

**Bài làm đã hoàn thiện:** [bai_lam.py](bai_lam.py) có đầy đủ các bước trên cùng giải thích. Chạy lệnh để đối chiếu kết quả, rồi tự thử thay một giá trị nếu muốn luyện thêm.

Tổng ban đầu 350000, C001 mua 300000, C002 mua 50000; thêm O004 được 4 đơn, 2 khách và 420000 đồng.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Hãy đếm đơn theo order_id và đếm khách theo mã customer_id khác nhau. Một khách có thể mua nhiều đơn.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```text
O002: khách C001 mua đơn trị giá 200000 đồng.
C002 ban đầu mua 50000 đồng.
Thêm O004: có 4 đơn, vẫn 2 khách; tổng tiền là 420000 đồng.
File giữ dữ liệu; Spark thực hiện các yêu cầu xử lý như chọn dòng và tính tổng.
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Tự tính được 350000 và 300000, giải thích được một dòng là một đơn; không cần chạy code.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-01/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
