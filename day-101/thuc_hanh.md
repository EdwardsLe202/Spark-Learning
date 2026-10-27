# Ngày 101 — Thực hành từng bước

[Lý thuyết](ly_thuyet.md) · [Ví dụ](vi_du.py) · [Tự viết](bai_lam.py) · [Ghi chú](ghi_chu.md)

## Bước 1 — Đọc đầu vào và đoán

Đọc lý thuyết, ghi số dòng/shape/trạng thái hoặc hành vi bạn dự đoán. Khi có metric/runtime, không đoán một điểm số đẹp; ghi phép đo và điều kiện cần kiểm tra.

## Bước 2 — Chạy mẫu

Điều kiện: Thư viện chuẩn Python 3.11; bước dịch vụ trong lab có điều kiện riêng. Cách cài: Không cần cài thêm cho ví dụ chuẩn.

Chạy từ gốc repo sau khi kích hoạt môi trường đúng chặng:

```bash
python scripts/run_day.py 101 --example
```

Giải thích đoạn chính: Template chỉ dùng object action nên không cấp quyền list bucket. Nếu job cần list, bổ sung quyền và prefix condition có lý do.

## Bước 3 — Thay đổi và tự làm

1. Vẽ nguồn/đích/network/service account cho môi trường bạn chọn.
2. Đặt budget/quota và kế hoạch tắt dịch vụ trước nhánh cloud.
3. Nếu không có tài khoản, nghiệm thu deployment ở Standalone; ghi cloud mới thiết kế. Nếu có, thử quyền đọc/ghi được phép và bị từ chối ngoài prefix.

Viết vào bai_lam.py hoặc thêm module/test cùng ngày. Ví dụ và bài làm dùng hai đích khác nhau để không lẫn bằng chứng.

```bash
python scripts/run_day.py 101
```

<details>
<summary>Gợi ý khi bị kẹt</summary>

Template chỉ dùng object action nên không cấp quyền list bucket. Nếu job cần list, bổ sung quyền và prefix condition có lý do.

Bắt đầu bằng một biến thể nhỏ và kiểm tra ngay. Mở vi_du.py để lấy phần khởi tạo đã chạy được; chỉ sửa phần xử lý của bước đang làm. Không cài thêm hệ thống để tránh một lỗi nhỏ chưa hiểu.

</details>

<details>
<summary>Đối chiếu sau khi đã tự thử</summary>

Có thiết kế quyền/chi phí; chỉ ghi deployed cloud khi có bằng chứng thực thi.

Ví dụ hoàn chỉnh nằm trong vi_du.py. Với biến thể cần model/dịch vụ thật, chỉ đánh dấu khi có log/output thực; AST parse, template, ranking fixture hoặc mock response chưa đủ cho phần tích hợp. Metric không được ấn định trước để ép chương trình khớp.

</details>

## Bước 4 — Nghiệm thu buổi học

- [ ] Tôi giải thích được đầu vào và phần code đang học.
- [ ] Tôi đã chạy mẫu trong môi trường đúng, ghi phần chưa chạy nếu còn thiếu.
- [ ] Tôi tự làm đủ các bước lab, có biến thể/ca lỗi và đối chiếu.
- [ ] Tôi lưu lệnh, version, kết quả và điều còn vướng trong ghi_chu.md.

**Tiêu chí cụ thể:** Có thiết kế quyền/chi phí; chỉ ghi deployed cloud khi có bằng chứng thực thi.

Đầu ra mẫu: `artifacts/full/day-101/example/`; bài làm: `artifacts/full/day-101/exercise/`. Không sửa nguồn hoặc test labels để làm đẹp kết quả. Nếu chưa đạt, thêm một buổi cho bài này thay vì đánh dấu đã học hết.
