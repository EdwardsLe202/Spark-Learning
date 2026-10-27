# Ngày 83 — Unit test và fixture với pytest

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Unit test và fixture với pytest”. Kết quả cần đạt: Pytest mẫu xanh; có ít nhất một ca âm/biên cho code của bạn.

## Từ mới gắn với bài này

- **Unit test (kiểm thử đơn vị logic)**.
- **Fixture (dữ liệu hoặc thiết lập dùng cho test)**.
- **Parametrization (chạy cùng test với nhiều ca)**.

## Tình huống và cách hiểu

**Unit test (kiểm thử đơn vị logic)** kiểm tra hành vi nhỏ có ý nghĩa. **Fixture (dữ liệu hoặc thiết lập dùng cho test)** phải có ca biên, không chỉ dữ liệu đẹp. **Parametrization (chạy cùng test với nhiều ca)** giúp thử ngưỡng hoặc điều kiện mà không chép nhiều test gần giống.

Test nên bắt được lỗi thật: future event không đổi feature, join không tăng tiền, negative input bị từ chối. Đừng chỉ chép công thức implementation vào assert rồi cho rằng đã kiểm chứng độc lập.

File tests/test_course_contracts.py có các mốc tính tay và test API. Hôm nay đọc một test, cố ý thay một kết quả ở nhánh thử để thấy nó đỏ, rồi sửa lại. Chưa cần dùng toàn bộ framework mock.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-083/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import subprocess
command = [sys.executable, "-m", "pytest", str(ROOT / "tests/test_course_contracts.py"), "-q", "-k", "metric"]
print("Lệnh:", " ".join(command))
subprocess.run(command, cwd=ROOT, check=True)
```

## Đọc từng phần của ví dụ

Chỉ chạy nhóm metric nhỏ trước. Test được cung cấp không tự chứng nhận bài làm của người học.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Pytest mẫu xanh; có ít nhất một ca âm/biên cho code của bạn.

## Ba câu kiểm tra hiểu bài

1. Unit test có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: kiểm thử đơn vị logic.
- Luồng chính: Chỉ chạy nhóm metric nhỏ trước. Test được cung cấp không tự chứng nhận bài làm của người học.
- Đối chiếu tiêu chí: Pytest mẫu xanh; có ít nhất một ca âm/biên cho code của bạn. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 16 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
