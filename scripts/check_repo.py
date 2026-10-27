"""Kiểm tra khóa nền Spark và bảo toàn bài cũ, không cần cài PySpark.

Chạy từ repo: python scripts/check_repo.py
Kiểm tra này không chấm bài làm của người học hoặc mức hiểu bài.
"""
from pathlib import Path
from collections import Counter
from datetime import date
from urllib.parse import unquote
import ast
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def read_csv(name):
    with (ROOT / "data/beginner" / name).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def main():
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    plan = json.loads((ROOT / "scripts/course_plan.json").read_text(encoding="utf-8"))
    check([day["day"] for day in plan] == list(range(1, 151)), "Lịch phải đủ 150 ngày theo thứ tự")
    expected_days = {f"day-{n:02d}" for n in range(1, 151)}
    check({p.name for p in ROOT.glob("day-*") if p.is_dir()} == expected_days, "Thư mục ngày học không khớp kế hoạch")
    coverage = json.loads((ROOT / "scripts/source_coverage.json").read_text(encoding="utf-8"))
    expected_source = {f"{part:02d}.{lesson}" for part in range(1, 31) for lesson in range(1, 6)}
    check({row["source_id"] for row in coverage} == expected_source and len(coverage) == 150, "Chưa ánh xạ đủ 150 ý gốc")
    for row in coverage:
        check(bool(row["days"]) and all(day in range(1, 151) for day in row["days"]), "Ý gốc trỏ ngày không hợp lệ: " + row["source_id"])
    for day in plan:
        n = day["day"]
        check(day["prerequisite"] == (None if n == 1 else n - 1), f"Điều kiện đầu vào vòng lặp hoặc thiếu ở ngày {n}")
        base = ROOT / f"day-{n:02d}"
        for filename in ["README.md", "ly_thuyet.md", "thuc_hanh.md", "vi_du.py", "bai_lam.py", "ghi_chu.md"]:
            path = base / filename
            check(path.is_file() and path.stat().st_size > 0, f"Thiếu/rỗng: {path.relative_to(ROOT)}")
        theory = (base / "ly_thuyet.md").read_text(encoding="utf-8")
        lab = (base / "thuc_hanh.md").read_text(encoding="utf-8")
        for marker in ["Mục tiêu nhỏ", "Đọc từng phần", "Kết quả để đối chiếu", "Từ mới", "Ba câu"]:
            check(marker in theory, f"Ngày {n}: thiếu phần giảng {marker}")
        for marker in ["Bước 1", "Bước 2", "Bước 3", "Bước 4", "Gợi ý", "Đối chiếu sau khi đã tự thử", "--example"]:
            check(marker in lab, f"Ngày {n}: thiếu bước hỗ trợ {marker}")
        if n <= 2:
            check("import pyspark" not in (base / "vi_du.py").read_text(), f"Ngày {n} không được cần cài Spark")
        check("Đã xong ngày 02" not in (base / "README.md").read_text(), f"Điều kiện cài đặt bị vòng lặp ngày {n}")

    markdown = [ROOT / name for name in ["README.md", "BAT_DAU.md", "TIEN_DO.md", "LO_TRINH_DAY_DU.md"]]
    for folder in ["docs", "data", "projects", "tham_khao"] + [f"day-{n:02d}" for n in range(1, 151)]:
        markdown.extend((ROOT / folder).rglob("*.md"))
    checked_links = 0
    for path in markdown:
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0].strip("<>"))
            check((path.parent / target).exists(), f"Link hỏng {path.relative_to(ROOT)}: {target}")
            checked_links += 1
        if "lo_trinh_tong_hop" not in path.parts:
            for code in re.findall(r"```python\n(.*?)\n```", content, re.S):
                try:
                    ast.parse(code)
                except SyntaxError as exc:
                    errors.append(f"Ví dụ Markdown sai cú pháp: {path.relative_to(ROOT)}: {exc}")

    python_files = (list((ROOT / "scripts").glob("*.py")) + list(ROOT.glob("day-*/*.py"))
                    + list((ROOT / "services").rglob("*.py")) + list((ROOT / "tests").glob("*.py")))
    python_files += [ROOT / "course_support.py", ROOT / "rag_support.py"]
    for path in python_files:
        try:
            ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError as exc:
            errors.append(f"Python sai cú pháp: {path.relative_to(ROOT)}: {exc}")

    manifest = json.loads((ROOT / "data/beginner/manifest.json").read_text())
    for name, digest in manifest["sha256"].items():
        path = ROOT / "data/beginner" / name
        check(hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"Nguồn beginner đổi: {name}")
        check(len(read_csv(name)) == manifest["rows"][name], f"Số dòng nguồn đổi: {name}")
    orders = read_csv("orders.csv")
    customers = read_csv("customers.csv")
    check(len(orders) == 8 and len(customers) == 5, "Nguồn cần 8 đơn / 5 khách")
    check(len({r["order_id"] for r in orders}) == 8, "Mã đơn chuẩn không duy nhất")
    check(len({r["customer_id"] for r in customers}) == 5, "Mã khách chuẩn không duy nhất")
    check(sum(int(r["amount"]) for r in orders) == 1400000, "Tổng nguồn sai")
    completed = [r for r in orders if r["status"] == "completed"]
    check(len(completed) == 7 and sum(int(r["amount"]) for r in completed) == 1100000, "Báo cáo completed sai")
    selected = [r for r in completed if int(r["amount"]) >= 150000]
    check(len(selected) == 3 and sum(int(r["amount"]) for r in selected) == 750000, "Kết quả biên ngưỡng sai")
    totals = {r["customer_id"]: 0 for r in customers}
    for row in completed:
        totals[row["customer_id"]] += int(row["amount"])
    check(totals == {"C001":700000,"C002":200000,"C003":120000,"C004":80000,"C005":0}, "Tổng khách tính tay sai")
    regions = Counter()
    for row in customers:
        regions[row["region"]] += totals[row["customer_id"]]
    check(dict(regions) == {"HN":780000,"HCM":200000,"DN":120000}, "Tổng vùng sai")

    dirty = read_csv("orders_dirty.csv")
    valid = []
    for row in dirty:
        try:
            amount = int(row["amount"])
            date.fromisoformat(row["order_date"])
            if not row["customer_id"] or amount < 0:
                continue
        except (ValueError, TypeError):
            continue
        valid.append(row)
    unique = {tuple(sorted(row.items())): row for row in valid}
    clean = [r for r in unique.values() if r["customer_id"] in totals]
    check([len(dirty), len(valid), len(unique), len(clean)] == [10,5,4,3], "Đối soát nguồn dirty sai")
    check(sum(int(r["amount"]) for r in clean) == 390000, "Tổng clean dirty sai")

    archive = ROOT / "tham_khao/lo_trinh_tong_hop"
    backup = json.loads((archive / "BAN_LUU.json").read_text())
    for name, digest in backup["sha256"].items():
        path = archive / name
        check(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
              f"Bản lưu không còn nguyên vẹn: {name}")
    check("day-01/bai_lam.py" in backup["sha256"] and "day-01/ghi_chu.md" in backup["sha256"], "Thiếu bài làm/ghi chú ngày 01 trong bản lưu")

    if errors:
        print("\n".join("ERROR: " + error for error in errors))
        raise SystemExit(1)
    print(f"OK: {len(plan)} ngày, 150 ý gốc, điều kiện đầu vào xuôi, ví dụ và khung bài làm; {len(python_files)} Python hợp lệ.")
    print(f"OK: {len(markdown)} Markdown, {checked_links} link local; dữ liệu tính tay, biên lọc và đối soát nguồn lỗi.")
    print(f"OK: bảo toàn {len(backup['sha256'])} tệp cũ, gồm bài làm/ghi chú ngày 01.")
    print("Không chấm tự động mức hiểu bài hay các phần người học chưa thực hiện.")


if __name__ == "__main__":
    main()
