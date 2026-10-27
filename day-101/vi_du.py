"""Ngày 101: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 101 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)

def main():
    out = output(101, exercise=False)
    policy = {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::course-example/raw/*"}, {"Effect": "Allow", "Action": ["s3:PutObject"], "Resource": "arn:aws:s3:::course-example/predictions/*"}]}
    write_json(out / "iam_policy_template.json", policy)
    print("Policy template, chưa tạo bucket hoặc cấp quyền thật.")


if __name__ == "__main__":
    main()
