# Ngày 109 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Môi trường API; không cần khởi động HTTP server để dùng TestClient. Cách cài: `python -m pip install -r requirements-api.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 109 --example
```

Giải thích đoạn chính: Fixture key chỉ dành test giả lập trong process. Ensure_demo_model train trước API; lifespan không gọi fit.

## Bước 3 — Thay đổi và tự làm

1. Dùng artifact bài làm ngày 78 thay demo qua COURSE_MODEL_PATH.
2. Khởi động tiến trình mới, kiểm tra ready và score khớp gọi trực tiếp.
3. Thử thiếu model: health còn sống, ready/predict trả 503.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 109
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Fixture key chỉ dành test giả lập trong process. Ensure_demo_model train trước API; lifespan không gọi fit.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có score model thật và version; không train trong endpoint; missing artifact không được giả vờ ready.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Có score model thật và version; không train trong endpoint; missing artifact không được giả vờ ready.

Đầu ra mẫu: `artifacts/full/day-109/example/`; bài làm: `artifacts/full/day-109/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
