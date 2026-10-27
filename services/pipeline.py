"""CLI tham chiếu các ngày 81–105; dùng dữ liệu giả lập và sklearn cho nhánh API.

python services/pipeline.py --step all --snapshot-date 2025-07-01 --version demo-v1
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import FULL, FEATURES, snapshot_pd, sklearn_pipeline, data_hash, write_json, read_json


def run_step(step, snapshot_date="2025-07-01", version="demo-v1", min_ap=0.0):
    import joblib
    import pandas as pd
    from sklearn.metrics import average_precision_score
    # Version là tên thư mục, không chấp nhận đường dẫn từ input.
    if not version or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_." for c in version) or version in {".", ".."}:
        raise ValueError("Version chỉ dùng chữ, số, dấu - _ .")
    base = FULL / "runs" / version
    base.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    if step == "validate":
        frame = snapshot_pd(snapshot_date, include_labels=False)
        if frame.customer_id.duplicated().any() or len(frame) != 120:
            raise ValueError("Khóa/số dòng snapshot không hợp lệ")
        result = {"rows": len(frame), "snapshot_date": snapshot_date, "data_hash": data_hash()}
    elif step == "features":
        frame = snapshot_pd(snapshot_date, include_labels=False)
        path = base / ("features-" + snapshot_date + ".parquet")
        frame.to_parquet(path, index=False)
        result = {"rows": len(frame), "path": str(path.relative_to(ROOT))}
    elif step == "train":
        train = snapshot_pd("2025-02-01")
        model = sklearn_pipeline().fit(train[FEATURES], train.label)
        joblib.dump(model, base / "model.joblib")
        metadata = {"model_version": version, "threshold": 0.5, "features": FEATURES,
                    "data_hash": data_hash(), "training_snapshot": "2025-02-01",
                    "code_hash": hashlib.sha256(Path(__file__).read_bytes() + (ROOT / "course_support.py").read_bytes()).hexdigest()}
        write_json(base / "model.json", metadata)
        result = metadata
    elif step == "evaluate":
        val = snapshot_pd("2025-04-01")
        model = joblib.load(base / "model.joblib")
        ap = float(average_precision_score(val.label, model.predict_proba(val[FEATURES])[:, 1]))
        result = {"validation_ap": ap, "min_ap": min_ap, "accepted": ap >= min_ap}
        write_json(base / "evaluation.json", result)
        if not result["accepted"]:
            raise ValueError("Candidate không đạt gate; không phát hành/score tự động")
    elif step == "score":
        evaluation = read_json(base / "evaluation.json")
        if not evaluation.get("accepted"):
            raise ValueError("Candidate chưa được chấp nhận")
        frame = pd.read_parquet(base / ("features-" + snapshot_date + ".parquet"))
        metadata = read_json(base / "model.json")
        model = joblib.load(base / "model.joblib")
        scored = frame[["customer_id", "snapshot_date"]].copy()
        scored["score"] = model.predict_proba(frame[FEATURES])[:, 1]
        scored["prediction"] = (scored.score >= metadata["threshold"]).astype(int)
        scored["model_version"] = version
        scored["data_hash"] = metadata["data_hash"]
        path = base / ("predictions-" + snapshot_date + ".parquet")
        scored.to_parquet(path, index=False)
        result = {"rows": len(scored), "path": str(path.relative_to(ROOT))}
    else:
        raise ValueError("Bước không hỗ trợ: " + step)
    result = {"step": step, "version": version, "duration_seconds": time.perf_counter() - start, **result}
    write_json(base / (step + "-last.json"), result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", choices=["all", "validate", "features", "train", "evaluate", "score"], default="all")
    parser.add_argument("--snapshot-date", default="2025-07-01")
    parser.add_argument("--version", default="demo-v1")
    parser.add_argument("--min-ap", type=float, default=0.0, help="Gate học tập; tự chọn trên validation, không dùng test")
    args = parser.parse_args()
    steps = ["validate", "features", "train", "evaluate", "score"] if args.step == "all" else [args.step]
    for step in steps:
        print(json.dumps(run_step(step, args.snapshot_date, args.version, args.min_ap), ensure_ascii=False))


if __name__ == "__main__":
    main()
