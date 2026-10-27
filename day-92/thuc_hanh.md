# Ngày 92 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Thư viện chuẩn Python 3.11; bước dịch vụ trong lab có điều kiện riêng. Cách cài: Không cần cài thêm cho ví dụ chuẩn.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 92 --example
```

Giải thích đoạn chính: AST chỉ xác nhận cú pháp Python, không chứng minh Airflow import hoặc task thực thi được.

## Bước 3 — Thay đổi và tự làm

1. Tạo .venv-airflow với Airflow 3.0.0 và constraints đúng Python 3.11.
2. Đặt COURSE_ROOT/COURSE_PYTHON/DAGS_FOLDER rồi chạy airflow standalone.
3. Trigger churn_pipeline, kiểm tra năm task gọi CLI thật và có prediction 120 dòng.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 92
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

AST chỉ xác nhận cú pháp Python, không chứng minh Airflow import hoặc task thực thi được.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có log/UI run DAG thật, output và interpreter đúng; không chỉ parse file.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Có log/UI run DAG thật, output và interpreter đúng; không chỉ parse file.

Đầu ra mẫu: `artifacts/full/day-092/example/`; bài làm: `artifacts/full/day-092/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
