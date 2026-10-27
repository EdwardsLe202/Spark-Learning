# Ngày 150 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Thư viện chuẩn Python 3.11; bước dịch vụ trong lab có điều kiện riêng. Cách cài: Không cần cài thêm cho ví dụ chuẩn.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 150 --example
```

Giải thích đoạn chính: Các số là trọng số rubric gốc, không là điểm tự động đã đạt. Bằng chứng từng mục do bạn điền và giải thích.

## Bước 3 — Thay đổi và tự làm

1. Tự chấm theo bằng chứng, sửa lỗi nghiêm trọng trước khi gọi hoàn thành.
2. Demo sạch 10 phút có file lỗi, retry, rollback, thiếu bằng chứng và sai quyền.
3. Trả lời câu hỏi Spark/ML/MLOps/API/RAG và ghi năm hướng học sâu tiếp theo.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 150
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Các số là trọng số rubric gốc, không là điểm tự động đã đạt. Bằng chứng từng mục do bạn điền và giải thích.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có ba dự án nghiệm thu, demo và rubric có dẫn chứng; không tự đánh dấu phần mở rộng chưa chạy.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Có ba dự án nghiệm thu, demo và rubric có dẫn chứng; không tự đánh dấu phần mở rộng chưa chạy.

Đầu ra mẫu: `artifacts/full/day-150/example/`; bài làm: `artifacts/full/day-150/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
