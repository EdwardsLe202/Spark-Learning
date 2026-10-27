# Ngày 11 — Lý thuyết: Feature engineering và phòng tránh leakage

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Hoàn thành dự án 1: tạo feature snapshot đúng thời điểm và nhãn có đủ thời gian quan sát.

## 1. Đặt câu hỏi tại một thời điểm cụ thể
**Entity (đối tượng cần dự đoán)** là khách hàng. **Cutoff time (mốc chốt thông tin)** là thời điểm giả định ra quyết định. **Feature (đặc trưng đầu vào)** phải tính từ điều đã biết trước mốc đó. **Observation window (cửa sổ quan sát lịch sử)** của bài này là `[cutoff − 30 ngày, cutoff)`. Dấu `[` bao gồm đầu trái; dấu `)` loại đầu phải. Tất cả mốc dùng UTC lúc 00:00.

**Label (nhãn mục tiêu)** churn bằng 1 khi không có giao dịch trong **label window (cửa sổ xác định nhãn)** `[cutoff, cutoff + 30 ngày)`. Chỉ gán nhãn khi nguồn đã được quan sát tới hết cửa sổ. Khách hàng chưa đủ thời gian không được tự gán churn=1. Khóa đầu ra là `(customer_id, snapshot_date)`, vì một khách hàng có thể được dự đoán nhiều lần.

## 2. Chặn thông tin tương lai
**Data leakage (rò rỉ thông tin vào quá trình học)** xảy ra khi feature chứa giao dịch sau cutoff hoặc preprocessing học từ test. **Point-in-time correctness (tính đúng với thông tin có sẵn tại thời điểm đó)** còn yêu cầu `ingested_at < cutoff` cho feature. Giao dịch xảy ra trước cutoff nhưng đến sau đó chưa thể được biết khi dự đoán. Với nguồn có phiên bản sửa đổi, còn cần chọn phiên bản đã có ở cutoff.

Các feature: `events_30d`, `spend_30d`, `recency_days`. Dùng bảng khách hàng làm gốc để giữ cả người không có giao dịch. Số lượng và tổng tiền có thể điền 0; recency chưa có hoạt động phải có chính sách riêng, không coi như vừa hoạt động hôm nay.

## 3. Chia tập theo thời gian
**Training set (tập huấn luyện)** dùng cutoff 2025-02-01; **validation set (tập chọn cấu hình)** dùng 2025-04-01; **test set (tập đánh giá cuối)** dùng 2025-06-01. Khoảng cách này tránh chồng cửa sổ nhãn của ba snapshot. Khách hàng có thể lặp vì mục tiêu là dự đoán kỳ tiếp theo cho khách hàng đang có; nếu muốn đánh giá khách hàng hoàn toàn mới, cần chia theo nhóm khách hàng nữa.

**Preprocessing (tiền xử lý)** như điền thiếu, chuẩn hóa, mã hóa phải fit trên train rồi áp dụng nguyên trạng cho validation và test. Seed không thể sửa một cách chia tập sai thời gian.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
cutoff = F.to_timestamp(F.lit("2025-02-01T00:00:00Z"))
events = (read_events(spark, "events_tiny.csv")
          .withColumn("event_ts", F.to_timestamp("event_time"))
          .withColumn("available_ts", F.to_timestamp("ingested_at"))
          .withColumn("amount", F.col("amount").cast("long")))
history = events.filter((F.col("event_ts") >= cutoff - F.expr("INTERVAL 30 DAYS")) &
                        (F.col("event_ts") < cutoff) & (F.col("available_ts") < cutoff))
history.groupBy("customer_id").agg(F.count("*").alias("events_30d"), F.sum("amount").alias("spend_30d")).show()
```

## Năm ý đối chiếu với lộ trình gốc

- 11.1 — Định nghĩa entity, thời điểm dự đoán, observation window và label window.
- 11.2 — Tạo nhãn churn cùng quy tắc xử lý khách hàng chưa đủ thời gian quan sát.
- 11.3 — Feature lịch sử, point in time join và dữ liệu được cập nhật muộn.
- 11.4 — Chia train, validation và test theo thời gian hoặc nhóm phù hợp bài toán.
- 11.5 — Fit imputer, scaler, encoder trên train; lưu feature schema và phiên bản dữ liệu.

Các ý trên giữ phạm vi phần 11 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Giao dịch trước cutoff nhưng đến muộn có dùng làm feature không?
2. Vì sao có khoảng cách giữa các snapshot?
3. Khách hàng lặp giữa các tập có luôn sai không?

## Đọc thêm từ nguồn chính thức

- [Common ML pitfalls](https://scikit-learn.org/1.5/common_pitfalls.html)
- [TimeSeriesSplit](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
