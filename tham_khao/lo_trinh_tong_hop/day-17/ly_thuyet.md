# Ngày 17 — Lý thuyết: Lập lịch và điều phối pipeline

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Xây workflow có dependency, retry giới hạn và backfill theo ngày dữ liệu.

## 1. Điều phối là quyết định bước nào chạy khi nào
**Orchestration (điều phối công việc)** gọi các bước theo phụ thuộc. **DAG — Directed Acyclic Graph (đồ thị có hướng không chu trình)** biểu diễn validate → features → train → evaluate → score. **Task dependency (quan hệ phụ thuộc giữa tác vụ)** giúp score chỉ chạy sau khi model và dữ liệu đạt điều kiện.

**Schedule (lịch chạy)** khác data interval. Task chạy ngày 10 có thể xử lý giao dịch ngày 9. Không dùng datetime.now() ở giữa logic để quyết định dữ liệu cần đọc; nhận ngày hoặc khoảng dữ liệu tường minh. Metadata nhỏ như đường dẫn, hash, số dòng có thể truyền giữa task; bảng lớn nên được lưu ở nơi dùng chung.

## 2. Retry phải đi cùng idempotency
**Retry (thử lại)** hợp lý cho lỗi tạm thời như kết nối; không tự sửa lỗi schema hoặc nhãn sai. **Timeout (giới hạn thời gian)** chặn tác vụ treo. Backfill chạy cho ngày cũ phải giữ đúng khóa và đích ngày đó. Một task ghi append rồi thất bại có thể nhân dữ liệu nếu retry; hãy dùng chiến lược ngày 10.

**Quality gate (điều kiện chất lượng để đi tiếp)** dừng luồng khi dữ liệu lỗi hoặc candidate không đạt. Nếu task thất bại, các bước phụ thuộc không được giả vờ hoàn thành. Tránh chạy nhiều ngày ghi cùng một đích mà không có chính sách cạnh tranh và cô lập.

## 3. Học cơ chế trước khi thêm dịch vụ
Bài cốt lõi dùng workflow Python local có dependency, log, retry và ngày tường minh. Nó giúp kiểm tra logic điều phối trong 30 ngày nhưng chưa thay thế scheduler vận hành. Nhánh Airflow là phần thực hành đầy đủ hơn: chuyển cùng task sang DAG, chọn phiên bản tài liệu đúng môi trường riêng, thử scheduler và lịch sử chạy. Không cài Airflow chung môi trường ML chỉ để có hình giao diện.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
from datetime import date
steps = ["validate", "features", "train", "evaluate", "score"]
snapshot = date.fromisoformat("2025-02-01")
for step in steps:
    print({"step": step, "snapshot_date": snapshot.isoformat(), "status": "planned"})
# TODO: thay bản kế hoạch bằng các lời gọi CLI ngày 16, kiểm tra returncode từng bước.
```

## Năm ý đối chiếu với lộ trình gốc

- 17.1 — DAG, task, dependency, data interval và lịch chạy trong Airflow.
- 17.2 — Tách ingest, validate, features, train, evaluate, register và score.
- 17.3 — Retry, timeout, backfill, idempotency và checkpoint theo bước.
- 17.4 — Điều kiện dừng khi dữ liệu lỗi hoặc model không đạt; truyền metadata thay vì dữ liệu lớn.
- 17.5 — Theo dõi trạng thái, thông báo lỗi, hạn chế tài nguyên và tránh chạy chồng ngoài ý muốn.

Các ý trên giữ phạm vi phần 17 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Task hôm nay có thể xử lý ngày nào?
2. Lỗi schema có nên retry như lỗi mạng?
3. Scheduler có tự bảo đảm idempotency không?

## Đọc thêm từ nguồn chính thức

- [Airflow 3.0 core concepts](https://airflow.apache.org/docs/apache-airflow/3.0.0/core-concepts/index.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
