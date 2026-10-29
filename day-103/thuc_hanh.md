# Ngày 103 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Python 3.11 và bộ thư viện ML đã cố định. Cách cài: `python -m pip install -r requirements-ml.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 103 --example
```

Giải thích đoạn chính: Tỷ lệ thiếu là theo từng cột trên 120 dòng. Recency thiếu có thể hợp lệ theo contract, cần ngưỡng riêng.

## Bước 3 — Thay đổi và tự làm

1. Tạo ba lỗi: thiếu cột, tăng missing, dữ liệu thiếu một ngày.
2. Chốt reference window/ngưỡng/mẫu tối thiểu và hành động.
3. Kiểm tra schema lỗi chặn score, freshness không bị che bởi job status success.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 103
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Tỷ lệ thiếu là theo từng cột trên 120 dòng. Recency thiếu có thể hợp lệ theo contract, cần ngưỡng riêng.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có quality report và ba phản ứng riêng, không đồng nhất mọi cảnh báo thành drift.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Có quality report và ba phản ứng riêng, không đồng nhất mọi cảnh báo thành drift.

Đầu ra mẫu: `artifacts/full/day-103/example/`; bài làm: `artifacts/full/day-103/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
