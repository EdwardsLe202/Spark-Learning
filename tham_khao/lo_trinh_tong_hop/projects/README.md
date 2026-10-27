# Ba mốc dự án và cách tự đánh giá

[Lộ trình](../README.md) · [Tiến độ](../TIEN_DO.md)

Các dự án gom công việc từ từng ngày. Chưa cần chép toàn bộ code sang đây ngay; ghi liên kết tới file gốc, rồi tách module khi tới ngày 16. Mỗi tiêu chí chỉ đánh dấu khi có lệnh hoặc kết quả thực chứng minh.

| Mốc | Tích lũy từ | Nghiệm thu | Đặc tả |
| --- | --- | --- | --- |
| 1 | Ngày 02–11 | Ngày 11 | [Pipeline dữ liệu và feature](01-data-pipeline/README.md) |
| 2 | Ngày 12–23 | Ngày 23 | [Hệ thống ML có MLOps](02-mlops/README.md) |
| 3 | Ngày 24–28 | Ngày 30 | [RAG có đánh giá](03-rag/README.md) |

## Rubric (bảng tiêu chí tự chấm)

Giữ trọng số từ lộ trình gốc. Điểm là công cụ học tập, không phải chuẩn tuyển dụng.

| Năng lực | Điểm tối đa | Bằng chứng |
| --- | --- | --- |
| Spark và tính đúng dữ liệu | 20 | Schema, join, window, rerun, test chống leakage |
| Thực thi và hiệu năng | 15 | Plan/UI, baseline, runtime, đầu ra tương đương |
| ML và đánh giá | 15 | Split thời gian, preprocessing train-only, metric, threshold, load model |
| MLOps và tái lập | 20 | Run/version, test, CI, orchestration, rollback |
| API và vận hành | 10 | Validation, readiness, latency, lỗi, log |
| RAG và workflow AI | 15 | Dense retrieval, eval, citation, quyền, trace, công cụ giới hạn |
| Tài liệu và giải thích | 5 | README sạch, lệnh chạy, giới hạn, trả lời đánh đổi |

Tự chấm theo bằng chứng: 0 nếu chưa có; khoảng nửa điểm nếu làm một phần hoặc cần thao tác thủ công chưa ghi lại; điểm đầy đủ khi tái chạy, kiểm tra ca lỗi và giải thích được. Không coi hình UI là bằng chứng đầy đủ cho pipeline.

Mốc gợi ý: 80/100 và không còn lỗi nghiêm trọng về leakage, trùng khi chạy lại, secret trong repo hoặc truy xuất sai quyền. Việc chưa làm Airflow/Docker/cloud/fine-tuning cần ghi đúng phạm vi; không ghi là hoàn thành đầy đủ các phần nâng cao của tài liệu gốc.

## Kịch bản demo 10 phút

1. Kiến trúc và nguồn giả lập: 2 phút.
2. Fixture tính tay, lỗi join/leakage và rerun: 3 phút.
3. Model version, API và rollback: 2 phút.
4. Retrieval, citation, không có nguồn và quyền: 2 phút.
5. Hạn chế và kế hoạch đo khi dữ liệu/lưu lượng tăng: 1 phút.

