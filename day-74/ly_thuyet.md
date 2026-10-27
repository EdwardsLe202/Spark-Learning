# Ngày 74 — Giới hạn số lần fit khi tuning

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Giới hạn số lần fit khi tuning”. Kết quả cần đạt: Grid ví dụ tay cần 24 fit trước lần fit cuối; bảng mẫu có hai cấu hình thật.

## Từ mới gắn với bài này

- **Hyperparameter (siêu tham số)**.
- **Parameter grid (lưới cấu hình)**.

## Tình huống và cách hiểu

**Hyperparameter (siêu tham số)** như mức regularization được chọn bên ngoài quá trình học hệ số. **Parameter grid (lưới cấu hình)** liệt kê các tổ hợp; số lần fit có thể tăng nhanh khi nhân thêm fold.

Bắt đầu hai cấu hình và một split thời gian đã cố định. Ghi runtime và metric cùng nhau. Không tăng grid chỉ vì máy đang rảnh nếu chưa có giả thuyết cần thử.

Spark có ParamGridBuilder, TrainValidationSplit và CrossValidator, nhưng cách chia mặc định không tự đáp ứng mọi bài toán thời gian. Bài này dùng vòng lặp tường minh để giữ train/validation đúng cutoff. Ngày sau mới tổ chức nhiều fold thời gian.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-074/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from sklearn.metrics import average_precision_score
from time import perf_counter
rows = []
for C in [0.1, 1.0]:
    start = perf_counter()
    model, train, val = fit_sklearn(C)
    ap = average_precision_score(val.label, model.predict_proba(val[FEATURES])[:, 1])
    rows.append({"C": C, "validation_ap": float(ap), "seconds": perf_counter() - start})
print(rows)
```

## Đọc từng phần của ví dụ

Hai cấu hình bằng hai lần fit. AP tính trên cùng snapshot nên so có ý nghĩa hơn đổi cả dữ liệu.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Grid ví dụ tay cần 24 fit trước lần fit cuối; bảng mẫu có hai cấu hình thật.

## Ba câu kiểm tra hiểu bài

1. Hyperparameter có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: siêu tham số.
- Luồng chính: Hai cấu hình bằng hai lần fit. AP tính trên cùng snapshot nên so có ý nghĩa hơn đổi cả dữ liệu.
- Đối chiếu tiêu chí: Grid ví dụ tay cần 24 fit trước lần fit cuối; bảng mẫu có hai cấu hình thật. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 13 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
