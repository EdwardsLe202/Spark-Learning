# Ngày 64 — Xếp hạng bằng ROC AUC và PR AUC

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Xếp hạng bằng ROC AUC và PR AUC”. Kết quả cần đạt: ROC AUC=0.75, AP khoảng 0.8333; ghi đúng tên hai metric.

## Từ mới gắn với bài này

- **ROC AUC (diện tích dưới đường ROC)**.
- **Average precision (trung bình precision theo thứ hạng)**.

## Tình huống và cách hiểu

Một ngưỡng chỉ cho một confusion matrix. **ROC AUC (diện tích dưới đường ROC)** đánh giá xếp hạng qua nhiều ngưỡng. **Average precision (trung bình precision theo thứ hạng)** tóm tắt precision/recall theo định nghĩa của thư viện.

Spark areaUnderPR và sklearn average_precision_score không mặc định cùng cách tính diện tích. Ghi tên hàm, cách weighting, tập dữ liệu và lớp dương khi so. Dùng score liên tục, không dùng nhãn 0/1 đã threshold cho metric ranking.

Nếu tập đánh giá chỉ có một lớp, ROC AUC không được xác định theo cách thông thường. Báo thiếu mẫu phù hợp thay vì bịa một điểm. Với dữ liệu nhỏ, xem cả ví dụ lỗi chứ không chỉ số AUC.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-064/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from sklearn.metrics import roc_auc_score, average_precision_score
y = [0, 0, 1, 1]
scores = [0.1, 0.4, 0.35, 0.8]
print("ROC AUC:", roc_auc_score(y, scores))
print("Average precision:", average_precision_score(y, scores))
```

## Đọc từng phần của ví dụ

Hai hàm nhận score, không phải prediction đã làm tròn. Cặp 0.4/0.35 thể hiện một lỗi xếp hạng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

ROC AUC=0.75, AP khoảng 0.8333; ghi đúng tên hai metric.

## Ba câu kiểm tra hiểu bài

1. ROC AUC có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: diện tích dưới đường ROC.
- Luồng chính: Hai hàm nhận score, không phải prediction đã làm tròn. Cặp 0.4/0.35 thể hiện một lỗi xếp hạng.
- Đối chiếu tiêu chí: ROC AUC=0.75, AP khoảng 0.8333; ghi đúng tên hai metric. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 13 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
