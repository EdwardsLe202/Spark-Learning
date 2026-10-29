# Ngày 124 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Bộ AI và generator thật đã tải; cần RAM trống phù hợp. Cách cài: `python -m pip install -r requirements-ai.txt`

Tải chủ động trước khi chạy: `python scripts/download_course_models.py generator`. Ví dụ dùng model thật; chưa tải thì phần đó chưa nghiệm thu, không thay bằng dữ liệu giả rồi báo đã chạy.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 124 --example
```

Giải thích đoạn chính: Generate_text chỉ load cache đã có, không tự tải. Response có text, input/output token, thời gian và resolved revision.

## Bước 3 — Thay đổi và tự làm

1. Tải generator nếu chưa có bằng script, ghi model card/license/revision.
2. Nối validator ngày 123, test lỗi/timeout và retry hữu hạn.
3. Thêm deadline cứng bằng subprocess timeout trong bản bài làm, ghi cách hủy worker.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 124
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Generate_text chỉ load cache đã có, không tự tải. Response có text, input/output token, thời gian và resolved revision.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có output model thật và usage; parser/content được đánh giá riêng, lỗi được báo trung thực.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Có output model thật và usage; parser/content được đánh giá riêng, lỗi được báo trung thực.

Đầu ra mẫu: `artifacts/full/day-124/example/`; bài làm: `artifacts/full/day-124/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
