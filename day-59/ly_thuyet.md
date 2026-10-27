# Ngày 59 — Chia tập thời gian và test chống leakage

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Chia tập thời gian và test chống leakage”. Kết quả cần đạt: Three snapshot mỗi tập 120 dòng, ngày không lẫn; có test biên thời gian.

## Từ mới gắn với bài này

- **Leakage (rò rỉ thông tin vào học máy)**.
- **Temporal split (chia tập theo thời gian)**.
- **Group split (chia theo nhóm đối tượng)**.

## Tình huống và cách hiểu

**Leakage (rò rỉ thông tin vào học máy)** có thể đến từ sự kiện tương lai, preprocessing học từ test hoặc các bản gần trùng qua hai tập. **Temporal split (chia tập theo thời gian)** phù hợp dự đoán kỳ tương lai; **group split (chia theo nhóm đối tượng)** phù hợp kiểm tra khách chưa từng gặp.

Bài chọn train cutoff 1/2, validation 1/4, test 1/6 năm 2025. Các cửa sổ nhãn không chồng; cùng khách xuất hiện ở nhiều kỳ vì mục tiêu là dự đoán tương lai cho khách hiện hữu. Đánh giá khách mới cần nhóm chia khác.

Seed chỉ cố định một phần ngẫu nhiên. Nó không sửa cách chia sai. Ghi hash nguồn và chỉ dùng validation chọn feature/threshold; test giữ tới khi chốt quyết định.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-059/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
frames = {name: snapshot_pd(day) for name, day in [("train", "2025-02-01"), ("validation", "2025-04-01"), ("test", "2025-06-01")]}
for name, frame in frames.items():
    print(name, frame.shape, frame["snapshot_date"].unique().tolist())
print("Hash nguồn:", data_hash())
```

## Đọc từng phần của ví dụ

Snapshot tham chiếu dùng cùng quy tắc as-of. Mỗi tập 120 khách tại một ngày khác nhau.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Three snapshot mỗi tập 120 dòng, ngày không lẫn; có test biên thời gian.

## Ba câu kiểm tra hiểu bài

1. Leakage có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: rò rỉ thông tin vào học máy.
- Luồng chính: Snapshot tham chiếu dùng cùng quy tắc as-of. Mỗi tập 120 khách tại một ngày khác nhau.
- Đối chiếu tiêu chí: Three snapshot mỗi tập 120 dòng, ngày không lẫn; có test biên thời gian. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 11 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
