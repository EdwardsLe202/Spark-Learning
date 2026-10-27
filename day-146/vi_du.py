"""Ngày 146: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 146 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(146, exercise=False)
    decision = {"observed_error_id": None, "root_cause": None, "options": ["fix_data_or_retrieval", "change_prompt", "fine_tune"], "chosen": None, "evidence": [], "budget_minutes": 30, "paid_budget": 0}
    write_json(out / "decision_template.json", decision)
    print("Điền bằng lỗi thật từ dự án RAG, không chọn fine-tune mặc định.")


if __name__ == "__main__":
    main()
