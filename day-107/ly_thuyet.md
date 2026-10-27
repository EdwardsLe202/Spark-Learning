# Ngày 107 — Pydantic kiểm tra kiểu miền giá trị và trường thừa

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Pydantic kiểm tra kiểu miền giá trị và trường thừa”. Kết quả cần đạt: Input chuẩn hợp lệ; ba mẫu sai bị ValidationError; không biến lỗi thành score giả.

## Từ mới gắn với bài này

- **Pydantic (thư viện kiểm tra dữ liệu)**.
- **Validation (kiểm tra cấu trúc và quy tắc)**.
- **Finite number (số hữu hạn)**.

## Tình huống và cách hiểu

**Pydantic (thư viện kiểm tra dữ liệu)** chuyển JSON/Python object thành dữ liệu theo schema. **Validation (kiểm tra cấu trúc và quy tắc)** cần cả kiểu, giới hạn và trường thừa. API phải chặn số âm, NaN/Infinity và chuỗi quá dài theo contract.

**Finite number (số hữu hạn)** quan trọng vì model thường không chấp nhận vô cực dù đó là một float trong Python. Quy tắc coercion của Pydantic cần được chọn chủ đích; không giả định mọi chuỗi số sẽ bị chặn khi bạn chưa bật strict.

PredictionInput của dịch vụ dùng ge, max length, extra=forbid, allow_inf_nan=false. Lab thử cả giá trị hợp lệ và không hợp lệ, không chỉ một request đẹp.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-107/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from pydantic import ValidationError
from services.churn_api import PredictionInput
body = {"events_30d": 2, "spend_30d": 300000, "region": "HN", "plan": "basic"}
print(PredictionInput(**body).model_dump())
for bad in [{**body, "events_30d": -1}, {**body, "extra": 1}, {**body, "spend_30d": float("inf")}]:
    try:
        PredictionInput(**bad)
    except ValidationError as error:
        print("Bị chặn:", error.error_count())
```

## Đọc từng phần của ví dụ

Recency có thể None theo policy đã học. Ba biến thể thử ba loại vi phạm riêng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Input chuẩn hợp lệ; ba mẫu sai bị ValidationError; không biến lỗi thành score giả.

## Ba câu kiểm tra hiểu bài

1. Pydantic có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: thư viện kiểm tra dữ liệu.
- Luồng chính: Recency có thể None theo policy đã học. Ba biến thể thử ba loại vi phạm riêng.
- Đối chiếu tiêu chí: Input chuẩn hợp lệ; ba mẫu sai bị ValidationError; không biến lỗi thành score giả. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 21 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
