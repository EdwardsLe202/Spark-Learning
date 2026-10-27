# Ngày 28 — Lý thuyết: Tool calling và workflow có tác nhân

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Xây bộ gọi công cụ chỉ đọc với validation, allowlist và giới hạn số bước.

## 1. Model đề xuất, ứng dụng quyết định
**Tool calling (đề xuất sử dụng công cụ qua đầu ra có cấu trúc)** không có nghĩa model được thực thi lệnh tùy ý. Ứng dụng nhận tên công cụ và tham số, kiểm tra schema, quyền và hạn mức rồi mới gọi. **Allowlist (danh sách công cụ được phép)** như search_docs và get_job_status giúp giới hạn bề mặt hành động.

**Workflow (luồng bước được định trước)** có thể luôn tìm tài liệu rồi lấy trạng thái. **Agent loop (vòng lặp tác nhân chọn bước tiếp theo)** cho model quyết định trong phạm vi cho phép. Nếu bài toán luôn có hai bước cố định, workflow dễ kiểm thử và dự đoán chi phí hơn. Chỉ thêm loop khi có bằng chứng cần lựa chọn động.

## 2. Kiểm tra cả tham số và kết quả
Schema bắt trường sai kiểu; kiểm tra miền giá trị và quyền ở server bắt hành vi sai. Không dùng eval, exec hoặc shell cho đầu ra model. Công cụ trả dữ liệu cũng là nguồn không tin cậy: kiểm tra định dạng, độ dài và trạng thái. **Read-only tool (công cụ chỉ đọc)** của lab truy vấn bảng trạng thái giả lập, không chạm dữ liệu thật.

**Step budget (giới hạn số bước)**, timeout và retry tối đa phải có điều kiện dừng rõ. Lỗi tạm thời có thể retry hữu hạn; tên công cụ ngoài danh sách phải từ chối. Không ghi chung “lỗi công cụ” cho mọi trường hợp vì khó điều tra.

## 3. Đánh giá toàn tác vụ
**Task success rate (tỷ lệ hoàn thành đúng tác vụ)** cần chấm cả đáp án, công cụ đúng và quyền đúng. Trace chứa đề xuất model, quyết định validator, kết quả công cụ và lý do dừng. Kết quả có câu trả lời đúng nhưng đã gọi công cụ ngoài quyền vẫn là thất bại. Công cụ ghi dữ liệu đòi hỏi thiết kế quyền riêng; lab này chỉ dùng trạng thái giả lập và tìm kiếm tài liệu.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
from pydantic import BaseModel, ConfigDict, Field
class StatusArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    job_id: str = Field(pattern=r"^job-[0-9]{3}$")
STATUSES = {"job-001": "succeeded", "job-002": "failed"}
def get_job_status(args):
    parsed = StatusArgs.model_validate(args)
    return {"job_id": parsed.job_id, "status": STATUSES.get(parsed.job_id, "not_found")}
print(get_job_status({"job_id": "job-001"}))
# TODO: dispatcher theo allowlist, kiểm tra quyền, timeout và tối đa 3 bước.
```

## Năm ý đối chiếu với lộ trình gốc

- 28.1 — Tool calling, schema công cụ, workflow cố định và agent loop.
- 28.2 — Kiểm tra tham số, xử lý lỗi, timeout và phân loại lỗi có thể retry.
- 28.3 — Giới hạn số bước, token, thời gian và chi phí; điều kiện dừng.
- 28.4 — Công cụ chỉ đọc, quyền tối thiểu và xác nhận cho hành động ảnh hưởng dữ liệu.
- 28.5 — Đánh giá thành công của tác vụ, trace và kiểm thử tình huống công cụ trả dữ liệu xấu.

Các ý trên giữ phạm vi phần 28 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Tool call khác thực thi công cụ thế nào?
2. Khi nào workflow cố định đủ dùng?
3. Nếu tool lặp vô hạn thì tầng nào phải dừng?

## Đọc thêm từ nguồn chính thức

- [OWASP GenAI security](https://genai.owasp.org/)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
