# Ngày 77 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Spark/Java và thư viện ML; dữ liệu feature tham chiếu đi kèm. Cách cài: `python -m pip install -r requirements-ml.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 77 --example
```

Giải thích đoạn chính: Chọn hai cột, chặn số dòng rồi mới toPandas. Memory_usage chỉ mô tả frame đã chuyển, chưa là peak RAM toàn job.

## Bước 3 — Thay đổi và tự làm

1. Thử nguồn >1000 dòng để thấy bị chặn.
2. So memory_usage với cột số và chuỗi dài ở fixture nhỏ.
3. Thiết kế nhánh khi nguồn vượt budget: sample/aggregate/export shard.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 77
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Chọn hai cột, chặn số dòng rồi mới toPandas. Memory_usage chỉ mô tả frame đã chuyển, chưa là peak RAM toàn job.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

8 dòng mẫu về driver có kiểm soát; dữ liệu lớn bị chặn trước toPandas.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** 8 dòng mẫu về driver có kiểm soát; dữ liệu lớn bị chặn trước toPandas.

Đầu ra mẫu: `artifacts/full/day-077/example/`; bài làm: `artifacts/full/day-077/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
