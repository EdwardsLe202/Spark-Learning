# Ngày 23 — Lý thuyết: Model serving hiệu năng và độ tin cậy

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Hoàn thành dự án 2 bằng báo cáo tải, mục tiêu phục vụ và demo rollback.

## 1. Đo trải nghiệm từng yêu cầu và tổng năng lực
**Latency (độ trễ một yêu cầu)** khác **throughput (số yêu cầu xử lý mỗi đơn vị thời gian)**. **Concurrency (số yêu cầu đang được xử lý hoặc chờ đồng thời)** tăng có thể làm throughput tăng tới một mức rồi làm hàng đợi dài hơn. **p50/p95/p99 (các phân vị 50/95/99 của độ trễ)** phản ánh phần phân bố; trung bình đẹp có thể che các request rất chậm.

**Warm-up (khởi động nóng trước khi đo)** giúp tách tải model và khởi tạo khỏi trạng thái ổn định. Phải ghi cả lỗi và timeout; bỏ request lỗi khỏi báo cáo sẽ làm dịch vụ trông tốt giả. Với 20 request thì p99 hầu như chỉ phản ánh một mẫu cực trị, nên ghi cả lượng mẫu.

## 2. Các lựa chọn đều có chi phí
**Batching (gom nhiều yêu cầu thành một lô)** có thể tăng hiệu suất nhưng thêm thời gian chờ. **Worker (tiến trình phục vụ)** thường load một bản model riêng, nên nhiều worker tăng RAM. **Backpressure (cơ chế hạn chế tiếp nhận khi quá tải)** chặn hàng đợi tăng vô hạn. Retry chỉ dùng có giới hạn với lỗi tạm thời; retry hàng loạt có thể làm quá tải nặng hơn.

Cache (bộ nhớ đệm kết quả) cần khóa gồm version model và input đã chuẩn hóa. Thiếu version có thể trả prediction của model cũ. **Canary release (phát hành cho một phần nhỏ lưu lượng)** và **shadow traffic (chạy song song để quan sát mà chưa dùng kết quả)** giúp kiểm tra, nhưng đều cần theo dõi và khả năng rollback.

## 3. Chốt mục tiêu trước khi đo
**SLO — Service Level Objective (mục tiêu mức phục vụ)** trong lab có thể là tỷ lệ lỗi 0 và p95 dưới ngưỡng bạn chọn ở tải cụ thể. Đây là mục tiêu thử nghiệm trên máy của bạn. Ghi cấu hình phần cứng, model, số request, input, warm-up và cách đo để kết quả có ý nghĩa.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
import httpx
payload = {"events_30d": 2, "spend_30d": 300000, "recency_days": 12, "region": "HN", "plan": "basic"}
def send(_):
    start = perf_counter()
    try:
        response = httpx.post("http://127.0.0.1:8000/predict", json=payload, timeout=5)
        return {"seconds": perf_counter()-start, "status": response.status_code}
    except httpx.HTTPError as exc:
        return {"seconds": perf_counter()-start, "error": type(exc).__name__}
with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(send, range(20)))
print(results)
# TODO: warm up riêng, đo nhiều mẫu hơn, lưu mọi kết quả và tính phân vị.
```

## Năm ý đối chiếu với lộ trình gốc

- 23.1 — Latency, throughput, concurrency và p50, p95, p99.
- 23.2 — Model warm up, batching, worker, queue và giới hạn tài nguyên.
- 23.3 — Cache có khóa đúng, timeout, retry có giới hạn và backpressure.
- 23.4 — Version endpoint, canary hoặc shadow theo nhu cầu; rollback.
- 23.5 — Load test, kiểm tra độ tương đương và phân tích điểm nghẽn.

Các ý trên giữ phạm vi phần 23 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. p95 khác trung bình ở đâu?
2. Vì sao tăng concurrency có thể tăng latency?
3. Cache thiếu model version gây lỗi gì?

## Đọc thêm từ nguồn chính thức

- [FastAPI deployment](https://fastapi.tiangolo.com/deployment/)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
