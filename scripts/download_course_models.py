"""Tải chủ động model miễn phí cho lab; không tải khi import module khác."""
from pathlib import Path
import argparse
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import FULL, read_json, write_json
from rag_support import MODEL_IDS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=list(MODEL_IDS))
    parser.add_argument("--revision", default="main", help="Có thể truyền commit cụ thể để tải lại đúng bản")
    args = parser.parse_args()
    cache = FULL / "hf_cache"
    os.environ.setdefault("HF_HOME", str(cache))
    from huggingface_hub import snapshot_download
    local = snapshot_download(MODEL_IDS[args.kind], revision=args.revision, cache_dir=str(cache),
                              allow_patterns=["*.json", "*.txt", "*.model", "*.safetensors", "1_Pooling/*", "2_Normalize/*"])
    manifest_path = FULL / "models/manifest.json"
    records = read_json(manifest_path) if manifest_path.exists() else {}
    records[args.kind] = {"model_id": MODEL_IDS[args.kind], "requested_revision": args.revision,
                          "resolved_revision": Path(local).name, "local_path": local}
    write_json(manifest_path, records)
    print(records[args.kind])


if __name__ == "__main__":
    main()
