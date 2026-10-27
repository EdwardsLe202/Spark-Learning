"""Ngày 43: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 43 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(43, exercise=False)
    import sqlite3
    with sqlite3.connect(out / "source.db") as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS orders (order_id TEXT PRIMARY KEY, amount INTEGER)")
        connection.execute("INSERT OR REPLACE INTO orders VALUES (?, ?)", ("O001", 100000))
        print(connection.execute("SELECT order_id, amount FROM orders").fetchall())
    print("Đây là fixture database local; lab JDBC dùng connector riêng.")


if __name__ == "__main__":
    main()
