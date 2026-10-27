"""Ngày 129: ví dụ tham chiếu; đọc lý thuyết và điều kiện trước khi chạy.
Chạy: python scripts/run_day.py 129 --example
"""
from pathlib import Path
import sys, os, json
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import (DATA, FULL, FEATURES, output, write_json, read_json, data_hash,
    snapshot_pd, sklearn_pipeline, fit_sklearn, ensure_demo_model, setup_tracking, metric_counts)
import numpy as np

def main():
    out = output(129, exercise=False)
    from rag_support import embedding_model, model_manifest
    import numpy as np
    model = embedding_model()
    vectors = model.encode(["Spark xử lý bảng dữ liệu", "Đơn hàng có số tiền"], normalize_embeddings=True)
    print("Shape:", vectors.shape, "Norm:", np.linalg.norm(vectors, axis=1).tolist())
    print(model_manifest("embedding"))


if __name__ == "__main__":
    main()
