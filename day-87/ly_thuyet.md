# Ngày 87 — Ghi metric và artifact từ lần train thật

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Ghi metric và artifact từ lần train thật”. Kết quả cần đạt: Có metric thật cho các run; đủ source/code metadata do bạn bổ sung.

## Từ mới gắn với bài này

- **Metric (chỉ số đo)**.
- **Artifact (đầu ra lưu kèm run)**.
- **Autologging (ghi thí nghiệm tự động)**.

## Tình huống và cách hiểu

**Metric (chỉ số đo)** cần có dataset, định nghĩa và thời điểm rõ. **Artifact (đầu ra lưu kèm run)** có thể là bảng metric theo nhóm hoặc model card. Đừng tạo năm run chỉ bằng năm con số bịa.

**Autologging (ghi thí nghiệm tự động)** tiết kiệm thao tác nhưng không biết hết nhãn churn, cutoff hay quyền dữ liệu. Vẫn log các thông tin nghiệp vụ và snapshot do bạn định nghĩa.

Bài này train hai cấu hình thật để thấy luồng; lab tạo ít nhất năm cấu hình nhỏ trên cùng validation, giữ budget. Không dùng test để chọn run thắng. Khi so runtime, ghi có tính chi phí log hay không.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-087/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from sklearn.metrics import average_precision_score
mlflow = setup_tracking()
for C in [0.1, 1.0]:
    with mlflow.start_run(run_name="churn-C-" + str(C)):
        model, train, val = fit_sklearn(C)
        ap = float(average_precision_score(val.label, model.predict_proba(val[FEATURES])[:, 1]))
        mlflow.log_param("C", C)
        mlflow.log_metric("validation_ap", ap)
        mlflow.set_tag("source_hash", data_hash())
        print(C, ap)
```

## Đọc từng phần của ví dụ

Mỗi run thực sự gọi fit và tính AP trên cùng snapshot. Các con số được đo, không có metric mong muốn sẵn.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có metric thật cho các run; đủ source/code metadata do bạn bổ sung.

## Ba câu kiểm tra hiểu bài

1. Metric có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: chỉ số đo.
- Luồng chính: Mỗi run thực sự gọi fit và tính AP trên cùng snapshot. Các con số được đo, không có metric mong muốn sẵn.
- Đối chiếu tiêu chí: Có metric thật cho các run; đủ source/code metadata do bạn bổ sung. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 15 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
