# Dự án 2 — Hệ ML có MLOps và API

[Lịch đầy đủ](../../LO_TRINH_DAY_DU.md) · [Ngày nghiệm thu 120](../../day-120/README.md)

Mở rộng feature dự án 1. Giữ hai artifact riêng: Spark PipelineModel cho batch và sklearn Pipeline cho API. Không xem một artifact thay cho cả hai runtime. Gộp các ngày 61–120, mỗi phần đã luyện riêng trước khi tích hợp.

Các file services là tham chiếu có thể chạy. Nghiệm thu cần code bạn hiểu, test và bằng chứng đầu ra, không chỉ file tồn tại.

## Tiêu chí nghiệm thu

- [ ] Baseline và ít nhất hai cấu hình, preprocessing chỉ fit train, threshold chọn validation; test giữ riêng.
- [ ] Năm training run thật trong MLflow với source/code/split/config/metric/model và input contract.
- [ ] Load model trong tiến trình mới; score fixture trước/sau khớp trong tolerance.
- [ ] Batch prediction có customer/snapshot/model_version/run/source; khóa duy nhất khi rerun.
- [ ] CLI, unit/integration test có ca biên; CI chạy fixture không cần secret/dữ liệu riêng.
- [ ] Airflow DAG thật: validate/features/train/evaluate/score, retry/timeout/gate/backfill không nhân dữ liệu.
- [ ] Docker build/run và volume thật; một môi trường deploy local Standalone có executor/worker thực.
- [ ] API model thật có validation/auth/readiness, chặn lỗi đầu vào và model thiếu; không fit trong request.
- [ ] Load test thật có warm-up, p95/throughput/lỗi/số mẫu/phần cứng, kiểm tra score không đổi.
- [ ] Release manifest/promote/rollback, monitoring quality/freshness/drift và performance khi nhãn đủ.
- [ ] Candidate không đạt giữ previous; từ prediction truy về được model/run/data/code.

## Ca phải demo

1. Validate sai schema chặn train/score.
2. Feature lỗi tạm thời retry không nhân dòng; schema sai không retry vô hạn.
3. Missing model ready=503, wrong key=401, input âm=422.
4. Candidate rejected không được promote; rollback có response version cũ sau restart.
5. Nhánh cloud chỉ đánh dấu deployed khi đã thực sự triển khai và kiểm tra quyền/ngân sách.

## Nơi tự làm và ghi bằng chứng

Gom code của các ngày vào dự án hoặc liên kết tới module gốc. Không cần chép lặp mọi file. Đầu ra dùng artifacts/full và manifest riêng, không sửa source fixtures hoặc bản lưu.

| Hạng mục | Lệnh / code / version | Kết quả / log | Đã chạy hay mới thiết kế |
| --- | --- | --- | --- |
| Dữ liệu và cấu hình | ... | ... | ... |
| Tính đúng / chất lượng | ... | ... | ... |
| Test và ca lỗi | ... | ... | ... |
| Phục hồi / chạy lại | ... | ... | ... |
| Clean run | ... | ... | ... |

## Hướng dẫn cần hoàn thiện

- Điều kiện môi trường và phiên bản:
- Lệnh chạy từng bước:
- Nguồn/hash, model/prompt/index version:
- Expected output và cách đối chiếu:
- Ba lỗi thường gặp, kiểm tra và phục hồi:
- Phần chưa chạy, giới hạn tài nguyên và việc học tiếp:
