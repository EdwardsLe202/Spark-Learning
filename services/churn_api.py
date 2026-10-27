"""API nhánh sklearn; chỉ load model, không train trong lifespan/request.

COURSE_API_KEY phải được đặt bởi môi trường. Dùng dữ liệu giả lập trong lab.
"""
from contextlib import asynccontextmanager
from pathlib import Path
import os
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from course_support import FULL, FEATURES, read_json
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from pydantic import BaseModel, ConfigDict, Field


class PredictionInput(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    events_30d: int = Field(ge=0, le=1000000)
    spend_30d: float = Field(ge=0)
    recency_days: float | None = Field(default=None, ge=0)
    region: str = Field(min_length=1, max_length=40)
    plan: str = Field(min_length=1, max_length=40)


@asynccontextmanager
async def lifespan(app):
    import joblib
    configured = os.environ.get("COURSE_MODEL_PATH")
    pointer = FULL / "releases/current.json"
    path = Path(configured) if configured else (ROOT / read_json(pointer)["model_path"] if pointer.exists() else FULL / "models/churn.joblib")
    app.state.model = None
    app.state.metadata = {}
    if path.exists() and path.with_suffix(".json").exists():
        app.state.metadata = read_json(path.with_suffix(".json"))
        if app.state.metadata.get("features") != FEATURES:
            raise ValueError("Model metadata không khớp contract API")
        app.state.model = joblib.load(path)
    yield
    app.state.model = None


app = FastAPI(lifespan=lifespan)


def require_key(x_api_key: str | None = Header(default=None)):
    import hmac
    expected = os.environ.get("COURSE_API_KEY")
    if not expected:
        raise HTTPException(503, "Chưa cấu hình khóa truy cập lab")
    if x_api_key is None or not hmac.compare_digest(x_api_key, expected):
        raise HTTPException(401, "Khóa truy cập không hợp lệ")


@app.get("/health")
def health():
    return {"status": "alive"}


@app.get("/ready")
def ready(request: Request):
    if request.app.state.model is None:
        raise HTTPException(503, "Model chưa sẵn sàng")
    return {"status": "ready", "model_version": request.app.state.metadata["model_version"]}


@app.post("/predict", dependencies=[Depends(require_key)])
def predict(body: PredictionInput, request: Request):
    import pandas as pd
    if request.app.state.model is None:
        raise HTTPException(503, "Model chưa sẵn sàng")
    start = time.perf_counter()
    frame = pd.DataFrame([body.model_dump()], columns=FEATURES)
    score = float(request.app.state.model.predict_proba(frame)[:, 1][0])
    metadata = request.app.state.metadata
    return {"score": score, "prediction": int(score >= metadata["threshold"]),
            "model_version": metadata["model_version"], "request_id": uuid.uuid4().hex,
            "duration_ms": (time.perf_counter() - start) * 1000}
