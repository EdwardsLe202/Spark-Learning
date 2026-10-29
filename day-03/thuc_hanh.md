# Ngày 03 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py)

**Trước khi chạy mẫu:** mở [cài đặt cơ bản](../docs/CAI_DAT.md) và làm lần lượt các bước. Đây là ngày dành riêng cho cài đặt.

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, tự dự đoán số dòng hoặc giá trị chính trước khi chạy. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, dùng uv run để tự chọn môi trường đã cài.

```bash
uv run python scripts/run_day.py 03 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Python 3.11.x, PySpark 3.5.7, Java 17; đường dẫn Python thuộc môi trường bạn chủ động chọn.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; câu trả lời bằng lời có thể viết dưới dạng comment hoặc print.

1. Mở `docs/CAI_DAT.md`, làm theo duy nhất luồng cài cơ bản.
2. Chạy bài làm để in và kiểm tra ba phiên bản cùng đường dẫn Python thực tế.
3. Mở terminal mới ở gốc repo rồi chạy lại cùng lệnh uv run; không cần activate.
4. Nếu lỗi, ghi nguyên lệnh và phần log có nguyên nhân; chưa cần làm thêm chức năng.

Chạy file bài làm bằng:

```bash
uv run python scripts/run_day.py 03
```

**Bài làm đã hoàn thiện:** [bai_lam.py](bai_lam.py) có đầy đủ các bước trên cùng giải thích. Chạy lệnh để đối chiếu kết quả, rồi tự thử thay một giá trị nếu muốn luyện thêm.

In phiên bản và interpreter thực tế; kiểm tra Python 3.11, PySpark 3.5.7, Java 17 và môi trường Python riêng.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Nếu import thất bại, kiểm tra sys.executable trước khi cài lại. Java và Python là hai thành phần khác nhau.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
# Đây là lệnh terminal, không chép vào bai_lam.py:
# uv sync
# uv run python scripts/run_day.py 03 --example
# uv pip show --python .venv/bin/python pyspark
# java -version
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi giải thích được kết quả và xác định được phần còn vướng.

**Tiêu chí cụ thể:** Chạy lại bằng uv run ở terminal mới vẫn hiện đúng ba phiên bản, không cần cài mọi công cụ trong bản tham khảo.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-03/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
