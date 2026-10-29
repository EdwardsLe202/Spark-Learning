# Ngày 51 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Môi trường Spark ngày 03; PySpark 3.5.7 và Java 17. Cách cài: `python -m pip install -r requirements.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 51 --example
```

Giải thích đoạn chính: Ba lượt query cùng checkpoint; chỉ hai file mới xuất hiện. Query kết thúc trước khi lượt tiếp theo bắt đầu.

## Bước 3 — Thay đổi và tự làm

1. Ghi số dòng sau từng lần chạy.
2. Tạo thí nghiệm riêng với checkpoint mới, giải thích nguy cơ đọc lại.
3. Viết runbook khôi phục mà không tùy ý xóa nguồn/checkpoint.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 51
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Ba lượt query cùng checkpoint; chỉ hai file mới xuất hiện. Query kết thúc trước khi lượt tiếp theo bắt đầu.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Cuối cùng vẫn 2 dòng a/b, không tăng ở lượt không có file mới.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Cuối cùng vẫn 2 dòng a/b, không tăng ở lượt không có file mới.

Đầu ra mẫu: `artifacts/full/day-051/example/`; bài làm: `artifacts/full/day-051/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
