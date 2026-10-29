# Ngày 114 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Python 3.11 và torch==2.6.0; CPU đủ cho ví dụ tensor nhỏ. Cách cài: `python -m pip install torch==2.6.0`

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 114 --example
```

Giải thích đoạn chính: Cả hai model cùng kiến trúc và eval để dropout không làm phép so ngẫu nhiên. Weights_only phù hợp state_dict.

## Bước 3 — Thay đổi và tự làm

1. So train mode và eval với dropout trên cùng input.
2. Load trong tiến trình mới, so allclose.
3. Nếu tiếp tục training, lưu thêm optimizer/epoch và giải thích vì sao.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 114
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Cả hai model cùng kiến trúc và eval để dropout không làm phép so ngẫu nhiên. Weights_only phù hợp state_dict.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Output trước/sau load khớp khi eval/no_grad; phân biệt mode với gradient.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi kiểm tra lệnh, phiên bản, kết quả và xác định phần còn vướng.

**Tiêu chí cụ thể:** Output trước/sau load khớp khi eval/no_grad; phân biệt mode với gradient.

Đầu ra mẫu: `artifacts/full/day-114/example/`; bài làm: `artifacts/full/day-114/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
