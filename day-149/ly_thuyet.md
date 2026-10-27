# Ngày 149 — Clean run data dictionary model card và runbook

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Clean run data dictionary model card và runbook”. Kết quả cần đạt: Người khác tái chạy được theo tài liệu, có version và giới hạn, không dựa notebook đang mở.

## Từ mới gắn với bài này

- **Reproducibility (khả năng tái lập)**.
- **Model card (mô tả mục đích và giới hạn)**.
- **Runbook (cách vận hành phục hồi)**.

## Tình huống và cách hiểu

**Reproducibility (khả năng tái lập)** cần code, dependency, snapshot, config và artifact đúng version. **Model card (mô tả mục đích và giới hạn)** không phải danh sách thư viện. **Runbook (cách vận hành phục hồi)** chỉ rõ triệu chứng, kiểm tra và cách xác nhận sau sửa.

Ba dự án chính là dữ liệu/feature, ML có MLOps/API và RAG có eval. Khóa nền còn có báo cáo đơn hàng nhỏ. Ngày này dùng để dọn bằng chứng đã có, không bắt đầu cả ba từ số 0.

Chạy từ môi trường/output mới mà không xóa bài làm gốc. Nhờ người khác hoặc chính bạn theo README mà không dựa vào trí nhớ đường dẫn. Tách local, nhiều container, cluster nhiều máy và cloud thật trong mọi claim.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-149/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
files = ["course_support.py", "services/pipeline.py", "services/churn_api.py", "rag_support.py"]
manifest = {name: __import__("hashlib").sha256((ROOT / name).read_bytes()).hexdigest() for name in files}
write_json(out / "code_manifest.json", manifest)
print(manifest)
print("Bổ sung model/prompt/index/data/dependency version thật của dự án bạn.")
```

## Đọc từng phần của ví dụ

Hash code chỉ kiểm chứng nội dung, chưa tự lưu mọi dependency/model. Manifest dự án phải bổ sung những phần còn lại.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Người khác tái chạy được theo tài liệu, có version và giới hạn, không dựa notebook đang mở.

## Ba câu kiểm tra hiểu bài

1. Reproducibility có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: khả năng tái lập.
- Luồng chính: Hash code chỉ kiểm chứng nội dung, chưa tự lưu mọi dependency/model. Manifest dự án phải bổ sung những phần còn lại.
- Đối chiếu tiêu chí: Người khác tái chạy được theo tài liệu, có version và giới hạn, không dựa notebook đang mở. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 30 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
