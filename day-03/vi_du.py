"""Ngày 03: ví dụ hoàn chỉnh để đọc và chạy.
Chạy từ gốc repo: uv run python scripts/run_day.py 03 --example
"""
import subprocess
import sys
import pyspark
print("Python:", sys.version.split()[0])
print("Python đang chạy:", sys.executable)
print("PySpark:", pyspark.__version__)
subprocess.run(["java", "-version"], check=True)
