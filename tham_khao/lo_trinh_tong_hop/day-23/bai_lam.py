"""Ngày 23: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 23
"""
from spark_lab import ROOT, DATA, output_dir

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

# Bài tự làm hôm nay:
# TODO Mở API ngày 21 ở terminal riêng. Chọn SLO lab, warm up 10 request rồi gửi ít nhất 100 request cho mỗi concurrency 1, 2, 4.
# TODO Lưu latency/status của mọi request; tính p50, p95, lỗi và throughput = tổng request / tổng wall time. Nêu cách xử lý timeout trong báo cáo.
# TODO Chỉ đổi một yếu tố như số worker; chạy lại cùng input, kiểm tra prediction không đổi và ghi RAM quan sát được.
# TODO Thực hiện rollback model theo manifest ngày 19, kiểm tra readiness và version trong response.
# TODO Hoàn thành `projects/02-mlops/README.md`: test, MLflow, batch, API, monitoring, load test và phạm vi Docker/Airflow/cloud đã thực sự làm.
