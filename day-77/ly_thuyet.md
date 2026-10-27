# Ngày 77 — Giới hạn trước khi toPandas

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Giới hạn trước khi toPandas”. Kết quả cần đạt: 8 dòng mẫu về driver có kiểm soát; dữ liệu lớn bị chặn trước toPandas.

## Từ mới gắn với bài này

- **Memory budget (ngân sách bộ nhớ)**.
- **Sampling (lấy mẫu có quy tắc)**.

## Tình huống và cách hiểu

ToPandas gom dữ liệu về driver. **Memory budget (ngân sách bộ nhớ)** cần xét số dòng, số cột, kiểu chuỗi và bộ nhớ sau giải nén, không chỉ byte trên đĩa. **Sampling (lấy mẫu có quy tắc)** hoặc tổng hợp trước giúp thu nhỏ.

Mẫu chặn quá 1000 dòng bằng limit(1001). Giới hạn dòng chỉ là hàng rào ban đầu; 1000 cột văn bản rất dài vẫn có thể tốn RAM. Chọn đúng cột trước khi chuyển.

Pandas API on Spark không làm mọi hàm sklearn trở thành phân tán. Train sklearn trong chương trình có Spark vẫn là train một máy nếu thư viện không có cơ chế phân tán riêng. Ghi rõ bước nào thực sự chạy ở đâu.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-077/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
small = orders.select("order_id", "amount").limit(1001)
if small.count() > 1000:
    raise ValueError("Vượt giới hạn số dòng của lab")
local = small.toPandas()
print(local.head())
print("Byte pandas ước lượng:", int(local.memory_usage(deep=True).sum()))
```

## Đọc từng phần của ví dụ

Chọn hai cột, chặn số dòng rồi mới toPandas. Memory_usage chỉ mô tả frame đã chuyển, chưa là peak RAM toàn job.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

8 dòng mẫu về driver có kiểm soát; dữ liệu lớn bị chặn trước toPandas.

## Ba câu kiểm tra hiểu bài

1. Memory budget có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: ngân sách bộ nhớ.
- Luồng chính: Chọn hai cột, chặn số dòng rồi mới toPandas. Memory_usage chỉ mô tả frame đã chuyển, chưa là peak RAM toàn job.
- Đối chiếu tiêu chí: 8 dòng mẫu về driver có kiểm soát; dữ liệu lớn bị chặn trước toPandas. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 14 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
