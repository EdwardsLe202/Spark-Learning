# Ngày 03 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

**Trước khi chạy mẫu:** mở [cài đặt cơ bản](../docs/CAI_DAT.md) và làm lần lượt các bước. Đây là ngày dành riêng cho cài đặt.

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 03 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Python 3.11.x, PySpark 3.5.7, Java 17; đường dẫn Python thuộc môi trường bạn chủ động chọn.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Mở `docs/CAI_DAT.md`, làm theo duy nhất luồng cài cơ bản.
2. Chạy ví dụ, chép ba phiên bản và đường dẫn Python vào ghi_chu.md.
3. Mở terminal mới, kích hoạt lại .venv rồi chạy cùng lệnh.
4. Nếu lỗi, ghi nguyên lệnh và phần log có nguyên nhân; chưa cần làm thêm chức năng.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 03
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Nếu import thất bại, kiểm tra sys.executable trước khi cài lại. Java và Python là hai thành phần khác nhau.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
# Đây là lệnh terminal, không chép vào bai_lam.py:
# source .venv/bin/activate
# python scripts/run_day.py 03 --example
# python -m pip show pyspark
# java -version
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Chạy lại ở terminal mới vẫn hiện đúng ba phiên bản, không cần cài mọi công cụ trong bản tham khảo.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-03/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
