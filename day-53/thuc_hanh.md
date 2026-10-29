# Ngày 53 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Môi trường Spark ngày 03; PySpark 3.5.7 và Java 17. Cách cài: `python -m pip install -r requirements.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 53 --example
```

Giải thích đoạn chính: Thêm timestamp trước withWatermark. Query append chỉ ghi kết quả khi điều kiện hoàn tất cửa sổ được đáp ứng.

## Bước 3 — Thay đổi và tự làm

1. Thêm một file event 10:30, restart đúng checkpoint để watermark tiến.
2. Sau khi ghi progress, thêm event 09:00 ở file khác và quan sát.
3. Ghi mốc thực tế, cửa sổ đóng và dữ liệu được giữ/loại; không đoán chỉ theo giờ hiện tại.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 53
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Thêm timestamp trước withWatermark. Query append chỉ ghi kết quả khi điều kiện hoàn tất cửa sổ được đáp ứng.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có progress eventTime và giải thích thứ tự batch; không áp một số dòng sink cố định ở lượt đầu.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Có progress eventTime và giải thích thứ tự batch; không áp một số dòng sink cố định ở lượt đầu.

Đầu ra mẫu: `artifacts/full/day-053/example/`; bài làm: `artifacts/full/day-053/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
