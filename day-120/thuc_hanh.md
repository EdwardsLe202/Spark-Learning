# Ngày 120 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Thư viện chuẩn Python 3.11; bước dịch vụ trong lab có điều kiện riêng. Cách cài: Không cần cài thêm cho ví dụ chuẩn.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 120 --example
```

Giải thích đoạn chính: Mẫu dẫn tới các thành phần thực thi. Nghiệm thu cần chạy và đối chiếu, không kiểm tra exists đơn thuần.

## Bước 3 — Thay đổi và tự làm

1. Hoàn thiện checklist dự án 2 và hướng dẫn clean run.
2. Demo ba lỗi và rollback, truy một prediction về model/run/data/code.
3. Lưu báo cáo tải/monitoring, đánh dấu rõ local, container và phần cloud chỉ thiết kế.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 120
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Mẫu dẫn tới các thành phần thực thi. Nghiệm thu cần chạy và đối chiếu, không kiểm tra exists đơn thuần.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có hệ thống ML chạy lại được cùng bằng chứng chất lượng/vận hành, sẵn nền để học LLM/RAG.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Có hệ thống ML chạy lại được cùng bằng chứng chất lượng/vận hành, sẵn nền để học LLM/RAG.

Đầu ra mẫu: `artifacts/full/day-120/example/`; bài làm: `artifacts/full/day-120/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
