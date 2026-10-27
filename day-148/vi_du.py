"""Ngày 148: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 148 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(148, exercise=False)
    plan = {"base_model": "Qwen/Qwen2.5-0.5B-Instruct", "method": "LoRA", "target_modules": ["q_proj", "v_proj"], "rank": 4, "steps_for_smoke": 2, "evaluation": "locked_test_after_validation_selection", "quantization": "not_required_on_mac"}
    write_json(out / "lora_plan.json", plan)
    print("Tùy chọn thực thi: python services/finetune_lora.py --steps 2")


if __name__ == "__main__":
    main()
