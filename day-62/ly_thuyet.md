# Ngày 62 — Baseline trước khi dùng model phức tạp

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Baseline trước khi dùng model phức tạp”. Kết quả cần đạt: Ví dụ tay accuracy=0.75, recall=0; không xem accuracy cao là đủ.

## Từ mới gắn với bài này

- **Baseline (mốc dự đoán đơn giản)**.
- **Class imbalance (mất cân bằng lớp)**.

## Tình huống và cách hiểu

**Baseline (mốc dự đoán đơn giản)** giúp biết model có hơn cách làm rất dễ không. Với **class imbalance (mất cân bằng lớp)**, luôn đoán lớp đông có thể accuracy cao nhưng không tìm được khách churn.

DummyClassifier học tỷ lệ hoặc lớp đông từ train. Nó vẫn phải dùng split đúng thời gian; không lấy tỷ lệ test để thiết kế baseline. Ghi metric trên validation trước khi thử model khác.

Một baseline yếu không có nghĩa bài toán vô ích, nhưng nó làm rõ cần so với gì. Giữ cả số lượng mẫu mỗi lớp và mục tiêu nghiệp vụ, chẳng hạn ngân sách liên hệ khách hàng, để metric có ngữ cảnh.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-062/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score
train, val = snapshot_pd(), snapshot_pd("2025-04-01")
baseline = DummyClassifier(strategy="most_frequent").fit(train[["events_30d"]], train["label"])
pred = baseline.predict(val[["events_30d"]])
print({"accuracy": accuracy_score(val.label, pred), "recall": recall_score(val.label, pred, zero_division=0)})
```

## Đọc từng phần của ví dụ

Fit chỉ train; đánh giá trên snapshot tương lai. Recall có policy rõ khi không có dự đoán dương.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ví dụ tay accuracy=0.75, recall=0; không xem accuracy cao là đủ.

## Ba câu kiểm tra hiểu bài

1. Baseline có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mốc dự đoán đơn giản.
- Luồng chính: Fit chỉ train; đánh giá trên snapshot tương lai. Recall có policy rõ khi không có dự đoán dương.
- Đối chiếu tiêu chí: Ví dụ tay accuracy=0.75, recall=0; không xem accuracy cao là đủ. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 13 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
