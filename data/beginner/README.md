# Tám đơn hàng để học Spark

[Khóa học](../../README.md) · [Ngày bắt đầu đọc CSV](../../day-06/README.md)

Đây là dữ liệu giả lập nhỏ để bạn tự tính được kết quả. Mỗi dòng orders là **một đơn**, không phải một khách. Đơn vị amount là đồng Việt Nam.

## Bảng đơn hàng

| order_id | customer_id | order_date | amount | status |
| --- | --- | --- | ---: | --- |
| O001 | C001 | 2025-01-01 | 100000 | completed |
| O002 | C001 | 2025-01-03 | 200000 | completed |
| O003 | C002 | 2025-01-03 | 50000 | completed |
| O004 | C003 | 2025-01-04 | 300000 | cancelled |
| O005 | C002 | 2025-01-05 | 150000 | completed |
| O006 | C003 | 2025-01-05 | 120000 | completed |
| O007 | C004 | 2025-01-06 | 80000 | completed |
| O008 | C001 | 2025-01-07 | 400000 | completed |

- order_id: mã đơn, duy nhất trong bảng chuẩn.
- customer_id: mã khách; lặp nhiều lần khi khách có nhiều đơn.
- order_date: ngày đặt theo năm-tháng-ngày, chưa có giờ.
- amount: tiền nguyên VND; khi khai báo schema dùng long.
- status: completed là hoàn tất, cancelled là đã hủy.

File CSV có 9 dòng tính cả dòng đầu tên cột, nhưng chỉ 8 dòng dữ liệu.

## Bảng khách hàng, dùng từ ngày 18

| customer_id | name | region |
| --- | --- | --- |
| C001 | An | HN |
| C002 | Binh | HCM |
| C003 | Chi | DN |
| C004 | Dung | HN |
| C005 | Ha | HCM |

C005 chưa có đơn. customer_id phải duy nhất ở bảng này để bổ sung tên vào đơn mà không nhân tiền.

## Các kết quả tính tay

Chỉ đối chiếu phần mà ngày hiện tại đã học; không cần hiểu các báo cáo sau ngay khi mở file.

- Tất cả đơn: 8 đơn, 1400000 VND.
- Hoàn tất: 7 đơn, 1100000 VND.
- Hủy: 1 đơn O004, 300000 VND.
- Completed và amount >=150000: O002/O005/O008, tổng 750000.

| Khách | Tổng mọi đơn | Tổng completed | Số đơn completed |
| --- | ---: | ---: | ---: |
| C001 | 700000 | 700000 | 3 |
| C002 | 200000 | 200000 | 2 |
| C003 | 420000 | 120000 | 1 |
| C004 | 80000 | 80000 | 1 |
| C005 | 0 | 0 | 0 |

Tổng completed theo vùng: HN=780000, HCM=200000, DN=120000.

## File lỗi, chỉ dùng khi tới ngày 23

orders_dirty.csv có 10 dòng: 5 lỗi cơ bản (thiếu mã khách, ngày sai, số âm, tiền không phải số, thiếu tiền); trong 5 ứng viên còn lại có một bản O002 lặp hoàn toàn. Sau bỏ trùng, có một mã C999 không tồn tại. Cuối cùng sạch 3 dòng O001/O002/O015, tổng 390000.

Đối soát: **10 = 5 lỗi cơ bản + 1 bản trùng + 1 mã khách lạ + 3 sạch**. File manifest.json chứa hash để kiểm tra nguồn không vô tình đổi.
