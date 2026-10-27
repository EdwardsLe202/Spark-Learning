# Ngày 26 — Làm từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ hoàn chỉnh](vi_du.py) · [Chỗ tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đoán trước khi chạy

Mở ví dụ trong lý thuyết, viết dự đoán số dòng hoặc giá trị chính vào ghi_chu.md. Nếu chưa hiểu đầu vào, đọc lại bảng nhỏ. Ngày 01 không bắt buộc dùng máy.

## Bước 2 — Chạy đúng ví dụ một lần

Chạy từ thư mục gốc repo. Từ ngày 03, kích hoạt môi trường đã cài.

```bash
python scripts/run_day.py 26 --example
```

Đọc [vi_du.py](vi_du.py) và phần giải thích từng lệnh trong lý thuyết. File này là ví dụ học, không tự chứng nhận bạn đã làm bài. Nếu muốn thử sửa mẫu, sao chép phần liên quan sang bai_lam.py để giữ bản mẫu dùng đối chiếu.

**Kết quả mẫu:** Có kế hoạch và báo cáo bốn khách tổng 1100000; không yêu cầu số job/stage cố định.

## Bước 3 — Thử thay đổi rồi tự làm

Làm lần lượt trong bai_lam.py; ngày 01 trả lời trực tiếp vào ghi chú là đủ.

1. Viết lại lọc completed → nhóm status → tổng tiền, gọi explain rồi show.
2. Chỉ ra filter/groupBy là transformation; show/count/write là action.
3. So kết quả với ngày 10 để xác nhận thêm explain không đổi số liệu.
4. Bổ sung nếu muốn: giữ phiên bằng input trước stop để mở UI theo địa chỉ log.

Chạy file bài làm bằng:

```bash
python scripts/run_day.py 26
```

Khung bài làm ban đầu chỉ giúp có chỗ viết; bạn cần thêm phần xử lý được yêu cầu. Không phải mọi kết quả có sẵn trong file khung.

## Khi bí — chỉ mở một mức hỗ trợ mỗi lần

<details>
<summary>Gợi ý, chưa xem lời giải</summary>

Chỉ cần tìm Filter/Aggregate trong plan, chưa cần hiểu mọi dòng kỹ thuật.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

```python
result = orders.filter(F.col("status") == "completed").groupBy("status").agg(F.sum("amount").alias("total"))
result.explain()
result.show()  # completed, 1100000
```

Đoạn trên có thể là phần xử lý thêm vào vùng bài làm; đọc chú thích để biết đầu vào phải tạo trước. Sau khi xem, đóng nó lại và tự viết lại một biến thể. Chạy được lời giải mẫu chưa có nghĩa đã tự làm được.

</details>

## Bước 4 — Chốt buổi học

- [ ] Tôi giải thích được đầu vào và dự đoán được kết quả chính.
- [ ] Tôi đã chạy/thực hiện mẫu và hiểu từng phần đang học.
- [ ] Tôi đã làm biến thể, so với kết quả kỳ vọng và sửa chỗ sai.
- [ ] Tôi ghi được một điều hiểu thêm hoặc còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Gắn được ba thuật ngữ với code đã biết và tìm được lọc/tổng hợp trong plan.

Nếu cần ghi file thử, dùng riêng `artifacts/beginner/day-26/exercise/`. Không sửa dữ liệu nguồn trong data/beginner. Không cần thêm bài nâng cao để được sang ngày tiếp theo.
