# Ngày 21 — Lý thuyết: Backend và API cho hệ thống AI

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Phục vụ model sklearn qua HTTP với validation và kiểm tra đầu vào lỗi.

## 1. Một API là một hợp đồng
**API — Application Programming Interface (giao diện để ứng dụng giao tiếp)** của bài dùng **HTTP — Hypertext Transfer Protocol (giao thức trao đổi yêu cầu và phản hồi)**. **Request (yêu cầu)** gửi JSON, **response (phản hồi)** trả kết quả và **status code (mã trạng thái)**. POST /predict nhận feature và trả score, prediction, model_version cùng request_id.

**Validation (kiểm tra đầu vào theo quy tắc)** dùng Pydantic: events_30d không âm, spend_30d không âm, recency_days có thể thiếu theo chính sách model, region/plan là chuỗi giới hạn độ dài. Sai cấu trúc thường được FastAPI trả 422; lỗi nội bộ trả mã 5xx và thông báo đã kiểm soát. Không trả stack trace hay đường dẫn cá nhân cho client.

## 2. Chuẩn bị model trước khi nhận yêu cầu
**Application lifespan (vòng đời khởi động và kết thúc ứng dụng)** là chỗ load pipeline một lần cho mỗi tiến trình. **Health check (kiểm tra tiến trình còn hoạt động)** khác **readiness check (kiểm tra đã sẵn sàng nhận việc)**: tiến trình sống nhưng model chưa load thì chưa ready. Không train hoặc mở SparkSession trong từng request.

**Authentication (xác thực danh tính)** khác **authorization (kiểm tra quyền thực hiện hành động)**. **Rate limit (giới hạn tần suất)**, **payload limit (giới hạn kích thước đầu vào)** và timeout bảo vệ khả năng phục vụ. Demo chạy loopback local; quyền dùng dịch vụ thật cần được thiết kế riêng.

## 3. Sync và async
**Synchronous execution (thực thi đồng bộ)** chờ một bước xong; **asynchronous execution (thực thi bất đồng bộ)** cho phép không chặn lúc chờ I/O theo cơ chế phù hợp. Gắn async vào phép tính CPU nặng không tự tạo thêm năng lực tính toán. Công việc lâu nên vào **queue (hàng đợi)** và có trạng thái job. Trong bài này, endpoint sync là khởi đầu hợp lý cho model nhỏ.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class PredictionRequest(BaseModel):
    events_30d: int = Field(ge=0)
    spend_30d: float = Field(ge=0)
    recency_days: float | None = Field(default=None, ge=0)
    region: str = Field(min_length=1, max_length=20)
    plan: str = Field(min_length=1, max_length=20)
@app.get("/health")
def health():
    return {"status": "alive"}
# TODO: load model sklearn trong lifespan; thêm /ready và POST /predict.
```

## Năm ý đối chiếu với lộ trình gốc

- 21.1 — HTTP, request, response, status code, JSON và API contract.
- 21.2 — FastAPI, validation, schema, dependency và cấu hình dịch vụ.
- 21.3 — Load model khi khởi động, endpoint predict, health và readiness.
- 21.4 — Authentication, authorization, rate limit, timeout và giới hạn payload.
- 21.5 — Sync, async, queue và công việc nền; phân biệt tác vụ IO với tác vụ CPU hoặc GPU.

Các ý trên giữ phạm vi phần 21 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Health khác readiness thế nào?
2. Authentication khác authorization ở đâu?
3. Vì sao không mở Spark trong mỗi request?

## Đọc thêm từ nguồn chính thức

- [FastAPI request body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
