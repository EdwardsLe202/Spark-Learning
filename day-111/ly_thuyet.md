# Ngày 111 — Sync async queue và công việc CPU

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Sync async queue và công việc CPU”. Kết quả cần đạt: Có thiết kế không chặn API bởi job dài; không gọi asyncio là cơ chế tăng năng lực CPU.

## Từ mới gắn với bài này

- **Synchronous / Asynchronous (đồng bộ / bất đồng bộ)**.
- **Queue (hàng đợi)**.
- **CPU-bound / IO-bound (nặng tính toán / chờ vào ra)**.

## Tình huống và cách hiểu

**Synchronous / asynchronous (đồng bộ / bất đồng bộ)** nói cách chờ và phối hợp công việc. **CPU-bound / IO-bound (nặng tính toán / chờ vào ra)** cần chiến lược khác nhau. Đổi def thành async không tự làm tính toán CPU nhanh hơn.

**Queue (hàng đợi)** phù hợp job dài có job_id/status thay vì giữ request mở vô hạn. Cần giới hạn queue, timeout, retry và nơi lưu trạng thái; asyncio queue trong process chưa là hàng đợi bền vững sau restart.

Mẫu chỉ mô phỏng hai lần chờ bằng asyncio.sleep để thấy concurrency cho I/O, không gửi request tới dịch vụ ngoài. Lab áp dụng vào tác vụ giả lập có thời gian giới hạn và không nhét SparkSession vào từng endpoint.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-111/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import asyncio
from time import perf_counter
async def fake_io(name):
    await asyncio.sleep(0.02)
    return name
async def run():
    return await asyncio.gather(fake_io("a"), fake_io("b"))
start = perf_counter()
print(asyncio.run(run()), "seconds:", perf_counter() - start)
print("Đây là chờ I/O giả lập, chưa benchmark tính toán CPU.")
```

## Đọc từng phần của ví dụ

Gather cho hai việc chờ phối hợp; sleep là mô phỏng, không là inference model.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có thiết kế không chặn API bởi job dài; không gọi asyncio là cơ chế tăng năng lực CPU.

## Ba câu kiểm tra hiểu bài

1. Synchronous / Asynchronous có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đồng bộ / bất đồng bộ.
- Luồng chính: Gather cho hai việc chờ phối hợp; sleep là mô phỏng, không là inference model.
- Đối chiếu tiêu chí: Có thiết kế không chặn API bởi job dài; không gọi asyncio là cơ chế tăng năng lực CPU. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 21 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
