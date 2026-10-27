# Dự án đầu tiên — Báo cáo đơn hàng

[Ngày 29](../../day-29/README.md)

Bạn phụ trách một báo cáo cho cửa hàng: mỗi khách đã mua bao nhiêu tiền ở các đơn hoàn tất, kể cả khách chưa có đơn. Sau đó tổng hợp theo vùng. Đầu vào là orders.csv và customers.csv ở data/beginner.

## Các bước đã học để dùng lại

1. Đọc file bằng schema tường minh: ngày 05–06.
2. Kiểm tra customer_id của customers không trùng: ngày 20.
3. Chọn các đơn completed và tổng hợp theo customer_id: ngày 08–10.
4. Ghép với toàn bộ khách, điền tổng 0 khi không có đơn: ngày 19.
5. Tổng hợp báo cáo khách theo region: ngày 10/18.
6. Ghi hai báo cáo, đọc lại và kiểm tra: ngày 16.

Nếu chưa viết được một bước, quay lại bài tương ứng để làm lại biến thể. Chưa cần thêm công cụ mới.

## Kết quả nghiệm thu

| Kiểm tra | Kỳ vọng |
| --- | --- |
| Orders nguồn | 8 dòng, tổng 1400000 |
| Đơn completed | 7 dòng, tổng 1100000 |
| Báo cáo khách | 5 dòng, customer_id duy nhất |
| Tổng theo C001/C002/C003/C004/C005 | 700000 / 200000 / 120000 / 80000 / 0 |
| Báo cáo vùng | 3 dòng, HN=780000 / HCM=200000 / DN=120000 |
| Đọc lại Parquet | Cùng số dòng và tổng |
| Chạy lại cùng nguồn | Không tăng dòng |
| Thử bảng khách trùng C001 | Dừng với lỗi rõ ràng trước join |

## Nơi tự viết

Làm trong day-29/bai_lam.py. Đầu ra riêng ở artifacts/beginner/day-29/exercise. Nếu muốn tách hàm Python để đọc/kiểm tra/tính/lưu, bạn có thể làm nhưng không bắt buộc tạo package trước.

## Hướng dẫn bạn cần điền

- Lệnh chạy:
- Các file nguồn:
- Quy tắc trạng thái:
- Số dòng/tổng tiền thực tế:
- Cách bạn đã gây và bắt lỗi join:
- Điều còn chưa giải thích được:

Hoàn thành khi bạn tự viết, chạy lại và giải thích được; không chỉ chạy mẫu trong vi_du.py.
