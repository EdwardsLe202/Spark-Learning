# Ngày 73 — Threshold chi phí và calibration

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Threshold chi phí và calibration”. Kết quả cần đạt: Bảng ba ngưỡng có FP/FN/cost thật; chọn trên validation, không trên test.

## Từ mới gắn với bài này

- **Threshold (ngưỡng quyết định)**.
- **Calibration (hiệu chỉnh độ phù hợp xác suất)**.

## Tình huống và cách hiểu

**Threshold (ngưỡng quyết định)** biến score thành nhãn; nó khác tham số dùng fit model. Nếu bỏ sót churn đắt hơn liên hệ nhầm, bạn có thể chọn ngưỡng theo chi phí FP/FN trên validation.

**Calibration (hiệu chỉnh độ phù hợp xác suất)** quan tâm score 0.7 có tương ứng khoảng 70% dương trong điều kiện đánh giá không. Model xếp hạng tốt chưa chắc đã hiệu chỉnh tốt. Chưa cần huấn luyện bộ calibration trong bài chính, nhưng phải phân biệt nó với chọn threshold.

Giữ test khóa sau khi đã chọn cấu hình và ngưỡng. Với ngân sách liên hệ cố định, còn có thể chọn top-k thay vì một ngưỡng xác suất. Ghi rõ chính sách và cách xử lý các score bằng nhau.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-073/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
model, train, val = fit_sklearn()
scores = model.predict_proba(val[FEATURES])[:, 1]
rows = []
for threshold in [0.3, 0.5, 0.7]:
    report = metric_counts(val.label, scores, threshold)
    rows.append({"threshold": threshold, **report, "cost": report["fp"] + 5 * report["fn"]})
print(rows)
```

## Đọc từng phần của ví dụ

Ví dụ đặt chi phí FN gấp 5 FP như giả định học tập. Không gọi đó là chi phí thật của doanh nghiệp.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Bảng ba ngưỡng có FP/FN/cost thật; chọn trên validation, không trên test.

## Ba câu kiểm tra hiểu bài

1. Threshold có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: ngưỡng quyết định.
- Luồng chính: Ví dụ đặt chi phí FN gấp 5 FP như giả định học tập. Không gọi đó là chi phí thật của doanh nghiệp.
- Đối chiếu tiêu chí: Bảng ba ngưỡng có FP/FN/cost thật; chọn trên validation, không trên test. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 13 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
