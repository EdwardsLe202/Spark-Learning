# Ngày 20 — Lý thuyết: Giám sát drift và huấn luyện lại

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Phát hiện thay đổi đầu vào và tách cảnh báo drift khỏi kết luận model kém.

## 1. Theo dõi cả hệ thống lẫn dự đoán
**Monitoring (giám sát)** gồm runtime, tỷ lệ lỗi, độ mới dữ liệu và chất lượng mô hình. **Log (bản ghi sự kiện)** cho biết chuyện gì xảy ra; **metric (chỉ số tổng hợp)** cho biết mức độ; **trace (dấu vết các bước của một yêu cầu)** nối các bước để tìm chỗ chậm hoặc lỗi.

**Data freshness (độ mới dữ liệu)** quan trọng vì một pipeline thành công trên dữ liệu cũ vẫn có thể tạo dự đoán không phù hợp. Đo tỷ lệ thiếu, khóa lạ và schema trước khi so phân bố. **Schema drift (thay đổi lược đồ)** có thể làm model không chạy; **data drift (thay đổi phân bố dữ liệu)** có thể không làm mất tính đúng của contract nhưng vẫn cần điều tra.

## 2. Chưa có nhãn thì biết được gì?
**Prediction drift (thay đổi phân bố dự đoán)** phản ánh score/nhãn model thay đổi. **Concept drift (thay đổi quan hệ giữa đầu vào và mục tiêu)** cần bằng chứng về quan hệ hoặc hiệu năng có nhãn. Phân bố spend thay đổi không tự chứng minh precision giảm. Với churn 30 ngày, nhãn đến trễ nên đánh giá hiện tại có giới hạn.

So với **reference window (khoảng dữ liệu làm mốc)** và tính theo nhóm plan/region. Chọn **alert threshold (ngưỡng cảnh báo)** cùng lượng mẫu tối thiểu và cách hành động; 120 dòng giả lập chưa đủ để suy ra ngưỡng production phổ quát.

## 3. Retrain là một quyết định có điều kiện
**Retraining (huấn luyện lại)** cần dữ liệu, nhãn, quality gate và so sánh candidate với model đang dùng. Nếu nguồn sai schema, sửa pipeline trước thay vì train trên dữ liệu hỏng. Giữ model cũ khi candidate không đạt và ghi lý do. Khi phát hành vẫn cần version, kiểm tra schema, theo dõi sau phát hành và rollback.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
import json
from spark_lab import output_dir
reference = [0.05, 0.10, 0.20, 0.30]
current = [0.20, 0.35, 0.60, 0.80]
report = {"reference_mean_score": sum(reference)/len(reference),
          "current_mean_score": sum(current)/len(current),
          "labels_available": False,
          "conclusion": "Phân bố score đổi; chưa kết luận chất lượng model."}
(output_dir(20) / "monitoring_demo.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(report)
```

## Năm ý đối chiếu với lộ trình gốc

- 20.1 — Log, metric, trace; theo dõi runtime, lỗi, độ trễ và tài nguyên.
- 20.2 — Schema drift, missing rate, phân bố feature, prediction drift và data freshness.
- 20.3 — Data drift, concept drift và hiệu năng khi có nhãn; nhãn đến trễ.
- 20.4 — Ngưỡng cảnh báo, điều tra lỗi và phân tích theo nhóm khách hàng.
- 20.5 — Chính sách retrain, đánh giá candidate, rollout và rollback; lưu lịch sử quyết định.

Các ý trên giữ phạm vi phần 20 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Data drift có luôn kéo performance xuống không?
2. Chưa có nhãn thì theo dõi gì?
3. Khi nào nên sửa nguồn thay vì retrain?

## Đọc thêm từ nguồn chính thức

- [MLflow tracking](https://mlflow.org/docs/2.22.0/tracking/)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
