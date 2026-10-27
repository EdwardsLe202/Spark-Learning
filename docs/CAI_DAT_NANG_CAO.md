# Cài theo chặng từ ngày 31 đến 150

[Lịch đầy đủ](../LO_TRINH_DAY_DU.md) · [Cài nền ngày 03](CAI_DAT.md)

Giữ Python **3.11** và Java **17**. Mỗi bài ghi môi trường cần dùng; chỉ cài khi tới chặng đó. Các thư viện được cố định để phù hợp ví dụ, không phải khuyến nghị luôn dùng phiên bản mới nhất. Các file requirements cố định phụ thuộc trực tiếp; sau khi cài thành công, lưu pip freeze của môi trường thực tế.

## 1. Spark nâng cao và ML

Ngày 31 trở đi tiếp tục dùng .venv đã có. Khi tới pandas/Arrow/sklearn/MLflow, cài:

```bash
source .venv/bin/activate
python -m pip install -r requirements-ml.txt
```

Bộ này gồm pandas 2.2.3, Arrow 17, sklearn 1.5.2, MLflow 2.22 và SQLAlchemy 2.0.40. Pin SQLAlchemy tránh API pool không tương thích với MLflow 2.22. Nếu chưa cài, ví dụ chỉ dùng PySpark vẫn chạy nhưng lab pandas UDF ngày 40 cần bổ sung bộ ML.

Snapshot tham chiếu đọc CSV giả lập trong data/raw; không cần tải dữ liệu cá nhân. `course_support.py` giữ các hàm chuẩn bị đầu vào, có docstring và được liên kết trong bài. Khi đề yêu cầu tự triển khai, chỉ gọi helper chưa đủ nghiệm thu.

## 2. Delta Lake ngày 44 và 48

