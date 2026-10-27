# Ngày 132 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Bộ AI và embedding model thật đã tải vào cache của khóa. Cách cài: `python -m pip install -r requirements-ai.txt`

Tải chủ động trước khi chạy: `python scripts/download_course_models.py embedding`. Ví dụ dùng model thật; chưa tải thì phần đó chưa nghiệm thu, không thay bằng dữ liệu giả rồi báo đã chạy.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 132 --example
```

Giải thích đoạn chính: Đây là dense model thật; filter trước ranking. Top-k có thể gồm nhiều chunk cùng doc, cần gộp doc khi chấm nhãn doc.

## Bước 3 — Thay đổi và tự làm

1. Chạy câu theo mã/thuật ngữ và câu paraphrase, lưu kết quả.
2. Thử query tự nhận admin và kiểm tra internal không vào candidates.
3. Tạo corpus vector index, so với reference helper theo cùng metric.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 132
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Đây là dense model thật; filter trước ranking. Top-k có thể gồm nhiều chunk cùng doc, cần gộp doc khi chấm nhãn doc.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có score embedding thật; không có doc sai quyền trong top-k.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Có score embedding thật; không có doc sai quyền trong top-k.

Đầu ra mẫu: `artifacts/full/day-132/example/`; bài làm: `artifacts/full/day-132/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
