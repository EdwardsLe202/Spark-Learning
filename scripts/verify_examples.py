"""Kiểm tra ví dụ theo ngày; không cài thư viện hoặc tải model tự động.

python scripts/verify_examples.py --include-delta
python scripts/verify_examples.py --days 109 110
"""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, nargs="+")
    parser.add_argument("--include-delta", action="store_true")
    parser.add_argument("--include-models", action="store_true", help="Cache model thật phải được chuẩn bị trước")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    plan = json.loads((ROOT / "scripts/course_plan.json").read_text(encoding="utf-8"))
    selected = set(args.days or [r["day"] for r in plan])
    if not selected <= {r["day"] for r in plan} or args.timeout < 1:
        parser.error("Ngày hoặc timeout không hợp lệ")
    out = ROOT / "artifacts/full/verification" / ("run-" + uuid.uuid4().hex[:10])
    out.mkdir(parents=True)
    environment = os.environ.copy()
    environment["PYSPARK_PYTHON"] = sys.executable
    environment.setdefault("SPARK_LOCAL_IP", "127.0.0.1")
    records = []
    for row in plan:
        day = row["day"]
        if day not in selected:
            continue
        mode = row.get("environment", "beginner")
        conditional = mode == "delta" and not args.include_delta
        conditional |= mode in {"embedding", "generator", "reranker", "rag_models"} and not args.include_models
        if conditional:
            record = {"day": day, "status": "conditional", "environment": mode}
        else:
            try:
                result = subprocess.run([sys.executable, str(ROOT / "scripts/run_day.py"), str(day), "--example"],
                    cwd=ROOT, env=environment, capture_output=True, text=True, timeout=args.timeout)
                (out / f"day-{day:03d}.log").write_text(result.stdout + "\n" + result.stderr, encoding="utf-8")
                record = {"day": day, "status": "passed" if result.returncode == 0 else "failed", "exit_code": result.returncode}
            except subprocess.TimeoutExpired:
                record = {"day": day, "status": "failed", "error": "timeout"}
        records.append(record)
        (out / "results.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(record, flush=True)
    print({s: sum(r["status"] == s for r in records) for s in ["passed", "failed", "conditional"]})
    print("Log:", out)
    raise SystemExit(any(r["status"] == "failed" for r in records))


if __name__ == "__main__":
    main()
