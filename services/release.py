"""Promote/rollback con trỏ model local; API cần restart để load lại."""
from pathlib import Path
import argparse
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import FULL, FEATURES, read_json, write_json


def atomic_json(path, value):
    temporary = Path(str(path) + ".tmp")
    write_json(temporary, value)
    os.replace(temporary, path)


def promote(version):
    if not version or version in {".", ".."} or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_." for c in version):
        raise ValueError("Version không hợp lệ")
    model = FULL / "runs" / version / "model.joblib"
    metadata = read_json(model.with_suffix(".json"))
    evaluation = read_json(model.parent / "evaluation.json")
    if not model.exists() or not evaluation.get("accepted") or metadata["features"] != FEATURES:
        raise ValueError("Candidate chưa đạt gate/contract")
    pointer = {"model_version": version, "model_path": str(model.relative_to(ROOT)), "data_hash": metadata["data_hash"]}
    current = FULL / "releases/current.json"
    if current.exists():
        atomic_json(FULL / "releases/previous.json", read_json(current))
    atomic_json(current, pointer)
    return pointer


def rollback():
    previous = read_json(FULL / "releases/previous.json")
    if not (ROOT / previous["model_path"]).is_file():
        raise ValueError("Artifact previous không còn")
    atomic_json(FULL / "releases/current.json", previous)
    return previous


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["promote", "rollback"])
    parser.add_argument("--version")
    args = parser.parse_args()
    print(promote(args.version) if args.action == "promote" else rollback())
