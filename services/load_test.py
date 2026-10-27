"""Gửi tải có giới hạn vào API lab. Không in giá trị credential."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from time import perf_counter
import argparse
import os
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import FULL, write_json


def main():
    import httpx
    import numpy as np
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8000/predict")
    parser.add_argument("--requests", type=int, default=100)
    parser.add_argument("--concurrency", type=int, default=1)
    args = parser.parse_args()
    if not 1 <= args.requests <= 10000 or not 1 <= args.concurrency <= 32:
        parser.error("Giới hạn lab: 1..10000 request, concurrency 1..32")
    key = os.environ.get("COURSE_API_KEY")
    if not key:
        parser.error("Đặt COURSE_API_KEY trong terminal, không đưa key vào command history")
    body = {"events_30d": 2, "spend_30d": 300000, "recency_days": 12, "region": "HN", "plan": "basic"}

    def send(_):
        start = perf_counter()
        try:
            response = httpx.post(args.url, json=body, headers={"x-api-key": key}, timeout=5)
            record = {"seconds": perf_counter() - start, "status": response.status_code}
            if response.status_code == 200:
                payload = response.json()
                record.update({"score": payload.get("score"), "model_version": payload.get("model_version")})
            return record
        except (httpx.HTTPError, ValueError) as error:
            return {"seconds": perf_counter() - start, "error": type(error).__name__}

    warmup = [send(i) for i in range(10)]
    if not any(r.get("status") == 200 for r in warmup):
        raise SystemExit("Warm-up không có request thành công; kiểm tra API/key/model trước khi benchmark")
    start = perf_counter()
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        rows = list(pool.map(send, range(args.requests)))
    wall = perf_counter() - start
    elapsed = [r["seconds"] * 1000 for r in rows]
    summary = {"requests": len(rows), "concurrency": args.concurrency, "wall_seconds": wall,
               "throughput_all_requests_per_second": len(rows) / wall,
               "error_rate": sum(r.get("status") != 200 for r in rows) / len(rows),
               "p50_all_ms": float(np.percentile(elapsed, 50)), "p95_all_ms": float(np.percentile(elapsed, 95)),
               "percentile_method": "numpy default linear", "warmup_excluded": len(warmup)}
    out = FULL / "load-tests" / uuid.uuid4().hex[:10]
    write_json(out / "requests.json", rows)
    write_json(out / "summary.json", summary)
    print(summary)
    print("Bằng chứng:", out)


if __name__ == "__main__":
    main()
