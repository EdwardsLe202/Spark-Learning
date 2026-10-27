# Ngày 93 — Retry timeout và gate không được bỏ qua

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Retry timeout và gate không được bỏ qua”. Kết quả cần đạt: Candidate rejected không được score; có timeout/retry hữu hạn và log nguyên nhân.

## Từ mới gắn với bài này

- **Retry policy (chính sách thử lại)**.
- **Timeout (giới hạn thời gian)**.
- **Failure propagation (truyền trạng thái thất bại)**.

## Tình huống và cách hiểu

**Retry policy (chính sách thử lại)** phân loại lỗi tạm thời và lỗi dữ liệu. **Timeout (giới hạn thời gian)** chặn task treo. **Failure propagation (truyền trạng thái thất bại)** làm các bước phụ thuộc không chạy như thể đầu vào đã đạt.

Không retry schema sai mãi. Gate model không đạt cần giữ candidate rejected và không phát hành. Nếu muốn tiếp tục dùng model cũ, thiết kế nhánh rõ ràng, không nuốt lỗi rồi gắn nhãn thành công cho model mới.

Mẫu đặt min_ap vượt mọi giá trị hợp lệ để cố ý từ chối candidate trong lab. Không dùng ngưỡng này như khuyến nghị kinh doanh. Kiểm tra evaluate thất bại và score bị chặn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-093/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from services.pipeline import run_step
version = "rejected-demo"
run_step("train", version=version)
try:
    run_step("evaluate", version=version, min_ap=1.1)
except ValueError as error:
    print("Candidate bị từ chối:", error)
try:
    run_step("score", version=version)
except ValueError as error:
    print("Score bị chặn:", error)
```

## Đọc từng phần của ví dụ

Min_ap=1.1 là lỗi chủ ý để test gate. Evaluation lưu accepted=false trước khi báo lỗi.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Candidate rejected không được score; có timeout/retry hữu hạn và log nguyên nhân.

## Ba câu kiểm tra hiểu bài

1. Retry policy có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: chính sách thử lại.
- Luồng chính: Min_ap=1.1 là lỗi chủ ý để test gate. Evaluation lưu accepted=false trước khi báo lỗi.
- Đối chiếu tiêu chí: Candidate rejected không được score; có timeout/retry hữu hạn và log nguyên nhân. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 17 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
