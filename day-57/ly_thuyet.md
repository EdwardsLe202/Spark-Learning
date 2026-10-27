# Ngày 57 — Tạo feature 30 ngày bằng Spark

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Tạo feature 30 ngày bằng Spark”. Kết quả cần đạt: 120 dòng trên nguồn đầy đủ. Tiny: C001=2/300000/12 ngày; C002=1/50000/17; C003=0/0/NULL.

## Từ mới gắn với bài này

- **Feature engineering (tạo đặc trưng từ dữ liệu)**.
- **Recency (số ngày từ lần hoạt động gần nhất)**.

## Tình huống và cách hiểu

**Feature engineering (tạo đặc trưng từ dữ liệu)** biến lịch sử thành đầu vào mô hình. Hôm nay tạo events_30d, spend_30d và **recency (số ngày từ lần hoạt động gần nhất)** trong cửa sổ lịch sử.

Dùng bảng khách làm trái để giữ người không có sự kiện. Đếm/tổng không có giao dịch có thể điền 0; recency không có lịch sử giữ NULL và xử lý tiền xử lý sau. Điền recency=0 sẽ làm người không hoạt động trông như vừa hoạt động.

Hàm tham chiếu build_features_spark trong course_support có toàn bộ bước. Lab yêu cầu bạn tự viết lại từ các phép join/groupBy/window đã học, rồi so fixture trước khi dùng dữ liệu đầy đủ. Không chỉ gọi helper và coi là đã hiểu.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-057/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
features = build_features_spark(spark, "2025-02-01", include_labels=False)
features.select("customer_id", "events_30d", "spend_30d", "recency_days").orderBy("customer_id").show(5)
assert features.count() == 120
assert features.select("customer_id", "snapshot_date").distinct().count() == 120
```

## Đọc từng phần của ví dụ

Hàm lọc thời gian trước tổng hợp, left join khách và thêm snapshot_date. Hai assert kiểm tra đủ đối tượng và khóa.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

120 dòng trên nguồn đầy đủ. Tiny: C001=2/300000/12 ngày; C002=1/50000/17; C003=0/0/NULL.

## Ba câu kiểm tra hiểu bài

1. Feature engineering có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: tạo đặc trưng từ dữ liệu.
- Luồng chính: Hàm lọc thời gian trước tổng hợp, left join khách và thêm snapshot_date. Hai assert kiểm tra đủ đối tượng và khóa.
- Đối chiếu tiêu chí: 120 dòng trên nguồn đầy đủ. Tiny: C001=2/300000/12 ngày; C002=1/50000/17; C003=0/0/NULL. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 11 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
