# Ngày 108 — FastAPI route và mã lỗi

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “FastAPI route và mã lỗi”. Kết quả cần đạt: Input hợp lệ 200, lỗi cấu trúc 422; không trả stack trace nội bộ cho client.

## Từ mới gắn với bài này

- **Endpoint (đường dẫn chức năng)**.
- **FastAPI (framework API Python)**.
- **HTTPException (phản hồi lỗi có trạng thái)**.

## Tình huống và cách hiểu

**Endpoint (đường dẫn chức năng)** nhận một kiểu request xác định. **FastAPI (framework API Python)** dùng model Pydantic để parse và sinh tài liệu. **HTTPException (phản hồi lỗi có trạng thái)** giúp phân biệt lỗi dự kiến với stack trace nội bộ.

Bài bắt đầu một endpoint chỉ kiểm tra đầu vào để bạn hiểu transport. Phục vụ model thật được ghép ở ngày sau. TestClient chạy ứng dụng trong tiến trình test, chưa đo đường truyền HTTP hoặc nhiều máy.

Một response 200 có score cố định không chứng minh inference hoạt động. Mẫu hôm nay cố ý trả dữ liệu kiểm tra cùng trạng thái validated, không gọi đó là prediction model.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-108/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient
from services.churn_api import PredictionInput
app = FastAPI()
@app.post("/validate")
def validate(body: PredictionInput):
    return {"status": "validated", "features": body.model_dump()}
with TestClient(app) as client:
    ok = client.post("/validate", json={"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"})
    bad = client.post("/validate", json={"events_30d": -1})
    print(ok.status_code, bad.status_code)
```

## Đọc từng phần của ví dụ

Endpoint dùng schema thật nhưng chưa model. TestClient chứng minh routing/validation, không là load test mạng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Input hợp lệ 200, lỗi cấu trúc 422; không trả stack trace nội bộ cho client.

## Ba câu kiểm tra hiểu bài

1. Endpoint có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đường dẫn chức năng.
- Luồng chính: Endpoint dùng schema thật nhưng chưa model. TestClient chứng minh routing/validation, không là load test mạng.
- Đối chiếu tiêu chí: Input hợp lệ 200, lỗi cấu trúc 422; không trả stack trace nội bộ cho client. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 21 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
