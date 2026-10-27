# Ngày 119 — Timeout retry canary và rollback dịch vụ

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Timeout retry canary và rollback dịch vụ”. Kết quả cần đạt: Vòng lặp dừng không quá 3 lần; rollout/rollback có log và không sửa quyền dữ liệu.

## Từ mới gắn với bài này

- **Canary release (phát hành cho phần nhỏ lưu lượng)**.
- **Shadow traffic (chạy quan sát song song)**.
- **Retry budget (giới hạn thử lại)**.

## Tình huống và cách hiểu

**Canary release (phát hành cho phần nhỏ lưu lượng)** dùng một phần request thật để quan sát candidate. **Shadow traffic (chạy quan sát song song)** chưa dùng output candidate cho quyết định. Cả hai vẫn có chi phí tài nguyên và yêu cầu kiểm soát dữ liệu.

**Retry budget (giới hạn thử lại)** tránh vòng lặp vô hạn và bão retry khi server quá tải. Chỉ retry lỗi tạm thời theo policy; không retry input 422 như lỗi mạng. Tác vụ ghi phải có idempotency.

Mẫu mô phỏng hai lần timeout rồi thành công với số lần giới hạn. Lab áp dụng API/model adapter, thử canary local hai version và xác nhận rollback bằng readiness và version trong response, không chỉ đổi file pointer.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-119/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
attempts = []
for attempt in range(3):
    attempts.append(attempt + 1)
    try:
        if attempt < 2:
            raise TimeoutError("fixture timeout")
        result = "ok"
        break
    except TimeoutError:
        if attempt == 2:
            raise
print({"attempts": attempts, "result": result})
```

## Đọc từng phần của ví dụ

Đây là lỗi giả lập có giới hạn. Bản thật cần timeout theo request và tổng budget, không chỉ giới hạn số vòng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Vòng lặp dừng không quá 3 lần; rollout/rollback có log và không sửa quyền dữ liệu.

## Ba câu kiểm tra hiểu bài

1. Canary release có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: phát hành cho phần nhỏ lưu lượng.
- Luồng chính: Đây là lỗi giả lập có giới hạn. Bản thật cần timeout theo request và tổng budget, không chỉ giới hạn số vòng.
- Đối chiếu tiêu chí: Vòng lặp dừng không quá 3 lần; rollout/rollback có log và không sửa quyền dữ liệu. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 23 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
