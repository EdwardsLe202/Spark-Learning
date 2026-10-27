# Ngày 13 — Lý thuyết: Đánh giá lựa chọn và tuning mô hình

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Chọn cấu hình và threshold trên validation rồi chỉ đánh giá test sau khi chốt.

## 1. Metric cần phản ánh mục tiêu
**Class imbalance (mất cân bằng lớp)** xuất hiện khi churn ít hơn không churn. **Accuracy (tỷ lệ dự đoán đúng)** có thể cao khi luôn đoán lớp đông. **Confusion matrix (ma trận nhầm lẫn)** gồm TP, FP, TN, FN. **Precision (tỷ lệ đúng trong các dự đoán dương)** = TP/(TP+FP); **recall (tỷ lệ tìm được các mẫu dương thực tế)** = TP/(TP+FN). Quy định giá trị khi mẫu số bằng 0.

**ROC AUC (diện tích dưới đường cong ROC)** và **PR AUC (diện tích dưới đường cong precision–recall)** đánh giá khả năng xếp hạng qua nhiều ngưỡng. Cần ghi cách tính; Spark areaUnderPR không đồng nhất mọi cách tính average precision của thư viện khác. Với fixture bé, kết quả có độ bất định lớn.

## 2. Model và threshold là hai quyết định
**Threshold (ngưỡng quyết định)** biến xác suất thành nhãn. Giảm threshold thường lấy thêm khách hàng nhưng cũng có thêm dự đoán nhầm. Nếu chỉ được liên hệ 20 khách hàng, có thể đánh giá top 20 thay vì chọn ngưỡng tùy ý. Dùng validation cho quyết định này; không nhìn test rồi sửa tiếp.

**Hyperparameter tuning (chọn siêu tham số)** thử các cấu hình như regParam. **Cross-validation (đánh giá chéo)** cần phù hợp cấu trúc thời gian. CrossValidator và TrainValidationSplit mặc định không tự bảo vệ mọi ràng buộc thời gian của dự án; với snapshot này, dùng vòng lặp train cố định và validation tương lai sẽ dễ kiểm soát hơn.

## 3. Giới hạn chi phí và diễn giải
Tính số lần fit trước khi chạy: 3 giá trị × 2 cấu hình × 3 fold = 18 lần fit, chưa kể fit cuối. Lưu cả baseline dự đoán đa số và ít nhất hai cấu hình. **Slice evaluation (đánh giá theo nhóm)** theo plan/region giúp thấy nhóm bị bỏ sót; nhóm quá ít mẫu cần được ghi rõ. Chỉ mở test sau khi đã lưu cấu hình và threshold cuối.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
# Ví dụ số học độc lập với thư viện metric.
tp, fp, fn, tn = 12, 8, 3, 77
precision = tp / (tp + fp)
recall = tp / (tp + fn)
print({"precision": precision, "recall": recall, "accuracy": (tp + tn) / 100})
```

## Năm ý đối chiếu với lộ trình gốc

- 13.1 — Baseline, class imbalance, confusion matrix, precision, recall, PR AUC và ROC AUC.
- 13.2 — Chọn threshold bằng validation và chi phí nghiệp vụ; hiệu chỉnh xác suất khi cần.
- 13.3 — CrossValidator, TrainValidationSplit và ParamGridBuilder.
- 13.4 — Validation theo thời gian bằng fold hoặc vòng lặp phù hợp; tránh dùng mặc định sai bài toán.
- 13.5 — Đánh giá theo nhóm, khoảng bất định và chốt test sau khi quyết định mô hình.

Các ý trên giữ phạm vi phần 13 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Accuracy cao có thể vô ích khi nào?
2. Threshold khác regParam thế nào?
3. 4 cấu hình × 3 fold cần ít nhất bao nhiêu lần fit?

## Đọc thêm từ nguồn chính thức

- [Spark ML tuning](https://spark.apache.org/docs/3.5.7/ml-tuning.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
