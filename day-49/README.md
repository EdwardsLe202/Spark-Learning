# Ngày 49 — Backfill và thay đổi schema có kiểm soát

[Ngày 48](../day-48/README.md) · [Lộ trình đầy đủ](../LO_TRINH_DAY_DU.md) · [Ngày 50](../day-50/README.md)

Chặng: **Incremental, streaming và feature**. Cần hoàn thành tiêu chí ngày 48; chưa tự làm được thì ôn đúng phần vướng trước khi đi tiếp.

## Mục tiêu nhỏ

E1 channel=NULL, E2=app; chỉ chấp nhận thay đổi đã có policy.

## Mở lần lượt

1. [Lý thuyết](ly_thuyet.md): hiểu tình huống, từ mới, dự đoán ví dụ.
2. [Thực hành](thuc_hanh.md): chạy [mẫu](vi_du.py), thử thay đổi rồi viết vào [bai_lam.py](bai_lam.py).
3. [Ghi chú](ghi_chu.md): kết quả, lỗi, câu chưa rõ; cập nhật tiến độ khi đã tự làm.

## Điều kiện chạy

Môi trường Spark ngày 03; PySpark 3.5.7 và Java 17.

`python -m pip install -r requirements.txt`

Đọc [cài đặt nâng cao](../docs/CAI_DAT_NANG_CAO.md) khi lần đầu vào chặng này. Không cài toàn bộ công cụ ngay từ ngày 01.

## Nhịp 2–3 giờ

Khoảng 15 phút ôn, 35–45 phút hiểu ví dụ, 60–90 phút chạy/thay đổi/tự viết, 15–30 phút đối chiếu. Bài tích hợp và tải model có thể cần nhiều buổi; không bỏ tiêu chí chỉ để đủ số ngày.

Ví dụ, kiểm tra cấu hình hoặc mô phỏng chưa thay bằng chứng chạy dịch vụ/model thật được yêu cầu trong lab. Khi hỏi, gửi ngày, bước, input, dự đoán và output/error cụ thể.
