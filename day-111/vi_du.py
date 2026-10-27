"""Ngày 111: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 111 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(111, exercise=False)
    import asyncio
    from time import perf_counter
    async def fake_io(name):
        await asyncio.sleep(0.02)
        return name
    async def run():
        return await asyncio.gather(fake_io("a"), fake_io("b"))
    start = perf_counter()
    print(asyncio.run(run()), "seconds:", perf_counter() - start)
    print("Đây là chờ I/O giả lập, chưa benchmark tính toán CPU.")


if __name__ == "__main__":
    main()
