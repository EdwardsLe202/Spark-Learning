"""Tạo lại dữ liệu của lộ trình tổng hợp cũ trong data/raw.
Khóa nền Spark mới dùng data/beginner; không cần chạy script này.
"""
from pathlib import Path
from datetime import datetime, timedelta, timezone
import csv
import hashlib
import json
import random

ROOT = Path(__file__).resolve().parents[1]


def generate():
    dest = ROOT / "data" / "raw"
    dest.mkdir(parents=True, exist_ok=True)
    rng = random.Random(42)
    customers = []
    for n in range(1, 121):
        customers.append([f"C{n:03d}", ["HN", "HCM", "DN"][n % 3],
                          "pro" if n % 3 == 0 else "basic", "2024-12-01"])
    with (dest / "customers.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["customer_id", "region", "plan", "signup_date"])
        w.writerows(customers)
    rows = []
    start = datetime(2025, 1, 1, tzinfo=timezone.utc)
    for d in range(212):  # Có dữ liệu tới hết tháng 7 để tạo nhãn tháng 6.
        day = start + timedelta(days=d)
        for n in range(1, 121):
            # Cơ chế giả lập cho bài học, không phải hành vi churn thực tế.
            inactive = (n + day.month) % 5 == 0
            probability = 0.035 if inactive else (0.12 + (n % 7) * 0.065)
            if rng.random() >= probability:
                continue
            ts = day + timedelta(hours=8 + n % 10)
            amount = rng.randrange(1, 21) * 10000
            eid = f"E{len(rows) + 1:06d}"
            fmt = lambda t: t.strftime("%Y-%m-%dT%H:%M:%SZ")
            rows.append([eid, f"C{n:03d}", fmt(ts), fmt(ts + timedelta(hours=1)), amount, "purchase"])
    header = ["event_id", "customer_id", "event_time", "ingested_at", "amount", "event_type"]
    with (dest / "events.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)
    dirty = [
        ["D001", "C001", "2025-01-01T10:00:00Z", "2025-01-01T11:00:00Z", "100000", "purchase"],
        ["D002", "C002", "2025-01-02T10:00:00Z", "2025-01-02T11:00:00Z", "50000", "purchase"],
        ["D002", "C002", "2025-01-02T10:00:00Z", "2025-01-03T11:00:00Z", "70000", "purchase"],
        ["D003", "", "2025-01-02T10:00:00Z", "2025-01-02T11:00:00Z", "10000", "purchase"],
        ["D004", "C003", "not-a-date", "2025-01-02T11:00:00Z", "10000", "purchase"],
        ["D005", "C003", "2025-01-03T10:00:00Z", "2025-01-03T11:00:00Z", "-10000", "purchase"],
        ["D006", "C999", "2025-01-03T10:00:00Z", "2025-01-03T11:00:00Z", "20000", "purchase"],
        ["D007", "C004", "2025-01-03T10:00:00Z", "2025-01-03T11:00:00Z", "abc", "purchase"],
    ]
    with (dest / "events_dirty.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(dirty)
    tiny = [
        ["T001", "C001", "2025-01-02T10:00:00Z", "2025-01-02T11:00:00Z", "100000", "purchase"],
        ["T002", "C001", "2025-01-20T10:00:00Z", "2025-01-20T11:00:00Z", "200000", "purchase"],
        ["T003", "C002", "2025-01-15T10:00:00Z", "2025-01-15T11:00:00Z", "50000", "purchase"],
        ["T004", "C001", "2025-02-05T10:00:00Z", "2025-02-05T11:00:00Z", "900000", "purchase"],
    ]
    with (dest / "events_tiny.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(tiny)
    manifest = {
        "synthetic": True, "seed": 42, "customers": len(customers), "events": len(rows),
        "observed_until_exclusive": "2025-08-01T00:00:00Z",
        "snapshots": {"train": "2025-02-01", "validation": "2025-04-01", "test": "2025-06-01"},
        "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dest.glob("*.csv"))},
    }
    (dest / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Đã tạo {len(customers)} khách hàng, {len(rows)} sự kiện; fixture tiny và dirty.")


if __name__ == "__main__":
    generate()
