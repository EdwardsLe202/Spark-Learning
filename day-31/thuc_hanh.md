# Ngày 31 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Môi trường Spark ngày 03; PySpark 3.5.7 và Java 17. Cách cài: `python -m pip install -r requirements.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 31 --example
```

Giải thích đoạn chính: Đọc master để biết đây là local. agg thu nhỏ tám đơn thành một dòng trước khi first lấy kết quả về Python.

## Bước 3 — Thay đổi và tự làm

1. Vẽ driver → phần thực thi → file nguồn cho báo cáo ngày 29.
2. Chỉ ra lệnh nào lấy dữ liệu về Python; giải thích kích thước đầu ra.
3. Thiết kế cùng luồng trên hai máy, ghi phần chưa kiểm chứng.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 31
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Đọc master để biết đây là local. agg thu nhỏ tám đơn thành một dòng trước khi first lấy kết quả về Python.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Master local[2], tổng 1400000. Sơ đồ phân biệt tiến trình và máy.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Master local[2], tổng 1400000. Sơ đồ phân biệt tiến trình và máy.

Đầu ra mẫu: `artifacts/full/day-031/example/`; bài làm: `artifacts/full/day-031/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
