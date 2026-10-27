# Ngày 110 — Xác thực phân quyền và kiểm thử API

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Xác thực phân quyền và kiểm thử API”. Kết quả cần đạt: Thiếu/sai key 401, key fixture đúng 200; có test giới hạn và quyền riêng.

## Từ mới gắn với bài này

- **Authentication (xác thực danh tính)**.
- **Authorization (kiểm tra quyền)**.
- **Rate limit (giới hạn tần suất)**.

## Tình huống và cách hiểu

**Authentication (xác thực danh tính)** trả lời ai gọi; **authorization (kiểm tra quyền)** trả lời người đó được làm gì. API key lab chỉ là bước xác thực đơn giản, chưa thay role/tenant policy của hệ thống thật.

**Rate limit (giới hạn tần suất)** và payload limit bảo vệ tài nguyên. Schema max length giới hạn từng trường nhưng không tự tạo giới hạn tổng body hay số request. Trong lab có thể dùng gateway hoặc middleware thử nghiệm, ghi rõ giới hạn nhiều worker.

Giữ key trong biến môi trường ngoài Git. Test thiếu/sai key phải bị chặn trước inference; user tự khai role trong JSON không được tự tăng quyền. Không log giá trị key hoặc toàn request chứa dữ liệu nhạy cảm.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-110/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from fastapi.testclient import TestClient
from services.churn_api import app
os.environ["COURSE_MODEL_PATH"] = str(ensure_demo_model())
os.environ["COURSE_API_KEY"] = "fixture-only-key"
body = {"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"}
with TestClient(app) as client:
    print("Thiếu key:", client.post("/predict", json=body).status_code)
    print("Sai key:", client.post("/predict", json=body, headers={"x-api-key": "wrong"}).status_code)
    print("Đúng key:", client.post("/predict", json=body, headers={"x-api-key": "fixture-only-key"}).status_code)
```

## Đọc từng phần của ví dụ

Ba request cùng dữ liệu, chỉ đổi credential. Không in credential thật của môi trường người học.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Thiếu/sai key 401, key fixture đúng 200; có test giới hạn và quyền riêng.

## Ba câu kiểm tra hiểu bài

1. Authentication có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: xác thực danh tính.
- Luồng chính: Ba request cùng dữ liệu, chỉ đổi credential. Không in credential thật của môi trường người học.
- Đối chiếu tiêu chí: Thiếu/sai key 401, key fixture đúng 200; có test giới hạn và quyền riêng. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 21 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
