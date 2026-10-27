"""Kiểm tra cấu trúc học, liên kết local, cú pháp và hợp đồng fixture.

Không cần Spark hay thư viện ngoài, không thực hiện TODO thay người học.
Chạy: python scripts/check_repo.py
"""
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter
from urllib.parse import unquote
import ast
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def load_csv(name):
    with (ROOT / "data/raw" / name).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main():
    for n in range(1, 31):
        base = ROOT / f"day-{n:02d}"
        for filename in ["README.md", "ly_thuyet.md", "thuc_hanh.md", "ghi_chu.md", "bai_lam.py"]:
            path = base / filename
            check(path.is_file() and path.stat().st_size > 0, f"Thiếu/rỗng: {path.relative_to(ROOT)}")
        theory = base / "ly_thuyet.md"
        if theory.exists():
            topics = re.findall(rf"^- {n:02d}\.[1-5] —", theory.read_text(encoding="utf-8"), re.M)
            check(len(topics) == 5, f"Ngày {n:02d} chưa đủ 5 ý gốc")

    markdown_files = [ROOT / "README.md", ROOT / "TIEN_DO.md"]
    for folder in ["docs", "data", "projects"] + [f"day-{n:02d}" for n in range(1, 31)]:
        markdown_files.extend((ROOT / folder).rglob("*.md"))
    checked_links = 0
    for path in markdown_files:
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0].strip("<>"))
            check((path.parent / target).exists(), f"Link hỏng trong {path.relative_to(ROOT)}: {target}")
            checked_links += 1
        for snippet in re.findall(r"```python\n(.*?)\n```", content, re.S):
            try:
                ast.parse(snippet)
            except SyntaxError as exc:
                errors.append(f"Code fence lỗi cú pháp: {path.relative_to(ROOT)}: {exc}")
    python_files = [ROOT / "spark_lab.py"] + list((ROOT / "scripts").glob("*.py"))
    python_files += [ROOT / f"day-{n:02d}/bai_lam.py" for n in range(1, 31)]
    for path in python_files:
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            errors.append(f"Python lỗi cú pháp: {path.relative_to(ROOT)}: {exc}")

    manifest = json.loads((ROOT / "data/raw/manifest.json").read_text())
    for name, digest in manifest["sha256"].items():
        check(hashlib.sha256((ROOT / "data/raw" / name).read_bytes()).hexdigest() == digest,
              f"Hash fixture thay đổi: {name}")
    customers = load_csv("customers.csv")
    events = load_csv("events.csv")
    check(len(customers) == manifest["customers"] == 120, "Số customer khác contract")
    check(len(events) == manifest["events"], "Số event khác manifest")
    customer_ids = {row["customer_id"] for row in customers}
    check(len(customer_ids) == len(customers), "Customer trùng khóa")
    check(len({row["event_id"] for row in events}) == len(events), "Events chuẩn trùng khóa")
    check(all(row["customer_id"] in customer_ids for row in events), "Events chuẩn có khóa lạ")
    check(all(int(row["amount"]) >= 0 for row in events), "Events chuẩn có số âm")
    check(len(load_csv("events_dirty.csv")) == 8, "Fixture dirty cần 8 dòng")
    tiny = load_csv("events_tiny.csv")
    check(sum(int(row["amount"]) for row in tiny) == 1250000, "Tổng tiny sai")
    # Đối chiếu bảng tính tay bằng datetime chuẩn, độc lập với Spark starter.
    cutoff = datetime.fromisoformat("2025-02-01T00:00:00+00:00")
    parse = lambda value: datetime.fromisoformat(value.replace("Z", "+00:00"))
    expected = {"C001": (2, 300000, 12, 0), "C002": (1, 50000, 17, 1), "C003": (0, 0, None, 1)}
    for cid, values in expected.items():
        history = [r for r in tiny if r["customer_id"] == cid
                   and cutoff-timedelta(days=30) <= parse(r["event_time"]) < cutoff
                   and parse(r["ingested_at"]) < cutoff]
        future = [r for r in tiny if r["customer_id"] == cid
                  and cutoff <= parse(r["event_time"]) < cutoff+timedelta(days=30)]
        recency = (cutoff.date()-max(parse(r["event_time"]).date() for r in history)).days if history else None
        actual = (len(history), sum(int(r["amount"]) for r in history), recency, int(not future))
        check(actual == values, f"Bảng feature tính tay sai cho {cid}: {actual}")
    for name, date in manifest["snapshots"].items():
        c = datetime.fromisoformat(date+"T00:00:00+00:00")
        check(parse(manifest["observed_until_exclusive"]) >= c+timedelta(days=30), f"{name} thiếu cửa sổ nhãn")
        positive = {r["customer_id"] for r in events if c <= parse(r["event_time"]) < c+timedelta(days=30)}
        check(0 < len(positive) < len(customers), f"{name} cần có cả hai lớp để học phân loại")

    corpus = [json.loads(line) for line in (ROOT / "data/rag/corpus.jsonl").read_text(encoding="utf-8").splitlines()]
    queries = [json.loads(line) for line in (ROOT / "data/rag/queries.jsonl").read_text(encoding="utf-8").splitlines()]
    docs = {d["doc_id"]: d for d in corpus}
    check(len(corpus) == len(docs) == 8, "Corpus cần 8 doc duy nhất")
    check(len(queries) == len({q["query_id"] for q in queries}) == 40, "Eval cần 40 query duy nhất")
    check(Counter(q["category"] for q in queries) == {"answerable": 20, "unanswerable": 8, "ambiguous": 6, "forbidden": 6}, "Sai số lượng nhóm eval")
    check(Counter(q["split"] for q in queries) == {"dev": 16, "test": 24}, "Sai split eval")
    for q in queries:
        check(set(q["relevant_doc_ids"]) <= set(docs), f"Nhãn trỏ doc không tồn tại: {q['query_id']}")
        check(all(docs[d]["access"] == "public" for d in q["relevant_doc_ids"]), f"Nhãn public chứa doc nội bộ: {q['query_id']}")
        check(bool(q["relevant_doc_ids"]) == (q["category"] == "answerable"), f"Nhãn relevant sai nhóm: {q['query_id']}")
    if errors:
        for error in errors:
            print("ERROR:", error)
        raise SystemExit(1)
    print(f"OK: 30 ngày, 150 ý gốc, {len(markdown_files)} Markdown, {checked_links} link local, {len(python_files)} Python.")
    print("OK: hash/count/key fixture, feature tính tay, cửa sổ nhãn, corpus và 40 eval.")
    print("Đây là kiểm tra bộ học; không chứng nhận các TODO của người học đã hoàn thành.")


if __name__ == "__main__":
    main()
