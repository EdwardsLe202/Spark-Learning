# Ngày 80 — Chốt model và model card

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Chốt model và model card”. Kết quả cần đạt: Có báo cáo test thật và model card; không tự đặt metric đẹp hoặc khẳng định hiệu quả kinh doanh.

## Từ mới gắn với bài này

- **Model card (bản mô tả mục đích và giới hạn model)**.
- **Holdout (tập giữ riêng để chấm cuối)**.

## Tình huống và cách hiểu

**Model card (bản mô tả mục đích và giới hạn model)** ghi target, nguồn, split, feature, metric, threshold và trường hợp không dùng. **Holdout (tập giữ riêng để chấm cuối)** chỉ mở sau khi đã lưu quyết định chọn cấu hình.

Đánh giá test một lần theo protocol đã chốt. Nếu kết quả không đạt, báo thật và xem xét một vòng nghiên cứu mới với eval plan phù hợp; không tiếp tục chỉnh theo test rồi vẫn gọi nó chưa từng dùng.

Đây là buổi ôn ML trước khi quản lý thí nghiệm. Artifact phải load được và truy về dataset. Chất lượng trên dữ liệu giả lập chỉ là bằng chứng quy trình, không chứng minh sẽ giữ khách thật tốt hơn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-080/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from sklearn.metrics import average_precision_score
model, train, val = fit_sklearn()
test = snapshot_pd("2025-06-01")
score = model.predict_proba(test[FEATURES])[:, 1]
report = {"test_ap": float(average_precision_score(test.label, score)), **metric_counts(test.label, score), "source": "synthetic", "threshold": 0.5}
write_json(out / "test_report.json", report)
print(report)
```

## Đọc từng phần của ví dụ

Đây là mẫu quyết định cố định C=1/threshold=0.5, không chọn bằng test. Bài làm dùng cấu hình bạn đã chốt trên validation.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có báo cáo test thật và model card; không tự đặt metric đẹp hoặc khẳng định hiệu quả kinh doanh.

## Ba câu kiểm tra hiểu bài

1. Model card có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: bản mô tả mục đích và giới hạn model.
- Luồng chính: Đây là mẫu quyết định cố định C=1/threshold=0.5, không chọn bằng test. Bài làm dùng cấu hình bạn đã chốt trên validation.
- Đối chiếu tiêu chí: Có báo cáo test thật và model card; không tự đặt metric đẹp hoặc khẳng định hiệu quả kinh doanh. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 13 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
