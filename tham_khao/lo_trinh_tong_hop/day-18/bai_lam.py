"""Ngày 18: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 18
"""
from spark_lab import ROOT, DATA, output_dir, spark_session, read_events, read_customers
from pyspark.sql import functions as F

if __name__ == "__main__":
    with spark_session("day-18") as spark:
        from pyspark.ml import PipelineModel
        model_path = ROOT / "artifacts/day-12/model"
        if not model_path.exists():
            raise FileNotFoundError("Hãy hoàn thành và lưu model ở ngày 12 trước.")
        model = PipelineModel.load(str(model_path))
        print("Đã load model Spark; cần feature có cùng schema và preprocessing.")
        # TODO: đọc feature snapshot mới, transform, thêm metadata, ghi theo khóa đã chọn.

# Bài tự làm hôm nay:
# TODO Tạo feature cutoff 2025-07-01 bằng hàm ngày 11. Batch score bằng model ngày 12; không fit lại preprocessing.
# TODO Ghi score lớp 1 và metadata; chọn khóa (customer_id, snapshot_date, model_version). Chạy lại cùng đầu vào và đối chiếu số dòng.
# TODO Viết predict CLI chạy được trong terminal mới bằng đường dẫn model và feature tường minh.
# TODO Với Docker, bắt đầu nhánh sklearn nhẹ: cài requirements-ml.txt, gắn model và input bằng volume, chạy predict CLI. Ghi cách build, run và kiến trúc máy. Nếu chưa có Docker, thực hiện venv sạch và ghi giới hạn kiểm chứng.
# TODO Viết bảng dữ liệu nào nằm trong image, container và volume; thử xóa container thử rồi đọc lại volume.
