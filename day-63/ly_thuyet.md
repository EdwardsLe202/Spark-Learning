# Ngày 63 — Confusion matrix precision recall

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Confusion matrix precision recall”. Kết quả cần đạt: Ngưỡng 0.5: precision=0.5, recall=0.5; các ô đều 1.

## Từ mới gắn với bài này

- **Confusion matrix (ma trận nhầm lẫn)**.
- **Precision (tỷ lệ đúng trong dự đoán dương)**.
- **Recall (tỷ lệ tìm được mẫu dương)**.

## Tình huống và cách hiểu

**Confusion matrix (ma trận nhầm lẫn)** đếm TP, FP, FN, TN. Positive ở bài này là churn=1. **Precision (tỷ lệ đúng trong dự đoán dương)** là TP/(TP+FP); **recall (tỷ lệ tìm được mẫu dương)** là TP/(TP+FN).

Không đổi tên lớp dương giữa hai báo cáo. Nếu không dự đoán ai churn, precision có mẫu số 0; ghi convention thay vì bỏ qua. Accuracy gộp cả hai lớp nên che được một nhóm bị bỏ sót.

Dùng bốn nhãn để tự đánh dấu từng lỗi trước khi gọi thư viện. Sau đó đối chiếu với helper metric_counts. Một lỗi định nghĩa metric có thể khiến bạn chọn sai model dù code train đúng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-063/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
y = [1, 0, 1, 0]
scores = [0.9, 0.8, 0.2, 0.1]
report = metric_counts(y, scores, threshold=0.5)
print(report)
assert report["tp"] == report["fp"] == report["fn"] == report["tn"] == 1
```

## Đọc từng phần của ví dụ

Ngưỡng 0.5 tạo dự đoán 1,1,0,0. Mỗi ô ma trận có đúng một mẫu.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ngưỡng 0.5: precision=0.5, recall=0.5; các ô đều 1.

## Ba câu kiểm tra hiểu bài

1. Confusion matrix có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: ma trận nhầm lẫn.
- Luồng chính: Ngưỡng 0.5 tạo dự đoán 1,1,0,0. Mỗi ô ma trận có đúng một mẫu.
- Đối chiếu tiêu chí: Ngưỡng 0.5: precision=0.5, recall=0.5; các ô đều 1. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 13 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
