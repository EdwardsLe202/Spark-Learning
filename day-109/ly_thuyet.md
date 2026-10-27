# Ngày 109 — Lifespan load model health và readiness

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Lifespan load model health và readiness”. Kết quả cần đạt: Có score model thật và version; không train trong endpoint; missing artifact không được giả vờ ready.

## Từ mới gắn với bài này

- **Lifespan (vòng đời ứng dụng)**.
- **Health (tiến trình còn sống)**.
- **Readiness (sẵn sàng phục vụ)**.

## Tình huống và cách hiểu

**Lifespan (vòng đời ứng dụng)** là chỗ load model một lần mỗi process. **Health (tiến trình còn sống)** khác **readiness (sẵn sàng phục vụ)**: API có thể đang chạy nhưng thiếu artifact nên predict chưa dùng được.

Dịch vụ tham chiếu chỉ load model; không fit trong request hoặc lúc mở API. Ví dụ chuẩn bị model demo trước khi tạo TestClient. Metadata phải cùng contract, model_version và threshold.

Một worker thường giữ một bản model, nên tăng worker có thể tăng RAM. Mẫu local nhỏ không thay thế kiểm chứng runtime model lớn. Nếu artifact mất hoặc metadata không hợp lệ, hệ thống phải báo rõ và không trả score giả.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-109/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from fastapi.testclient import TestClient
from services.churn_api import app
path = ensure_demo_model()
os.environ["COURSE_MODEL_PATH"] = str(path)
os.environ["COURSE_API_KEY"] = "fixture-only-key"
with TestClient(app) as client:
    print("Health:", client.get("/health").status_code)
    print("Ready:", client.get("/ready").json())
    body = {"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"}
    print(client.post("/predict", json=body, headers={"x-api-key": "fixture-only-key"}).json())
```

## Đọc từng phần của ví dụ

Fixture key chỉ dành test giả lập trong process. Ensure_demo_model train trước API; lifespan không gọi fit.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có score model thật và version; không train trong endpoint; missing artifact không được giả vờ ready.

## Ba câu kiểm tra hiểu bài

1. Lifespan có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: vòng đời ứng dụng.
- Luồng chính: Fixture key chỉ dành test giả lập trong process. Ensure_demo_model train trước API; lifespan không gọi fit.
- Đối chiếu tiêu chí: Có score model thật và version; không train trong endpoint; missing artifact không được giả vờ ready. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 21 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
