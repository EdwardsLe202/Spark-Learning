# Ngày 94 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Python 3.11 và bộ thư viện ML đã cố định. Cách cài: `python -m pip install -r requirements-ml.txt`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 94 --example
```

Giải thích đoạn chính: Lần chạy thực hiện hôm nay nhưng dữ liệu của ngày 1/4/2025. Đích cùng snapshot được ghi thay có chủ đích.

## Bước 3 — Thay đổi và tự làm

1. Trigger DAG hai lần cùng snapshot/version, kiểm tra không tăng khóa.
2. Tạo policy max_active_runs/pool phù hợp máy.
3. Thiết kế lịch từ data_interval khi chuyển sang nguồn liên tục thật, ghi giới hạn nguồn giả lập.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 94
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Lần chạy thực hiện hôm nay nhưng dữ liệu của ngày 1/4/2025. Đích cùng snapshot được ghi thay có chủ đích.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

120 dòng mỗi lượt, cùng ngày dữ liệu; không truyền bảng lớn qua XCom.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** 120 dòng mỗi lượt, cùng ngày dữ liệu; không truyền bảng lớn qua XCom.

Đầu ra mẫu: `artifacts/full/day-094/example/`; bài làm: `artifacts/full/day-094/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
