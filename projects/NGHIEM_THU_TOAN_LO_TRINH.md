# Nghiệm thu toàn lộ trình ngày 150

[Lịch đầy đủ](../LO_TRINH_DAY_DU.md)

Có 30 buổi nền và 120 buổi nối tiếp, không tự chứng nhận đã thành thạo chỉ vì đọc đủ file. Nghiệm thu theo đầu ra đã tự làm và kiểm tra; buổi chưa đạt được học thêm.

## Ba dự án chính

- [ ] [Dữ liệu và feature](02-data-features/README.md): khóa/thời gian/quality/rerun/stream restart đúng.
- [ ] [ML/MLOps/API](03-mlops-serving/README.md): model có version, đánh giá đúng, tracking/test/DAG/container/deploy/rollback/monitoring và phục vụ thật.
- [ ] [RAG/workflow](04-rag-workflow/README.md): index/dense/generation/eval/citation/ACL/trace/tool budget có bằng chứng.

## Rubric gợi ý từ tài liệu gốc

| Năng lực | Điểm tối đa | Điểm tự chấm | Bằng chứng |
| --- | --- | --- | --- |
| Spark và tính đúng dữ liệu | 20 | | |
| Thực thi và hiệu năng | 15 | | |
| ML và đánh giá | 15 | | |
| MLOps và tái lập | 20 | | |
| API và vận hành | 10 | | |
| RAG và workflow | 15 | | |
| Tài liệu và giải thích | 5 | | |

80/100 là mốc tự đánh giá học tập. Leakage, rerun tạo trùng, secret trong repo hoặc truy xuất sai quyền phải sửa dù tổng điểm cao. Chưa có bằng chứng thì chưa chấm đầy đủ.

## Demo 10 phút

1. Bài toán và kiến trúc, nguồn giả lập: 2 phút.
2. Tính đúng dữ liệu, fixture và một lỗi được test bắt: 3 phút.
3. Run/model version, API và rollback: 2 phút.
4. RAG có citation, thiếu nguồn và quyền: 2 phút.
5. Giới hạn và đo gì nếu dữ liệu/lưu lượng tăng10 lần: 1 phút.

## Phạm vi mở rộng

Cloud có phí/GPU lớn/train LoRA là nhánh mở rộng theo tài liệu gốc. Quyết định kỹ thuật và kế hoạch đánh giá là cốt lõi; chỉ ghi đã train/deploy khi thực sự làm. Deployment core có thể dùng Spark Standalone local. Nhiều container vẫn là một máy, không gọi là đã kiểm chứng cluster nhiều máy chịu lỗi.

## Điều kiện chốt

- [ ] Clean run theo README từ môi trường/output mới, không xóa bài làm để thử.
- [ ] Dependency, code, data, config, model/prompt/index version đầy đủ.
- [ ] Có data dictionary, model card, release manifest và runbook.
- [ ] Mỗi claim chất lượng/tốc độ có số liệu, máy, dataset/split và giới hạn.
- [ ] Tự giải thích code/đánh đổi; liệt kê các chỗ cần học sâu tiếp.
