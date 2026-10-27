# Ngày 94 — Backfill Airflow data interval và giới hạn tài nguyên

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Backfill Airflow data interval và giới hạn tài nguyên”. Kết quả cần đạt: 120 dòng mỗi lượt, cùng ngày dữ liệu; không truyền bảng lớn qua XCom.

## Từ mới gắn với bài này

- **Logical date (mốc logic của lần chạy)**.
- **Catchup (tạo bù các kỳ chưa chạy)**.
- **Pool (nhóm giới hạn số task)**.

## Tình huống và cách hiểu

**Logical date (mốc logic của lần chạy)** và data interval không phải thời điểm bấm chạy. **Catchup (tạo bù các kỳ chưa chạy)** có thể tạo nhiều lần chạy lịch sử; chỉ bật sau khi task đã idempotent và phạm vi dữ liệu rõ.

**Pool (nhóm giới hạn số task)** và max_active_runs giúp tránh nhiều job cùng tranh tài nguyên/ghi đích. DAG mẫu ban đầu schedule=None để bạn chủ động chọn snapshot dữ liệu giả lập. Không bật lịch năm hiện tại rồi tự gán nhãn cho nguồn đã kết thúc năm 2025.

Backfill phải truyền đúng ngày, version và nguồn. Mẫu gọi lại hai bước cho cùng snapshot, còn lab chạy cùng interval trên Airflow và kiểm tra số dòng/hash không nhân. XCom chỉ giữ metadata nhỏ.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-094/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from services.pipeline import run_step
for _ in range(2):
    print(run_step("validate", snapshot_date="2025-04-01", version="backfill-demo"))
    print(run_step("features", snapshot_date="2025-04-01", version="backfill-demo")["rows"])
```

## Đọc từng phần của ví dụ

Lần chạy thực hiện hôm nay nhưng dữ liệu của ngày 1/4/2025. Đích cùng snapshot được ghi thay có chủ đích.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

120 dòng mỗi lượt, cùng ngày dữ liệu; không truyền bảng lớn qua XCom.

## Ba câu kiểm tra hiểu bài

1. Logical date có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mốc logic của lần chạy.
- Luồng chính: Lần chạy thực hiện hôm nay nhưng dữ liệu của ngày 1/4/2025. Đích cùng snapshot được ghi thay có chủ đích.
- Đối chiếu tiêu chí: 120 dòng mỗi lượt, cùng ngày dữ liệu; không truyền bảng lớn qua XCom. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 17 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
