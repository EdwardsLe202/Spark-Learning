# Ngày 75 — Đánh giá theo nhiều fold thời gian

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Đánh giá theo nhiều fold thời gian”. Kết quả cần đạt: Có protocol không dùng test để lựa chọn; mọi fold chỉ fit thống kê từ train của fold.

## Từ mới gắn với bài này

- **Temporal fold (cặp train và validation theo thời gian)**.
- **Gap (khoảng cách để tránh cửa sổ chồng)**.

## Tình huống và cách hiểu

**Temporal fold (cặp train và validation theo thời gian)** phải giữ việc học xảy ra trước phần cần đánh giá. **Gap (khoảng cách để tránh cửa sổ chồng)** cần xét cả cửa sổ nhãn, không chỉ thứ tự snapshot_date.

Trong bộ dữ liệu này, có thể dùng train 1/2 → validate 1/4, rồi train 1/2+1/4 → validate 1/6 để nghiên cứu quy trình. Nếu dùng tháng 6 làm validation của fold để chọn cấu hình, nó không còn là test cuối; cần một holdout mới hoặc ghi test đã được dùng.

Bài mẫu chỉ in thiết kế fold, không âm thầm đổi mục đích test. Lab phải chốt một eval protocol trước khi chạy, lưu tập nào dùng để chọn và tập nào chỉ chấm cuối.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-075/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
folds = [{"train": ["2025-02-01"], "validation": "2025-04-01"}]
protocol = {"selection_folds": folds, "final_test": "2025-06-01", "label_horizon_days": 30}
write_json(out / "protocol.json", protocol)
print(protocol)
```

## Đọc từng phần của ví dụ

Test tháng 6 giữ riêng. Muốn thêm fold chọn cấu hình cần thêm dữ liệu đủ quan sát, không tái dùng test rồi vẫn gọi là độc lập.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có protocol không dùng test để lựa chọn; mọi fold chỉ fit thống kê từ train của fold.

## Ba câu kiểm tra hiểu bài

1. Temporal fold có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: cặp train và validation theo thời gian.
- Luồng chính: Test tháng 6 giữ riêng. Muốn thêm fold chọn cấu hình cần thêm dữ liệu đủ quan sát, không tái dùng test rồi vẫn gọi là độc lập.
- Đối chiếu tiêu chí: Có protocol không dùng test để lựa chọn; mọi fold chỉ fit thống kê từ train của fold. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 13 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
