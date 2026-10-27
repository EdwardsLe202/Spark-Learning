"""Chạy từ thư mục gốc: python scripts/run_day.py 04."""
from pathlib import Path
import argparse
import os
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description="Chạy file bài làm của một ngày.")
parser.add_argument("day", type=int, choices=range(1, 31))
args = parser.parse_args()
sys.path.insert(0, str(ROOT))
os.chdir(ROOT)
runpy.run_path(str(ROOT / f"day-{args.day:02d}" / "bai_lam.py"), run_name="__main__")

