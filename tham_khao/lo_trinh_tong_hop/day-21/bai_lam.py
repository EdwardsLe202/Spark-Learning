"""Ngày 21: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 21
"""
from spark_lab import ROOT, DATA, output_dir

from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()
class PredictionRequest(BaseModel):
    events_30d: int = Field(ge=0)
    spend_30d: float = Field(ge=0)
    recency_days: float | None = Field(default=None, ge=0)
    region: str = Field(min_length=1, max_length=20)
    plan: str = Field(min_length=1, max_length=20)
@app.get("/health")
def health():
    return {"status": "alive"}
# TODO: load model sklearn trong lifespan; thêm /ready và POST /predict.

# Bài tự làm hôm nay:
# TODO Cài requirements-api.txt. Sửa bai_lam.py thành ứng dụng FastAPI; chạy bằng lệnh uvicorn ghi dưới phần “Cách chạy”.
# TODO Load artifacts/day-14/model.joblib một lần trong lifespan. Tạo /health, /ready và POST /predict theo contract năm feature ngày 14.
# TODO Chuyển đúng một request thành DataFrame pandas một dòng, gọi predict_proba, áp threshold đã chọn, trả model_version và request_id.
# TODO Dùng httpx/TestClient viết test: đúng input, thiếu spend, events âm, sai kiểu, category mới. So response score với gọi trực tiếp pipeline trên cùng input.
# TODO Thêm giới hạn số dòng mỗi request nếu hỗ trợ batch; log request_id, runtime, version và mã lỗi. Ghi cách dừng bằng Ctrl+C.
