# Ngày 123 — Structured output và validation lỗi

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Structured output và validation lỗi”. Kết quả cần đạt: Parser chặn hai mẫu lỗi; bạn còn kiểm tra nội dung theo nguồn.

## Từ mới gắn với bài này

- **Structured output (đầu ra có cấu trúc)**.
- **Schema validation (kiểm tra theo lược đồ)**.
- **Refusal / Error (từ chối / lỗi)**.

## Tình huống và cách hiểu

**Structured output (đầu ra có cấu trúc)** giúp ứng dụng đọc trường. **Schema validation (kiểm tra theo lược đồ)** bắt sai kiểu, thiếu trường hoặc số âm, nhưng không biết 999999 có đúng trong tài liệu nguồn hay không.

Phân biệt **refusal / error (từ chối / lỗi)** với đầu ra đúng schema nhưng sai nội dung. Không sửa JSON lỗi thành câu trả lời mặc định rồi tính như thành công. Retry tối đa số lần đã chốt và có trạng thái cuối.

Ví dụ dùng chuỗi đầu ra giả lập để test parser, không gọi nó là đánh giá LLM. Tới ngày 124, nối cùng validator vào model thật để tách lỗi generation và lỗi phần mềm.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-123/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from pydantic import BaseModel, ConfigDict, Field, ValidationError
class Order(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    order_id: str | None
    amount_vnd: int | None = Field(ge=0)
for raw in ['{"order_id":"A01","amount_vnd":120000}', '{"order_id":"A01","amount_vnd":-1}', 'not json']:
    try:
        print(Order.model_validate_json(raw))
    except ValidationError as error:
        print("Parser rejected:", error.error_count())
```

## Đọc từng phần của ví dụ

Ba chuỗi kiểm tra parser độc lập. Validation thành công chưa xác nhận đúng dữ kiện.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Parser chặn hai mẫu lỗi; bạn còn kiểm tra nội dung theo nguồn.

## Ba câu kiểm tra hiểu bài

1. Structured output có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đầu ra có cấu trúc.
- Luồng chính: Ba chuỗi kiểm tra parser độc lập. Validation thành công chưa xác nhận đúng dữ kiện.
- Đối chiếu tiêu chí: Parser chặn hai mẫu lỗi; bạn còn kiểm tra nội dung theo nguồn. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 24 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
