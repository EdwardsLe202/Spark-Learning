# Dự án 2 — Hệ thống churn có MLOps

[Các dự án](../README.md) · [Ngày 23](../../day-23/README.md)

Mở rộng dự án 1 thành train → evaluate → chọn candidate → batch score → API → monitor. Giữ **hai artifact riêng**: Spark PipelineModel cho batch và sklearn Pipeline cho API. Ghi version, metric và contract riêng cho mỗi nhánh.

## Nơi gom code từ ngày 16

Tạo `churn/` có __init__.py và các module features.py, train.py, evaluate.py, predict.py, cli.py. Tạo `tests/` dùng fixture nhỏ. Không để logic chạy toàn pipeline ngay khi import module. Nếu chưa refactor, liên kết file của ngày tương ứng và ghi rõ giới hạn.

## Tiêu chí cốt lõi

- [ ] Split và preprocessing tuân thủ dự án 1; test không dùng chọn model/threshold.
- [ ] Baseline và ít nhất hai cấu hình, metric có định nghĩa và báo cáo theo nhóm.
- [ ] Năm training run thật trong MLflow: parameter, validation metric, data hash, code reference, model và schema.
- [ ] Model được load trong tiến trình mới, prediction trên fixture tương đương.
- [ ] Batch score 120 khách hàng, có snapshot_date, model_version, run_id và khóa chống trùng.
- [ ] Workflow validate/features/train/evaluate/score có dependency, retry hữu hạn, timeout và backfill.
- [ ] CI chạy được kiểm tra repo và test nghiệp vụ bạn đã thêm.
- [ ] API sklearn có validation, /health, /ready và /predict; score khớp gọi trực tiếp.
- [ ] Load test có p95, throughput, lỗi, lượng mẫu, concurrency và cấu hình máy.
- [ ] Monitoring phân biệt schema lỗi, drift và metric có nhãn.
- [ ] Candidate không đạt bị từ chối; rollback có log và version cũ được khôi phục.

## Phần mở rộng cần ghi mức kiểm chứng

| Hạng mục | Thiết kế / chạy local / triển khai thật | Bằng chứng |
| --- | --- | --- |
| Airflow DAG và scheduler | Chưa làm | ... |
| Docker image và volume | Chưa làm | ... |
| Cluster hoặc cloud | Chưa làm | ... |
| Release staging và rollout | Chưa làm | ... |

Không đánh dấu hoàn thành thực hành đầy đủ của tài liệu gốc cho Airflow/Docker/cloud nếu mới mô phỏng bằng Python local.

## Tình huống demo

1. Validate lỗi làm score không chạy.
2. Features lỗi một lần, retry không tạo trùng.
3. Model load ở tiến trình mới không cần notebook.
4. Request thiếu/sai trường bị chặn; category mới được xử lý theo contract.
5. Candidate kém bị từ chối; phục hồi version previous.

## Tài liệu bạn cần hoàn thiện

- Lệnh clean run: ...
- MLflow URI / run_id / model version: ...
- Model card: mục đích, đầu vào, split, metric, threshold, giới hạn dữ liệu giả lập: ...
- Release manifest, log rollback: ...
- Runbook cho dữ liệu lỗi và API không ready: ...
- Báo cáo tải và monitoring: ...

