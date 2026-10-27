# Ngày 30 — Lý thuyết: Dự án cuối khóa và chuẩn bị ứng tuyển

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Hoàn thiện ba mốc dự án và trình bày bằng chứng chạy từ môi trường sạch.

## 1. Portfolio là chuỗi bằng chứng
**Portfolio (bộ dự án thể hiện năng lực)** cần trả lời: bài toán gì, dữ liệu nào, làm bằng cách nào, kết quả ra sao và giới hạn ở đâu. Một README liệt kê công nghệ chưa chứng minh tính đúng. Bằng chứng tốt gồm fixture, lệnh chạy, test bắt lỗi, bảng metric và demo phục hồi.

Ba mốc của repo là dữ liệu/feature, hệ thống ML có MLOps và RAG có đánh giá. Các ngày trước xây từng phần; ngày 30 dùng để tích hợp và sửa thiếu sót, không bắt đầu cả ba từ số 0. Nguồn gốc ước tính 306–430 giờ, nên 30 ngày là một vòng học tăng tốc; chặng nâng cao cần được giữ là việc học tiếp nếu chưa đủ thời gian.

## 2. Tài liệu cho người chưa biết repo
**Data dictionary (từ điển dữ liệu)** giải thích cột, kiểu, đơn vị và khóa. **Model card (bản mô tả mục đích, dữ liệu và giới hạn model)** ghi split, metric, người dùng dự kiến và trường hợp không phù hợp. **Runbook (hướng dẫn vận hành và xử lý sự cố)** mô tả triệu chứng, kiểm tra, cách phục hồi và xác nhận thành công.

Một release cần code, dependency, snapshot dữ liệu, model/prompt/index và cấu hình. Demo sạch nghĩa là có thể tái chạy từ tài liệu bằng môi trường mới và đích mới; không xóa thư mục bài làm đang dùng để tạo cảm giác sạch. Tách mô phỏng, local nhiều luồng và cluster thật khi mô tả kết quả.

## 3. Tự đánh giá và học tiếp
Chấm theo rubric ở projects/README.md. Mốc gợi ý 80/100 hữu ích để định hướng, nhưng lỗi leakage, trùng khi rerun hoặc sai quyền cần sửa trước. Khi phỏng vấn, giải thích một đánh đổi bằng bằng chứng thực tế: tại sao chọn Spark, ngưỡng dự đoán, cách tìm bottleneck hoặc lý do chưa fine-tune. Chỗ chưa chạy nên được nói rõ để người xem hiểu phạm vi năng lực.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
from spark_lab import ROOT
for project in ["01-data-pipeline", "02-mlops", "03-rag"]:
    readme = ROOT / "projects" / project / "README.md"
    print(project, "->", readme)
# TODO: điền bảng nghiệm thu và liên kết tới code/log/test thực của từng dự án.
```

## Năm ý đối chiếu với lộ trình gốc

- 30.1 — Chốt yêu cầu, dữ liệu, metric, giới hạn tài nguyên và tiêu chí nghiệm thu.
- 30.2 — Hoàn thiện ba mốc dự án dữ liệu, ML vận hành và ứng dụng RAG.
- 30.3 — Tạo README, sơ đồ, data dictionary, model card và runbook.
- 30.4 — Demo khởi động sạch, lỗi có chủ ý, phục hồi và rollback.
- 30.5 — Ôn SQL, PySpark, ML, MLOps, API, RAG và phỏng vấn thiết kế hệ thống.

Các ý trên giữ phạm vi phần 30 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Nếu dữ liệu tăng 10 lần, đo gì đầu tiên?
2. Tái tạo prediction cũ cần những version nào?
3. RAG sai thì phân biệt lỗi retrieval và generation ra sao?

## Đọc thêm từ nguồn chính thức

- [Spark guide](https://spark.apache.org/docs/3.5.7/)
- [MLflow guide](https://mlflow.org/docs/2.22.0/index.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
