# Dự án 1 — Pipeline dữ liệu và feature đúng thời điểm

[Lịch đầy đủ](../../LO_TRINH_DAY_DU.md) · [Ngày nghiệm thu 60](../../day-60/README.md)

Dùng data/raw/customers.csv và events.csv giả lập. Feature [cutoff−30 ngày,cutoff), ingested_at<cutoff; nhãn churn=1 khi không purchase trong [cutoff,cutoff+30 ngày) và đã quan sát đủ. Snapshot train/validation/test là 2025-02-01/04-01/06-01.

Các ngày 31–60 cung cấp từng phần. Bài làm của bạn cần ghép thành CLI có ngày nguồn/đích rõ; không chỉ chạy helper tham chiếu.

## Tiêu chí nghiệm thu

- [ ] Schema/data dictionary, đơn vị VND và UTC, khóa nguồn/đích rõ.
- [ ] Clean/quarantine theo lý do, đối soát số dòng và tiền; không bỏ mất dữ liệu lỗi.
- [ ] Join không nhân tiền; dedup phiên bản có quy tắc và đúng thời điểm sẵn có.
- [ ] Incremental/backfill/rerun không nhân khóa; source/sink độc lập khi overwrite.
- [ ] Stream file có checkpoint, restart và kịch bản late data; giải thích watermark/state/giới hạn exactly-once.
- [ ] Ba snapshot ×120 khách, khóa customer_id/snapshot_date duy nhất; giữ cả khách không event.
- [ ] Test future event, late ingestion, đúng cutoff và thiếu cửa sổ nhãn.
- [ ] So Spark với reference theo khóa/tolerance; báo cáo baseline và một thay đổi hiệu năng có plan/UI.

## Ca phải demo

1. Một file timestamp/amount sai.
2. Một ngày thiếu nguồn và một sự kiện tới muộn.
3. Cùng interval chạy lại không nhân dòng.
4. Một khóa dimension trùng bị chặn.
5. Feature tiny: C001=2/300000/12/churn0; C002=1/50000/17/churn1; C003=0/0/NULL/churn1.

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
