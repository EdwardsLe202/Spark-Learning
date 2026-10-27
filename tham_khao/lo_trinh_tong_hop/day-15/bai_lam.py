"""Ngày 15: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 15
"""
from spark_lab import ROOT, DATA, output_dir

import mlflow
from spark_lab import ROOT, output_dir
store = ROOT / "artifacts" / "mlflow.db"
store.parent.mkdir(exist_ok=True)
mlflow.set_tracking_uri("sqlite:///" + str(store))
mlflow.set_experiment("spark-learning-churn")
with mlflow.start_run(run_name="metadata-demo") as run:
    mlflow.log_param("seed", 42)
    mlflow.set_tag("data_manifest", "data/raw/manifest.json")
    mlflow.log_artifact(str(ROOT / "data/raw/manifest.json"))
    print("run_id:", run.info.run_id)

# Bài tự làm hôm nay:
# TODO Chạy ví dụ rồi xem UI với lệnh trong docs/CAI_DAT.md. Phân biệt run metadata với model artifact.
# TODO Chạy ít nhất 5 thí nghiệm nhỏ từ ngày 13–14, mỗi run log cấu hình, validation metric, thời gian, snapshot hash, code reference và schema. Không dùng metric bịa để đủ số run.
# TODO Dùng mlflow.sklearn.log_model với pipeline, signature và input_example. Đăng ký model dưới tên churn-sklearn, lưu version cụ thể.
# TODO Tạo alias candidate, load model theo version và kiểm tra cùng fixture như ngày 14. Giữ Spark model tên riêng nếu log thêm nhánh đó.
# TODO Viết một prediction metadata gồm customer_id, snapshot_date, model_version, run_id, data_hash và code_reference.
