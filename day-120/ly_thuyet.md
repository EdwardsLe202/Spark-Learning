# Ngày 120 — Nghiệm thu dự án 2 từ dữ liệu tới API

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Nghiệm thu dự án 2 từ dữ liệu tới API”. Kết quả cần đạt: Có hệ thống ML chạy lại được cùng bằng chứng chất lượng/vận hành, sẵn nền để học LLM/RAG.

## Từ mới gắn với bài này

- **Service level objective — SLO (mục tiêu mức phục vụ)**.
- **Runbook (hướng dẫn vận hành sự cố)**.

## Tình huống và cách hiểu

**Service level objective — SLO (mục tiêu mức phục vụ)** của lab gắn một tải và cấu hình cụ thể; không là cam kết production. **Runbook (hướng dẫn vận hành sự cố)** cần triệu chứng, bằng chứng kiểm tra, cách xử lý và xác nhận phục hồi.

Ngày này gom Spark batch, nhánh sklearn/API, MLflow, tests, DAG, packaging, CI và monitoring đã luyện riêng. Không bắt đầu toàn bộ từ số 0. Nếu chưa chạy Docker/Airflow/cluster, ghi ca chưa đạt rồi bổ sung theo ngày liên quan.

Demo phải có dữ liệu lỗi, candidate rejected, missing model, request sai, load model tiến trình mới và rollback. Mỗi claim chất lượng/tốc độ có số liệu, split, phần cứng và giới hạn. Không dùng screenshot UI thay bằng chứng lineage/prediction.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-120/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
paths = {"pipeline": ROOT / "services/pipeline.py", "api": ROOT / "services/churn_api.py", "dag": ROOT / "services/airflow/dags/churn_pipeline.py", "tests": ROOT / "tests/test_course_contracts.py"}
print({name: str(path) for name, path in paths.items()})
print("Checklist:", ROOT / "projects/03-mlops-serving/README.md")
print("Điền bằng chứng thật; file tồn tại không có nghĩa đã nghiệm thu.")
```

## Đọc từng phần của ví dụ

Mẫu dẫn tới các thành phần thực thi. Nghiệm thu cần chạy và đối chiếu, không kiểm tra exists đơn thuần.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có hệ thống ML chạy lại được cùng bằng chứng chất lượng/vận hành, sẵn nền để học LLM/RAG.

## Ba câu kiểm tra hiểu bài

1. Service level objective — SLO có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mục tiêu mức phục vụ.
- Luồng chính: Mẫu dẫn tới các thành phần thực thi. Nghiệm thu cần chạy và đối chiếu, không kiểm tra exists đơn thuần.
- Đối chiếu tiêu chí: Có hệ thống ML chạy lại được cùng bằng chứng chất lượng/vận hành, sẵn nền để học LLM/RAG. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 30 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
