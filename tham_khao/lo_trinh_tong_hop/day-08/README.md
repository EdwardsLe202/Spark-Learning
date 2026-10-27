# Ngày 08 — Partition shuffle và nền tảng RDD

[Ngày trước](../day-07/README.md) · [Lộ trình](../README.md) · [Ngày sau](../day-09/README.md)

Đọc được chi phí shuffle và viết một word count nhỏ bằng hai API.

## Cách học hôm nay

Dành khoảng 3–4 giờ cho phần cốt lõi: 45–60 phút đọc và giải thích lại, 90–120 phút viết/chạy/sửa, 30–45 phút kiểm tra và ghi kết quả. Phần mở rộng làm sau nếu cần học sâu hoặc có thêm thời gian. Ngày tích hợp có thể cần dùng phần thời gian dự phòng từ các ngày trước.

1. Đọc [lý thuyết](ly_thuyet.md), tự kể lại ví dụ bằng lời của bạn.
2. Làm [thực hành](thuc_hanh.md) trong [bai_lam.py](bai_lam.py). File có ví dụ khởi động và các TODO theo ngày, chưa phải lời giải toàn bộ bài.
3. Lưu bằng chứng và câu trả lời trong [ghi_chu.md](ghi_chu.md); đầu ra chạy thử ở `artifacts/day-08/`.
4. Chỉ đánh dấu xong khi kiểm tra được tiêu chí, rồi cập nhật [tiến độ](../TIEN_DO.md).

Điều kiện đầu vào: Đã xong ngày 02; môi trường nền `requirements.txt`.

## Đã hoàn thành khi

- [ ] Giải thích được khái niệm bằng ví dụ nhỏ.
- [ ] Tự viết được biến thể và chạy kiểm tra kết quả.
- [ ] Có log/kết quả, lỗi đã sửa hoặc ca lỗi đã thử.
- [ ] Trả lời được câu hỏi tự kiểm tra và ghi giới hạn của bài.
