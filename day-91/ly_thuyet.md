# Ngày 91 — DAG và dependency của pipeline

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “DAG và dependency của pipeline”. Kết quả cần đạt: Thứ tự validate→features→train→evaluate→score; phân biệt đồ thị và scheduler.

## Từ mới gắn với bài này

- **DAG — Directed Acyclic Graph (đồ thị có hướng không chu trình)**.
- **Dependency (quan hệ bước cần chạy trước)**.

## Tình huống và cách hiểu

**DAG — Directed Acyclic Graph (đồ thị có hướng không chu trình)** mô tả thứ tự task. **Dependency (quan hệ bước cần chạy trước)** làm score chỉ chạy khi features/model/evaluation đã sẵn sàng.

Đồ thị không tự cung cấp scheduler. Mẫu dùng thư viện chuẩn để sắp topo, giúp bạn kiểm tra luồng logic trước khi cài Airflow. Không truyền cả DataFrame qua metadata của task; truyền path, hash, version và trạng thái.

Một DAG có tên đẹp nhưng mọi task chỉ print chưa chứng minh pipeline hoạt động. Tới ngày 92 bạn chạy DAG gọi CLI thật, có lệnh lỗi trả mã khác 0 và gate chặn score.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-091/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from graphlib import TopologicalSorter
parents = {"validate": set(), "features": {"validate"}, "train": {"features"}, "evaluate": {"train"}, "score": {"evaluate"}}
print(list(TopologicalSorter(parents).static_order()))
print("Đây là kiểm tra đồ thị local; chưa chạy scheduler Airflow.")
```

## Đọc từng phần của ví dụ

Mỗi key liệt kê các bước cha. Sort không thực thi train và cũng chưa tạo lịch chạy.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Thứ tự validate→features→train→evaluate→score; phân biệt đồ thị và scheduler.

## Ba câu kiểm tra hiểu bài

1. DAG — Directed Acyclic Graph có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đồ thị có hướng không chu trình.
- Luồng chính: Mỗi key liệt kê các bước cha. Sort không thực thi train và cũng chưa tạo lịch chạy.
- Đối chiếu tiêu chí: Thứ tự validate→features→train→evaluate→score; phân biệt đồ thị và scheduler. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 17 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
