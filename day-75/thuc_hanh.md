# Ngày 75 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Thư viện chuẩn Python 3.11; bước dịch vụ trong lab có điều kiện riêng. Cách cài: Không cần cài thêm cho ví dụ chuẩn.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 75 --example
```

Giải thích đoạn chính: Test tháng 6 giữ riêng. Muốn thêm fold chọn cấu hình cần thêm dữ liệu đủ quan sát, không tái dùng test rồi vẫn gọi là độc lập.

## Bước 3 — Thay đổi và tự làm

1. Vẽ các cửa sổ nhãn trên trục thời gian và kiểm tra không chồng.
2. Thiết kế thêm fold trên dữ liệu giả lập mở rộng, kiểm tra observed_until.
3. Giải thích khác biệt random CV và temporal CV, đọc CrossValidator foldCol nhưng không tin nó tự kiểm tra thời gian.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 75
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Test tháng 6 giữ riêng. Muốn thêm fold chọn cấu hình cần thêm dữ liệu đủ quan sát, không tái dùng test rồi vẫn gọi là độc lập.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có protocol không dùng test để lựa chọn; mọi fold chỉ fit thống kê từ train của fold.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Có protocol không dùng test để lựa chọn; mọi fold chỉ fit thống kê từ train của fold.

Đầu ra mẫu: `artifacts/full/day-075/example/`; bài làm: `artifacts/full/day-075/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
