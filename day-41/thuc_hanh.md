# Ngày 41 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Môi trường Spark ngày 03; PySpark 3.5.7 và Java 17. Cách cài: `python -m pip install -r requirements.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 41 --example
```

Giải thích đoạn chính: from_json parse chuỗi theo schema. C001 sinh hai dòng; C002 mảng rỗng không có dòng từ explode.

## Bước 3 — Thay đổi và tự làm

1. Thêm payload có items=NULL và so explode/explode_outer.
2. Ghi số dòng trước sau từng biến thể.
3. Mô tả cách tránh nhân tổng tiền đơn khi chuyển sang cấp sản phẩm.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 41
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

from_json parse chuỗi theo schema. C001 sinh hai dòng; C002 mảng rỗng không có dòng từ explode.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Ví dụ có hai dòng item a/b của C001; phân biệt mất dòng với dữ liệu nguồn bị xóa.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Ví dụ có hai dòng item a/b của C001; phân biệt mất dòng với dữ liệu nguồn bị xóa.

Đầu ra mẫu: `artifacts/full/day-041/example/`; bài làm: `artifacts/full/day-041/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
