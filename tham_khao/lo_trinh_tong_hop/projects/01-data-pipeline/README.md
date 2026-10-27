# Dự án 1 — Pipeline dữ liệu và đặc trưng

[Các dự án](../README.md) · [Ngày 11](../../day-11/README.md)

Chứng minh dữ liệu được xử lý đúng, chạy lại có kiểm soát và feature không dùng thông tin tương lai. Dùng customers/events giả lập và quy ước thời gian ở [data/README.md](../../data/README.md).

## Công việc tích lũy

| Ngày | Công việc | Nơi điền bằng chứng của bạn |
| --- | --- | --- |
| 04–05 | Parse, schema, clean, quarantine, đối soát | Code / lệnh / báo cáo: ... |
| 06 | Join đúng cardinality, dedup có quy tắc | Code / test: ... |
| 07–08 | Parquet, partition, shuffle | Plan / output: ... |
| 09 | Baseline và một thay đổi hiệu năng | Bảng thời gian / cấu hình: ... |
| 10 | Incremental, backfill, retry, stream checkpoint | Log rerun / restart: ... |
| 11 | Feature, nhãn và split theo thời gian | Hàm / snapshot / test: ... |

## Đầu ra tối thiểu

- [ ] Clean và quarantine có lý do, tổng tiền/số dòng đối soát được.
- [ ] Feature events_30d, spend_30d, recency_days theo cutoff và thời điểm sẵn có dữ liệu.
- [ ] Nhãn churn có cửa sổ đủ 30 ngày; không gán churn khi chưa đủ quan sát.
- [ ] Ba snapshot train/validation/test, mỗi snapshot 120 khóa duy nhất.
- [ ] Một lệnh nhận ngày dữ liệu, ghi đúng partition và rerun không nhân đôi.
- [ ] Test trên tiny phát hiện tương lai, ingested_at muộn, khóa trùng và join nhân tiền.
- [ ] Data dictionary và báo cáo trước/sau tối ưu có số liệu đo thật.

## Tình huống phải thử

1. File có amount sai kiểu hoặc timestamp sai: bị cách ly/chặn theo policy.
2. Thiếu một ngày: pipeline báo thiếu nguồn thay vì tạo số liệu giả.
3. Event đến muộn: cập nhật đúng ngày có ảnh hưởng, không đổi ngày khác.
4. Cùng ngày chạy hai lần: cùng khóa/số dòng/tổng tiền.
5. Event đúng cutoff: không đi vào feature, có thể đi vào nhãn nếu cửa sổ phù hợp.

## Lệnh tái chạy của bạn

```bash
# Điền lệnh thật cho validate, features và kiểm tra rerun.
```

## Kết quả và giới hạn

- Đường dẫn snapshot và hash: ...
- Kết quả fixture: ...
- Log thử lỗi/phục hồi: ...
- Máy, phiên bản, số dòng, runtime: ...
- Phần local / phần cluster chưa kiểm chứng: ...

