# Ngày 43 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Thư viện chuẩn Python 3.11; bước dịch vụ trong lab có điều kiện riêng. Cách cài: Không cần cài thêm cho ví dụ chuẩn.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 43 --example
```

Giải thích đoạn chính: Placeholder ? truyền dữ liệu vào SQL, không nối tùy ý thành câu lệnh. Fixture kiểm tra đầu vào database, chưa chạy Spark JDBC.

## Bước 3 — Thay đổi và tự làm

1. Chạy PostgreSQL bằng services/postgres.compose.yml và file SQL nguồn đi kèm.
2. Dùng spark.read.format("jdbc") với PostgreSQL driver, URL và user/password từ biến môi trường theo docs/CAI_DAT_NANG_CAO.md.
3. So số dòng/tổng tiền với nguồn; ghi quyền tối thiểu và phần object storage mới thiết kế.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 43
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Placeholder ? truyền dữ liệu vào SQL, không nối tùy ý thành câu lệnh. Fixture kiểm tra đầu vào database, chưa chạy Spark JDBC.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

SQLite mẫu trả O001/100000. JDBC chỉ đánh dấu xong sau khi đọc được database thật, không chỉ in cấu hình.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** SQLite mẫu trả O001/100000. JDBC chỉ đánh dấu xong sau khi đọc được database thật, không chỉ in cấu hình.

Đầu ra mẫu: `artifacts/full/day-043/example/`; bài làm: `artifacts/full/day-043/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
