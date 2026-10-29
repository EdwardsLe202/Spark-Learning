"""Ngày 03: kiểm tra môi trường thực tế, không ghi cứng phiên bản máy.
Cài theo docs/CAI_DAT.md, rồi chạy: uv run python scripts/run_day.py 03
Ở terminal mới: đứng ở gốc repo, rồi chạy lại lệnh uv run trên.
"""
import os
import re
import subprocess
import sys

import pyspark

print("Python:", sys.version.split()[0], flush=True)
print("Python đang chạy:", sys.executable, flush=True)
print("PySpark:", pyspark.__version__, flush=True)
print("JAVA_HOME:", os.environ.get("JAVA_HOME", "chưa đặt; dùng java trên PATH"), flush=True)

# java -version thường ghi phiên bản vào stderr, nên lấy cả hai luồng.
java = subprocess.run(["java", "-version"], capture_output=True, text=True, check=True)
java_version_text = java.stdout + java.stderr
print(java_version_text.strip(), flush=True)

if sys.version_info[:2] != (3, 11):
    raise SystemExit("Cần Python 3.11. Xem docs/CAI_DAT.md và chạy bằng uv run.")
if sys.prefix == sys.base_prefix:
    raise SystemExit("Python chưa thuộc môi trường riêng. Chạy bằng uv run ở gốc repo.")
if pyspark.__version__ != "3.5.7":
    raise SystemExit("Cần PySpark 3.5.7. Chạy uv sync rồi chạy lại bằng uv run.")
if not re.search(r'version\s+"17[."]', java_version_text):
    raise SystemExit("Cần Java 17. Chọn lại Java theo docs/CAI_DAT.md.")

print("Đạt yêu cầu: Python 3.11, PySpark 3.5.7, Java 17 và Python trong môi trường riêng.")
print("Nếu lỗi ở terminal khác, kiểm tra lại interpreter và JAVA_HOME trước khi cài lại.")
