# Ngày 58 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Môi trường Spark ngày 03; PySpark 3.5.7 và Java 17. Cách cài: `python -m pip install -r requirements.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 58 --example
```

Giải thích đoạn chính: Hàm kiểm tra khoảng quan sát trước khi tạo nhãn. Cutoff tháng 7 này cần thấy giữa tháng 8 nhưng nguồn chưa đủ.

## Bước 3 — Thay đổi và tự làm

1. Tự viết nhãn bằng danh sách khách có event tương lai và left join.
2. Đối chiếu tiny: C001=0, C002/C003=1.
3. Viết ca thiếu nguồn và kiểm tra không tự gán 1.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 58
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Hàm kiểm tra khoảng quan sát trước khi tạo nhãn. Cutoff tháng 7 này cần thấy giữa tháng 8 nhưng nguồn chưa đủ.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Cutoff 2025-07-15 bị từ chối; nhãn tiny đúng 0/1/1.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Cutoff 2025-07-15 bị từ chối; nhãn tiny đúng 0/1/1.

Đầu ra mẫu: `artifacts/full/day-058/example/`; bài làm: `artifacts/full/day-058/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
