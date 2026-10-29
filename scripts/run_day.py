"""Chạy bài tự làm; thêm --example để chạy ví dụ hoàn chỉnh."""
from pathlib import Path
import argparse
import json
import os
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
plan = json.loads((ROOT / "scripts/course_plan.json").read_text(encoding="utf-8"))
days = {item["day"]: item for item in plan}
parser = argparse.ArgumentParser(description="Lộ trình Spark/MLOps/AI: chạy bài làm hoặc ví dụ theo ngày.")
parser.add_argument("day", type=int, help=f"Ngày 1–{max(days)}")
parser.add_argument("--example", action="store_true", help="Chạy vi_du.py thay cho bai_lam.py")
args = parser.parse_args()
if args.day not in days:
    parser.error(f"Chọn một ngày từ 1 đến {max(days)}")
if args.day >= 3 and sys.version_info[:2] != (3, 11):
    parser.exit(1, "Từ ngày 03, dùng Python 3.11. Chạy uv run python scripts/run_day.py <ngày>; xem docs/CAI_DAT.md.\n")
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
filename = "vi_du.py" if args.example else "bai_lam.py"
try:
    runpy.run_path(str(ROOT / f"day-{args.day:02d}" / filename), run_name="__main__")
except ModuleNotFoundError as exc:
    if exc.name == "pyspark":
        parser.exit(1, "Chưa có PySpark trong Python này. Chạy uv sync rồi uv run python scripts/run_day.py <ngày>; xem docs/CAI_DAT.md.\n")
    if args.day > 30 and exc.name in {"pandas", "numpy", "sklearn", "mlflow", "torch", "qdrant_client", "sentence_transformers", "transformers", "delta", "pytest"}:
        parser.exit(1, f"Thiếu thư viện {exc.name}. Xem Điều kiện chạy trong day-{args.day:02d}/README.md và docs/CAI_DAT_NANG_CAO.md.\n")
    raise
