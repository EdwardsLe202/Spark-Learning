# Ngày 82 — Data contract và quality gate

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Data contract và quality gate”. Kết quả cần đạt: Nguồn chuẩn 120 dòng; các fixture sai bị chặn trước train.

## Từ mới gắn với bài này

- **Data contract (hợp đồng dữ liệu)**.
- **Quality gate (điều kiện chất lượng để đi tiếp)**.

## Tình huống và cách hiểu

**Data contract (hợp đồng dữ liệu)** gồm schema, khóa, miền giá trị, đơn vị và thời gian. **Quality gate (điều kiện chất lượng để đi tiếp)** chặn bước sau khi contract sai, thay vì để model xử lý đầu vào không có ý nghĩa.

Tên cột đúng chưa đủ: customer_id trùng, spend âm hoặc snapshot_date lẫn nhiều kỳ đều có thể làm sai. Chỉ điền thiếu khi quy tắc cho phép; recency thiếu hợp lệ có thể khác amount lỗi.

Viết validate trả báo cáo và ném lỗi khi nghiêm trọng. Dataset nhỏ xác định là đủ để thử, không cần lấy dữ liệu cá nhân. Giữ rejected rows/reasons để không mất dấu.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-082/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
frame = snapshot_pd()
required = set(FEATURES + ["customer_id", "snapshot_date", "label"])
assert required <= set(frame.columns)
assert not frame[["customer_id", "snapshot_date"]].duplicated().any()
assert (frame.spend_30d >= 0).all()
print({"rows": len(frame), "missing_recency": int(frame.recency_days.isna().sum()), "valid": True})
```

## Đọc từng phần của ví dụ

Khóa gồm mã khách và kỳ. Recency NULL được báo chứ không tự coi là lỗi toàn bộ nguồn.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Nguồn chuẩn 120 dòng; các fixture sai bị chặn trước train.

## Ba câu kiểm tra hiểu bài

1. Data contract có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: hợp đồng dữ liệu.
- Luồng chính: Khóa gồm mã khách và kỳ. Recency NULL được báo chứ không tự coi là lỗi toàn bộ nguồn.
- Đối chiếu tiêu chí: Nguồn chuẩn 120 dòng; các fixture sai bị chặn trước train. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 16 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
