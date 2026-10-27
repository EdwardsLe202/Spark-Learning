# Ngày 132 — Dense retrieval có lọc quyền

[Ngày 131](../day-131/README.md) · [Lộ trình đầy đủ](../LO_TRINH_DAY_DU.md) · [Ngày 133](../day-133/README.md)

Chặng: **LLM, RAG và tool workflow**. Cần hoàn thành tiêu chí ngày 131; chưa tự làm được thì ôn đúng phần vướng trước khi đi tiếp.

## Mục tiêu nhỏ

Có score embedding thật; không có doc sai quyền trong top-k.

## Mở lần lượt

1. [Lý thuyết](ly_thuyet.md): hiểu tình huống, từ mới, dự đoán ví dụ.
2. [Thực hành](thuc_hanh.md): chạy [mẫu](vi_du.py), thử thay đổi rồi viết vào [bai_lam.py](bai_lam.py).
3. [Ghi chú](ghi_chu.md): kết quả, lỗi, câu chưa rõ; cập nhật tiến độ khi đã tự làm.

## Điều kiện chạy

Bộ AI và embedding model thật đã tải vào cache của khóa.

`python -m pip install -r requirements-ai.txt`

Tải chủ động trước khi chạy: `python scripts/download_course_models.py embedding`. Ví dụ dùng model thật; chưa tải thì phần đó chưa nghiệm thu, không thay bằng dữ liệu giả rồi báo đã chạy.

Đọc [cài đặt nâng cao](../docs/CAI_DAT_NANG_CAO.md) khi lần đầu vào chặng này. Không cài toàn bộ công cụ ngay từ ngày 01.

## Nhịp 2–3 giờ

Khoảng 15 phút ôn, 35–45 phút hiểu ví dụ, 60–90 phút chạy/thay đổi/tự viết, 15–30 phút đối chiếu. Bài tích hợp và tải model có thể cần nhiều buổi; không bỏ tiêu chí chỉ để đủ số ngày.

Ví dụ, kiểm tra cấu hình hoặc mô phỏng chưa thay bằng chứng chạy dịch vụ/model thật được yêu cầu trong lab. Khi hỏi, gửi ngày, bước, input, dự đoán và output/error cụ thể.
