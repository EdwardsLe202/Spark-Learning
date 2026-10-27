# Kiểm tra bộ học khi biên soạn

[Lộ trình](../README.md)

Các kiểm tra dưới đây dành cho tài liệu, fixture và ví dụ khởi động. Bài tự làm của người học vẫn còn TODO; kết quả này không chứng nhận bạn đã hoàn thành lab hay ba dự án.

## Đã kiểm tra

- Đủ 30 thư mục, mỗi ngày 4 Markdown và 1 file Python.
- Đủ 150 ý đối chiếu với tài liệu gốc; liên kết local và cú pháp các file Python/đoạn ví dụ đều hợp lệ tại lúc biên soạn.
- Hash, số dòng và khóa của fixture; tổng tiền tiny; bảng feature/nhãn tính tay; đủ cửa sổ quan sát của ba snapshot.
- Corpus 8 tài liệu; eval 40 câu, đúng nhóm, split và nhãn tài liệu.
- Chạy thành công 28 ví dụ khởi động: ngày 01–17, 19–22 và 24–30. Các ví dụ Spark đã chạy với Python 3.11.15, Java 17.0.19 và PySpark 3.5.7 trên macOS Apple Silicon.
- Ngày 15 tạo được run, log parameter/tag và manifest vào MLflow 2.22.0 với SQLite sau khi cố định SQLAlchemy 2.0.40.
- Ngày 21: `/health` và schema đầu vào hợp lệ/lỗi được kiểm tra riêng.
- Ngày 22: ví dụ PyTorch 2.6.0 CPU có shape [4,1] và loss cuối nhỏ hơn ban đầu.
- Bộ requirements AI giải được dependency; chưa tải embedding/generation model để benchmark.

## Phần cần người học hoàn thiện rồi kiểm tra

- Ví dụ ngày 18 cần PipelineModel do bạn lưu ở ngày 12. Không tạo model thay người học để bỏ qua điều kiện này.
- Ví dụ gửi tải ngày 23 cần `/predict` hoàn chỉnh từ ngày 21, nên chưa chạy benchmark endpoint này trong kiểm tra bộ học.
- Các bước full lab, test nghiệp vụ, DAG/scheduler, Docker, cluster/cloud, dense retrieval, generation, đánh giá chất lượng LLM và LoRA cần thực hiện theo đề. Không có số liệu chất lượng được tạo thay cho các bước đó.

## Lệnh kiểm tra lại bộ học

```bash
python scripts/check_repo.py
```

Lệnh này dùng thư viện chuẩn Python, không khởi động Spark hoặc dịch vụ ngoài, không ghi đè bài làm. Khi bạn thêm code/test/dữ liệu mới, tự bổ sung kiểm tra nghiệp vụ; bộ kiểm tra cấu trúc không thay chúng.
