# Ngày 29 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 29 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** 5 dòng khách, 3 dòng vùng, cùng tổng 1100000; C005=0. Các số cụ thể ở phần lý thuyết.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Làm theo đặc tả projects/01-spark-report/README.md; tự viết luồng chính trước khi mở mẫu.
2. Ghi hai báo cáo Parquet vào đích exercise, đọc lại để xác nhận.
3. Chạy lại hai lần và xác nhận số dòng không tăng.
4. Thử bảng khách trùng C001 để thấy chương trình dừng.
5. Viết hướng dẫn chạy ngắn và giải thích vì sao phải giữ C005.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 29
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Bạn có thể chia thành hàm Python read/validate/report/write. Không cần tự tạo package phức tạp để xong dự án đầu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
# Sau khi tự tạo report và regional bằng các bước đã học:
base = ROOT / "artifacts/beginner/day-29/exercise"
report.write.mode("overwrite").parquet(str(base / "customers"))
regional.write.mode("overwrite").parquet(str(base / "regions"))
loaded = spark.read.parquet(str(base / "customers"))
assert loaded.count() == 5
assert loaded.agg(F.sum("total_amount")).first()[0] == 1100000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Hoàn thành một dự án tự chạy được, lưu/đọc lại đúng, bắt lỗi khóa và không tăng dòng khi chạy lại.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-29/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
