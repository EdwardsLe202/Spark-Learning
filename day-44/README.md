# Ngày 44 — Delta Lake transaction và time travel

[Ngày 43](../day-43/README.md) · [Lộ trình đầy đủ](../LO_TRINH_DAY_DU.md) · [Ngày 45](../day-45/README.md)

Chặng: **Spark nâng cao**. Cần hoàn thành tiêu chí ngày 43; chưa tự làm được thì ôn đúng phần vướng trước khi đi tiếp.

## Mục tiêu nhỏ

Hiện tại 7 dòng, version trước delete 8 dòng; có history thực tế.

## Mở lần lượt

1. [Lý thuyết](ly_thuyet.md): hiểu tình huống, từ mới, dự đoán ví dụ.
2. [Thực hành](thuc_hanh.md): chạy [mẫu](vi_du.py), thử thay đổi rồi viết vào [bai_lam.py](bai_lam.py).
3. Đối chiếu kết quả, ghi giải thích bằng comment trong [bài làm](bai_lam.py) khi cần; cập nhật tiến độ khi đã tự làm.

## Điều kiện chạy

Môi trường Delta riêng/chỉ chạy query này sau khi cài connector; lần đầu cần mạng để tải JAR.

`python -m pip install -r requirements-delta.txt`

Đọc [cài đặt nâng cao](../docs/CAI_DAT_NANG_CAO.md) khi lần đầu vào chặng này. Không cài toàn bộ công cụ ngay từ ngày 01.

## Nhịp 2–3 giờ

Khoảng 15 phút ôn, 35–45 phút hiểu ví dụ, 60–90 phút chạy/thay đổi/tự viết, 15–30 phút đối chiếu. Bài tích hợp và tải model có thể cần nhiều buổi; không bỏ tiêu chí chỉ để đủ số ngày.

Ví dụ, kiểm tra cấu hình hoặc mô phỏng chưa thay bằng chứng chạy dịch vụ/model thật được yêu cầu trong lab. Khi hỏi, gửi ngày, bước, input, dự đoán và output/error cụ thể.
