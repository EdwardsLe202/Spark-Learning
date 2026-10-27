# Ngày 103 — Giám sát schema missing và độ mới dữ liệu

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Giám sát schema missing và độ mới dữ liệu”. Kết quả cần đạt: Có quality report và ba phản ứng riêng, không đồng nhất mọi cảnh báo thành drift.

## Từ mới gắn với bài này

- **Data freshness (độ mới dữ liệu)**.
- **Missing rate (tỷ lệ thiếu)**.
- **Schema drift (thay đổi lược đồ)**.

## Tình huống và cách hiểu

**Data freshness (độ mới dữ liệu)** đo khoảng cách giữa dữ liệu mới nhất và yêu cầu cập nhật. **Missing rate (tỷ lệ thiếu)** phải có mẫu số và cửa sổ. **Schema drift (thay đổi lược đồ)** có thể làm pipeline không chạy trước khi cần nói tới chất lượng model.

Một job thành công trên file cũ vẫn tạo prediction lỗi thời. Theo dõi runtime/lỗi, số dòng và latest event time cùng feature quality. Không log toàn dữ liệu nhạy cảm để làm dashboard.

Mẫu đo quality snapshot, không khẳng định dữ liệu năm 2025 là fresh cho ngày hiện tại. Lab định nghĩa freshness relative theo data interval giả lập hoặc ghi rõ nguồn lịch sử, tránh dùng đồng hồ hiện tại rồi coi mọi bài đều sự cố.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-103/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
frame = snapshot_pd("2025-04-01")
report = {"rows": len(frame), "snapshot": "2025-04-01", "missing_rate": frame[FEATURES].isna().mean().to_dict(), "duplicate_keys": int(frame[["customer_id", "snapshot_date"]].duplicated().sum())}
write_json(out / "quality_report.json", report)
print(report)
```

## Đọc từng phần của ví dụ

Tỷ lệ thiếu là theo từng cột trên 120 dòng. Recency thiếu có thể hợp lệ theo contract, cần ngưỡng riêng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có quality report và ba phản ứng riêng, không đồng nhất mọi cảnh báo thành drift.

## Ba câu kiểm tra hiểu bài

1. Data freshness có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: độ mới dữ liệu.
- Luồng chính: Tỷ lệ thiếu là theo từng cột trên 120 dòng. Recency thiếu có thể hợp lệ theo contract, cần ngưỡng riêng.
- Đối chiếu tiêu chí: Có quality report và ba phản ứng riêng, không đồng nhất mọi cảnh báo thành drift. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 20 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
