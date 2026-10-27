# Ngày 105 — Chính sách retrain và nghiệm thu MLOps

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Chính sách retrain và nghiệm thu MLOps”. Kết quả cần đạt: Có candidate rejected, previous không bị thay, lineage và policy được kiểm tra.

## Từ mới gắn với bài này

- **Retraining (huấn luyện lại)**.
- **Candidate gate (điều kiện chấp nhận model ứng viên)**.

## Tình huống và cách hiểu

**Retraining (huấn luyện lại)** cần dữ liệu hợp lệ, nhãn đủ quan sát và protocol đánh giá. **Candidate gate (điều kiện chấp nhận model ứng viên)** so với baseline/current, theo nhóm, runtime và contract; không chỉ một metric đẹp hơn chút.

Giữ model cũ khi candidate không đạt và ghi lý do. Nếu nguồn sai schema, sửa nguồn trước thay vì học lại từ dữ liệu hỏng. Sau promote còn cần rollout, theo dõi và rollback.

Ngày này nghiệm thu phần vận hành dự án 2: từ prediction tìm được model/run/data/code, CLI có test, DAG retry/backfill, image chạy, CI kiểm tra và release có thể quay lại. Các phần chưa chạy thật ghi rõ để bổ sung ở ngày 120.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-105/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
policy = {"trigger": ["quality_checked", "labels_complete", "reviewed_performance_drop"], "gates": ["same_validation_protocol", "schema_compatible", "minimum_metric", "no_slice_regression_unexplained"], "on_reject": "keep_previous", "after_promote": ["readiness", "monitor", "rollback_if_needed"]}
write_json(out / "retrain_policy.json", policy)
print(policy)
```

## Đọc từng phần của ví dụ

Policy là thiết kế cần được code và test; nó không tự huấn luyện hay tự đổi model.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có candidate rejected, previous không bị thay, lineage và policy được kiểm tra.

## Ba câu kiểm tra hiểu bài

1. Retraining có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: huấn luyện lại.
- Luồng chính: Policy là thiết kế cần được code và test; nó không tự huấn luyện hay tự đổi model.
- Đối chiếu tiêu chí: Có candidate rejected, previous không bị thay, lineage và policy được kiểm tra. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 20 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
