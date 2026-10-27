# Ngày 116 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Python 3.11 và torch==2.6.0; CPU đủ cho ví dụ tensor nhỏ. Cách cài: `python -m pip install torch==2.6.0`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 116 --example
```

Giải thích đoạn chính: Không tự chọn CUDA chỉ vì tutorial dùng GPU. Download là bước riêng có tên/revision/cache rõ.

## Bước 3 — Thay đổi và tự làm

1. Cài requirements-ai, tải generator bằng script của repo khi đủ dung lượng.
2. Dùng AutoTokenizer.from_pretrained trên đường dẫn cache trong manifest; xem input_ids/token count.
3. Chạy generate tối đa 64 token trên CPU, ghi model revision và tài nguyên, không gọi mock là model thật.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 116
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Không tự chọn CUDA chỉ vì tutorial dùng GPU. Download là bước riêng có tên/revision/cache rõ.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có tokenizer/model pretrained thật và báo cáo máy; ví dụ kiểm tra thiết bị chưa thay lab inference.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Có tokenizer/model pretrained thật và báo cáo máy; ví dụ kiểm tra thiết bị chưa thay lab inference.

Đầu ra mẫu: `artifacts/full/day-116/example/`; bài làm: `artifacts/full/day-116/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