Đọc [bảng tương thích Delta/Spark](https://docs.delta.io/releases/) trước khi thay phiên bản. Khóa chọn Delta 3.3.2 với Spark 3.5.7. Có thể dùng venv riêng:

```bash
uv venv --python 3.11 --seed .venv-delta
source .venv-delta/bin/activate
python -m pip install -r requirements-delta.txt
python scripts/run_day.py 44 --example
python scripts/run_day.py 48 --example
```

Mỗi lệnh tạo tiến trình mới; đừng dùng lại JVM đã mở không có Delta extension. Lần đầu cần mạng để tải JAR từ Maven, cache ở artifacts/full/ivy-cache. Cài package Python thành công chưa chứng minh JAR đã tải và query Delta chạy được. Nếu Maven không truy cập được, lưu lỗi và ghi phần Delta chưa kiểm chứng; không thay bằng Parquet rồi gọi đó là Delta merge.

Quay lại .venv chính khi học ML/API. Không sửa các môi trường riêng của dự án khác.

## 3. PostgreSQL/JDBC ngày 43

Ví dụ SQLite trong ngày 43 là fixture local, không phải Spark JDBC. Lab JDBC cần Docker đang hoạt động và JAR PostgreSQL:

```bash
export COURSE_DB_PASSWORD="local-fixture-password-change-before-real-use"
docker compose -f services/postgres.compose.yml up -d
python services/jdbc_smoke.py
```

Nguồn khởi tạo có 3 đơn, tổng 350000. Mật khẩu ví dụ chỉ là giá trị giả lập local; không dùng cho dữ liệu thật và không commit giá trị credential riêng của bạn. JAR 42.7.5 tải khi chạy Spark lần đầu. Source SQL chỉ được container PostgreSQL áp dụng khi volume mới được khởi tạo.

Dừng bằng `docker compose -f services/postgres.compose.yml down`. Volume database vẫn còn. Chỉ xóa volume thử nếu chủ động muốn xóa dữ liệu, không dùng down -v như cách chữa mọi lỗi.

## 4. Tests và MLflow ngày 81–90

```bash
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest tests -q
python scripts/run_day.py 86 --example
mlflow ui --backend-store-uri sqlite:///artifacts/full/mlflow.db --host 127.0.0.1 --port 5000
```

Experiment mới tên spark-course-150. Metadata SQLite và artifact ở hai vị trí khác nhau dưới artifacts/full; ghi lại cả hai nếu backup. UI chỉ mở loopback. Dừng Ctrl+C khi học xong. Các run của người học cần đủ code/data/split/version, không chỉ những trường tối thiểu của ví dụ.

## 5. Airflow ngày 91–94

Trước tiên cài đủ requirements-dev ở .venv và kiểm tra CLI:

```bash
python services/pipeline.py --step all --version cli-smoke
```

Sau đó ghi đường dẫn Python ML, chuyển sang môi trường Airflow riêng:

```bash
export COURSE_ROOT="$PWD"
export COURSE_PYTHON="$PWD/.venv/bin/python"
uv venv --python 3.11 --seed .venv-airflow
source .venv-airflow/bin/activate
export AIRFLOW_HOME="$PWD/artifacts/full/airflow"
export AIRFLOW__CORE__DAGS_FOLDER="$PWD/services/airflow/dags"
python -m pip install "apache-airflow==3.0.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.11.txt"
airflow standalone
```

Mở UI theo log, đăng nhập bằng thông tin standalone in ra. Trigger DAG churn_pipeline với snapshot_date=2025-07-01 và version riêng. DAG có schedule=None để không tự chạy nguồn lịch sử 2025 theo lịch hiện tại. Các task gọi CLI thật bằng COURSE_PYTHON, metadata nhỏ trả qua task output; không truyền DataFrame qua XCom.

Kiểm tra log interpreter/path, năm task, prediction và lỗi candidate gate. AST parse file chỉ là kiểm tra cú pháp, chưa nghiệm thu scheduler. Dừng standalone bằng Ctrl+C và kích hoạt lại .venv khi quay về các bài khác. [Tài liệu TaskFlow 3.0.0](https://airflow.apache.org/docs/apache-airflow/3.0.0/tutorial/taskflow.html) là nguồn đọc thêm đúng phiên bản.

## 6. Docker, batch và API ngày 95–110

Docker CLI và daemon phải đang hoạt động: `docker version`, `docker compose version`. Repo không tự cài hay bật daemon.

### Build và batch trong container

```bash
docker build -f services/Dockerfile -t spark-course-api:local .
mkdir -p artifacts/full
docker run --rm -v "$PWD/artifacts/full:/app/artifacts/full" spark-course-api:local python services/pipeline.py --step all --version container-v1
```

Nhánh image này phục vụ sklearn, không cần Java/Spark để predict. Dữ liệu giả lập nguồn được copy vào image; model/prediction ghi trong volume. Ghi kiến trúc ARM/x86 và phạm vi bạn đã thử. .dockerignore loại model cache, .env, Git và bản lưu khỏi build context.

### Chuẩn bị model và chạy API local

```bash
source .venv/bin/activate
python services/pipeline.py --step all --version api-v1
python services/release.py promote --version api-v1
export COURSE_API_KEY="local-fixture-key-change-before-real-use"
python -m uvicorn services.churn_api:app --host 127.0.0.1 --port 8000
```

API đọc con trỏ release current hoặc COURSE_MODEL_PATH nếu được đặt. Trước khi dùng pointer, bỏ biến COURSE_MODEL_PATH cũ bằng `unset COURSE_MODEL_PATH` nếu chính bạn đã đặt nó ở terminal. Không đặt model path sang artifact không tin cậy.

Mở /docs và /ready. Key được truyền trong header x-api-key. Model không tồn tại thì /health có thể 200, /ready và /predict trả 503. API không train trong lifespan/request. Khi đổi release pointer, restart process/worker rồi xác nhận model_version ở response.

### Compose API

Sau khi đã có model/release và COURSE_API_KEY:

```bash
docker compose -f services/compose.yml up --build
```

Artifact volume read-only trong API. Cổng host chỉ bind 127.0.0.1. Dừng Ctrl+C hoặc compose down; artifact host vẫn còn. Fixture key trong hướng dẫn chỉ dùng lab, không phải cơ chế identity/authorization production hoàn chỉnh.

### Batch scoring Spark model

Giữ hai artifact riêng. Sau khi chạy ví dụ ngày 60 và 72, có thể thử CLI Spark với artifact mẫu:

```bash
python services/batch_spark.py --model artifacts/full/day-072/example/pipeline --features artifacts/full/day-060/example/snapshot_date=2025-06-01 --output artifacts/full/batch-spark-demo --version spark-demo-v1
```

Mẫu trên chỉ kiểm tra khả năng load/score, không dùng test để lựa chọn model. Bài làm dùng cutoff mới, version/run/source thật đã chọn và đường dẫn riêng. Đích không được trùng nguồn.

## 7. Spark Standalone ngày 100

```bash
mkdir -p artifacts/full/cluster
docker compose -f services/spark.compose.yml up --build -d
docker compose -f services/spark.compose.yml exec master /usr/local/lib/python3.11/site-packages/pyspark/bin/spark-submit --master spark://master:7077 --deploy-mode client /workspace/services/cluster_smoke.py
```

Xem master UI http://127.0.0.1:8080. Kết quả cần 8 đơn, 1400000; output host ở artifacts/full/cluster/summary. Cả master/worker có cùng mount nguồn và output. Có thể thêm worker bằng `up --scale worker=2 -d` sau khi xem tài nguyên máy.

Các container vẫn nằm trên một máy vật lý. Ghi đúng giới hạn này. Với PySpark Standalone, lab dùng client mode; không khẳng định cluster deploy mode cho Python được hỗ trợ như mọi cluster manager. Dừng bằng `docker compose -f services/spark.compose.yml down`. Không cần cloud trả phí để nghiệm thu một môi trường triển khai.

## 8. PyTorch, AI và model local

Ngày 112–115 có thể chỉ cài `python -m pip install torch==2.6.0`. Khi tới pretrained/RAG:

```bash
python -m pip install -r requirements-ai.txt
python scripts/download_course_models.py embedding
python scripts/download_course_models.py generator
```

Chỉ tải reranker khi tới ngày 135:

```bash
python scripts/download_course_models.py reranker
```

Script chỉ tải khi bạn gọi rõ, không dùng API có phí. Cần mạng, dung lượng và RAM trống; model generator ở float32 và embedding cùng sống có thể chiếm vài GB. Chạy ít dịch vụ cùng lúc, giữ max input/output của lab, không coi Mac có CUDA.

Model ID: paraphrase-multilingual-MiniLM-L12-v2 (embedding), Qwen2.5-0.5B-Instruct (generation), mmarco-mMiniLMv2-L12-H384-v1 (reranker). Đọc model card/license ở nguồn học; chất lượng tiếng Việt cần đo, không được bảo đảm bởi tên model. Script ghi resolved commit và local_path trong artifacts/full/models/manifest.json. Tải lại đúng bản bằng --revision <commit> đã ghi.

Không commit model weights/cache. Chạy ví dụ cần model mà cache chưa có sẽ báo thiếu model; không đổi thành vector random rồi gọi đó là dense semantic retrieval. Qdrant local API fixture ngày 130 không cần tải model, nhưng lab semantic index có cần embedding thật.

## 9. Eval RAG và tool workflow

Retrieval từ vựng chạy không cần LLM:

```bash
python services/rag_eval.py --strategy sparse --split dev
```

Sau khi tải embedding/generator:

```bash
python services/rag_eval.py --strategy dense --split dev --generation
```

Chọn cấu hình trên dev, rồi chấm test cuối. `--split all` dùng khi tạo bảng 40 ca đầy đủ theo protocol đã chốt. Hybrid/reranked có thang score khác nên generation yêu cầu --min-score được bạn chọn trên dev. Script dùng cùng retrieval strategy cho metric và generation; bảng chấm correctness/groundedness/citation còn trống để bạn chấm tay. Keywords không là judge hoàn chỉnh.

Role CLI là fixture do người chạy lab đặt; API public thật phải lấy role từ tầng xác thực. Không để prompt hoặc JSON user tự cấp internal. Chỉ có tool read-only giả lập, không eval/exec/shell từ output model.

## 10. Load test và LoRA tùy chọn

Khi API ở terminal khác đã sẵn sàng, terminal gửi tải đặt cùng COURSE_API_KEY:

```bash
python services/load_test.py --requests 100 --concurrency 1
python services/load_test.py --requests 100 --concurrency 2
python services/load_test.py --requests 100 --concurrency 4
```

Ghi mọi lỗi/timeout, wall time, số mẫu, phiên bản và phần cứng. Không dùng percentile của số minh họa trong bài như benchmark thật.

LoRA ngày 148 là nhánh mở rộng theo tài nguyên:

```bash
python -m pip install -r requirements-finetune.txt
python services/finetune_lora.py --steps 2
```

Hai step chỉ smoke-check cơ chế adapter. Dùng dataset train có quyền qua --data khi làm thí nghiệm thật, giữ test độc lập và load adapter trong tiến trình mới. Không có claim chất lượng nếu chưa benchmark. Không cần thuê GPU hoặc cloud để hoàn thành phần cốt lõi như lộ trình gốc quy định.
