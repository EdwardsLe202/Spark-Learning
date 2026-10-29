# Ngày 82 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Python 3.11 và bộ thư viện ML đã cố định. Cách cài: `python -m pip install -r requirements-ml.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 82 --example
```

Giải thích đoạn chính: Khóa gồm mã khách và kỳ. Recency NULL được báo chứ không tự coi là lỗi toàn bộ nguồn.

## Bước 3 — Thay đổi và tự làm

1. Tạo ba fixture sai: thiếu cột, khóa trùng, spend âm.
2. Viết validate chặn đúng từng lỗi, giữ thông báo rõ.
3. Chứng minh bước train không chạy khi validate thất bại.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 82
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Khóa gồm mã khách và kỳ. Recency NULL được báo chứ không tự coi là lỗi toàn bộ nguồn.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Nguồn chuẩn 120 dòng; các fixture sai bị chặn trước train.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Nguồn chuẩn 120 dòng; các fixture sai bị chặn trước train.

Đầu ra mẫu: `artifacts/full/day-082/example/`; bài làm: `artifacts/full/day-082/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
