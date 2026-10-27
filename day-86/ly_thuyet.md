# Ngày 86 — MLflow experiment run và parameter

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “MLflow experiment run và parameter”. Kết quả cần đạt: Có run_id, parameter và artifact manifest trong experiment spark-course-150.

## Từ mới gắn với bài này

- **Experiment (nhóm thí nghiệm)**.
- **Run (một lần thực thi)**.
- **Parameter (tham số cấu hình)**.

## Tình huống và cách hiểu

**Experiment (nhóm thí nghiệm)** gom các **run (một lần thực thi)** của cùng mục tiêu. **Parameter (tham số cấu hình)** như C khác metric đo trên dữ liệu. Mỗi lần fit cần nối được với nguồn và code.

Repo cố định MLflow 2.22.0 với SQLite và artifact local. Dùng setup_tracking để chọn đường dẫn tường minh, không phụ thuộc mặc định của phiên bản khác. Mẫu mới không trộn các run cũ đã tạo trong khóa nền trước.

Log thủ công trước khi dùng autolog để hiểu thông tin nào thực sự được lưu. Hash của source và code giúp phát hiện thay đổi nhưng không tự phục hồi file đã mất; vẫn giữ snapshot và dependency.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-086/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
mlflow = setup_tracking()
with mlflow.start_run(run_name="parameter-demo") as run:
    mlflow.log_param("C", 1.0)
    mlflow.log_param("train_snapshot", "2025-02-01")
    mlflow.set_tag("source_hash", data_hash())
    mlflow.log_artifact(str(ROOT / "data/raw/manifest.json"))
    print("Run:", run.info.run_id)
```

## Đọc từng phần của ví dụ

Run có context manager để kết thúc đúng trạng thái. Manifest được lưu như artifact chứ không chỉ đường dẫn text.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có run_id, parameter và artifact manifest trong experiment spark-course-150.

## Ba câu kiểm tra hiểu bài

1. Experiment có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: nhóm thí nghiệm.
- Luồng chính: Run có context manager để kết thúc đúng trạng thái. Manifest được lưu như artifact chứ không chỉ đường dẫn text.
- Đối chiếu tiêu chí: Có run_id, parameter và artifact manifest trong experiment spark-course-150. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 15 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
