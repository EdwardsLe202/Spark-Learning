# Ngày 66 — Fit preprocessing chỉ trên train

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Fit preprocessing chỉ trên train”. Kết quả cần đạt: Thống kê train giữ nguyên; inference không huấn luyện lại.

## Từ mới gắn với bài này

- **Fit / Transform (học quy tắc / áp dụng quy tắc)**.
- **Train-only statistics (thống kê chỉ học từ train)**.

## Tình huống và cách hiểu

**Fit / transform (học quy tắc / áp dụng quy tắc)** là hai giai đoạn khác nhau. Median và trung bình scaler được học trong fit. Validation chỉ được transform bằng quy tắc đã học, không fit lại để nó trông gần train hơn.

**Train-only statistics (thống kê chỉ học từ train)** giúp đánh giá đúng thông tin có sẵn. Fit imputer trên toàn dataset làm tập đánh giá góp dữ liệu vào quá trình chuẩn bị, dù bạn chưa đưa nhãn test vào classifier.

Ví dụ học mean/scale ở train rồi xem sau predict validation chúng không đổi. Bạn cũng cần cố định nguồn/split; random seed không tự bảo vệ ranh giới thời gian.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-066/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
model, train, val = fit_sklearn()
scale = model.named_steps["preprocess"].named_transformers_["numeric"].named_steps["scale"]
before = scale.mean_.copy()
model.predict_proba(val[FEATURES])
assert (before == scale.mean_).all()
print("Mean học từ train:", before.tolist())
```

## Đọc từng phần của ví dụ

Predict chỉ áp dụng pipeline. Mảng mean không đổi sau khi dùng validation.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Thống kê train giữ nguyên; inference không huấn luyện lại.

## Ba câu kiểm tra hiểu bài

1. Fit / Transform có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: học quy tắc / áp dụng quy tắc.
- Luồng chính: Predict chỉ áp dụng pipeline. Mảng mean không đổi sau khi dùng validation.
- Đối chiếu tiêu chí: Thống kê train giữ nguyên; inference không huấn luyện lại. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 11 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
