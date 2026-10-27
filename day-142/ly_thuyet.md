# Ngày 142 — Tool schema và công cụ chỉ đọc

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Tool schema và công cụ chỉ đọc”. Kết quả cần đạt: job-001 succeeded; input sai bị chặn; job lạ đúng mẫu trả not_found.

## Từ mới gắn với bài này

- **Tool calling (model đề xuất sử dụng công cụ)**.
- **Tool schema (lược đồ tham số công cụ)**.
- **Read-only (chỉ đọc)**.

## Tình huống và cách hiểu

**Tool calling (model đề xuất sử dụng công cụ)** không phải quyền thực thi trực tiếp. Ứng dụng nhận tên/args, kiểm tra **tool schema (lược đồ tham số công cụ)**, quyền và budget rồi mới gọi.

**Read-only (chỉ đọc)** trong lab là get_job_status trên bảng giả lập. Không có database production, không gửi message hoặc sửa dữ liệu thật. Output cũng phải có cấu trúc để không tin mọi text trả về.

Dùng Pydantic tạo schema rồi validate trước dispatch. JSON model có định dạng đúng vẫn có thể xin công cụ ngoài quyền; allowlist và authorization là tầng kiểm tra khác. Không dùng eval/exec để biến text thành Python.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-142/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from pydantic import BaseModel, ConfigDict, Field
from rag_support import get_job_status
class StatusArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    job_id: str = Field(pattern=r"^job-[0-9]{3}$")
print(StatusArgs.model_json_schema())
args = StatusArgs.model_validate({"job_id": "job-001"})
print(get_job_status(args.job_id))
```

## Đọc từng phần của ví dụ

Schema hạn chế mã job, không cho trường thừa. Hàm chỉ đọc fixture, không có hành động ghi.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

job-001 succeeded; input sai bị chặn; job lạ đúng mẫu trả not_found.

## Ba câu kiểm tra hiểu bài

1. Tool calling có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: model đề xuất sử dụng công cụ.
- Luồng chính: Schema hạn chế mã job, không cho trường thừa. Hàm chỉ đọc fixture, không có hành động ghi.
- Đối chiếu tiêu chí: job-001 succeeded; input sai bị chặn; job lạ đúng mẫu trả not_found. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 28 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
