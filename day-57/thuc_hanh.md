# Ngày 57 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Môi trường Spark ngày 03; PySpark 3.5.7 và Java 17. Cách cài: `python -m pip install -r requirements.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 57 --example
```

Giải thích đoạn chính: Hàm lọc thời gian trước tổng hợp, left join khách và thêm snapshot_date. Hai assert kiểm tra đủ đối tượng và khóa.

## Bước 3 — Thay đổi và tự làm

1. Tự triển khai hàm nhận events/customers/cutoff, không gọi helper trong bài làm.
2. Trên tiny và C001/C002/C003: kiểm tra count/spend/recency.
3. Chèn sự kiện tương lai rồi chứng minh feature không đổi.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 57
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Hàm lọc thời gian trước tổng hợp, left join khách và thêm snapshot_date. Hai assert kiểm tra đủ đối tượng và khóa.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

120 dòng trên nguồn đầy đủ. Tiny: C001=2/300000/12 ngày; C002=1/50000/17; C003=0/0/NULL.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** 120 dòng trên nguồn đầy đủ. Tiny: C001=2/300000/12 ngày; C002=1/50000/17; C003=0/0/NULL.

Đầu ra mẫu: `artifacts/full/day-057/example/`; bài làm: `artifacts/full/day-057/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
