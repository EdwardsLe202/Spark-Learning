# Ngày 90 — Backend store artifact store và truy vết prediction

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Backend store artifact store và truy vết prediction”. Kết quả cần đạt: Có một prediction truy về được model/run/source; không chỉ một template placeholder.

## Từ mới gắn với bài này

- **Backend store (kho metadata)**.
- **Artifact store (kho tệp đầu ra)**.
- **Prediction lineage (nguồn gốc dự đoán)**.

## Tình huống và cách hiểu

**Backend store (kho metadata)** giữ run, metric, parameter; **artifact store (kho tệp đầu ra)** giữ model và báo cáo. Chỉ sao lưu SQLite mà mất artifact thì không đủ load model.

**Prediction lineage (nguồn gốc dự đoán)** nối customer/snapshot với model_version, run_id, feature version, data hash và code. Đường dẫn cố định có thể bị ghi đè; ghi nội dung/version cụ thể mới kiểm chứng được.

Server local chạy loopback cho lab. Khi chia sẻ server cần authentication, authorization và chính sách lưu trữ; không tự công khai cổng chỉ để xem UI trên thiết bị khác. Bài thực hành kiểm tra backup và restore trong vùng thử riêng.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-090/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
mlflow = setup_tracking()
experiment = mlflow.get_experiment_by_name("spark-course-150")
print({"tracking_uri": mlflow.get_tracking_uri(), "artifact_location": experiment.artifact_location})
record = {"customer_id": "C001", "snapshot_date": "2025-07-01", "model_version": "fill-resolved-version", "run_id": "fill-real-run", "data_hash": data_hash()}
write_json(out / "prediction_lineage_template.json", record)
print("Template chưa đủ nghiệm thu cho tới khi điền run/version thật.")
```

## Đọc từng phần của ví dụ

In hai vị trí lưu khác nhau. Record là mẫu cần điền định danh thật, không tính như prediction thực đã truy vết.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có một prediction truy về được model/run/source; không chỉ một template placeholder.

## Ba câu kiểm tra hiểu bài

1. Backend store có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: kho metadata.
- Luồng chính: In hai vị trí lưu khác nhau. Record là mẫu cần điền định danh thật, không tính như prediction thực đã truy vết.
- Đối chiếu tiêu chí: Có một prediction truy về được model/run/source; không chỉ một template placeholder. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 15 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
