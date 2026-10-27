# Cài môi trường thực hành trên macOS

[Lộ trình](../README.md) · [Dữ liệu](../data/README.md)

Chỉ cài công cụ khi tới ngày cần dùng. Repo chọn **Python 3.11 + Java 17 + PySpark 3.5.7**, dùng Spark Classic ở `local[2]`. Các số phiên bản này là bộ học cố định, không phải yêu cầu dùng bản mới nhất. [Tài liệu cài PySpark 3.5.7](https://spark.apache.org/docs/3.5.7/api/python/getting_started/install.html) mô tả yêu cầu Java và Python.

## 1. Kiểm tra máy và terminal

Chạy từ thư mục repo:

```bash
pwd
uname -m
sw_vers
sysctl -n hw.memsize
df -h .
python3 --version
java -version
/usr/libexec/java_home -V
```

`arm64` là Apple Silicon, `x86_64` thường là Intel hoặc terminal đang chạy qua lớp tương thích. Dùng Python và gói native cùng kiến trúc. Nếu Python mặc định là 3.14, vẫn tạo môi trường 3.11 cho repo; không cần thay Python toàn máy. RAM và dung lượng cần thiết tăng theo dịch vụ; bắt đầu dữ liệu nhỏ, chạy từng dịch vụ và theo dõi máy thay vì bật mọi thứ cùng lúc.

## 2. Tạo môi trường Python riêng

Nếu đã có `uv` (công cụ quản lý môi trường và package Python):

```bash
uv venv --python 3.11 --seed .venv
source .venv/bin/activate
python --version
uv pip install --python .venv/bin/python -r requirements.txt
```

`uv` có thể tải Python 3.11 nếu máy chưa có, nên lần đầu cần mạng. `--seed` cài pip để các lệnh `python -m pip` bên dưới dùng được. Nếu dùng Homebrew và chưa có uv, có thể cài `brew install uv` trước.

Nếu đã có lệnh `python3.11`, có thể dùng cách chuẩn thay cho uv:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Chọn một cách tạo môi trường. Không cần chạy cả hai lên cùng `.venv`. Mỗi terminal mới phải chạy `source .venv/bin/activate`. Ghi đường dẫn `python` bằng:

```bash
python -c "import sys; print(sys.executable)"
```

## 3. Chọn Java 17

Nếu JDK 17 đã được macOS nhận diện:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH="$JAVA_HOME/bin:$PATH"
java -version
```

Nếu chưa có Java, cài JDK 17 phù hợp kiến trúc máy. Với Homebrew, `brew install openjdk@17` là một lựa chọn. Không cần tạo symlink hệ thống để học repo; có thể chọn trực tiếp đường dẫn:

```bash
export JAVA_HOME="$(brew --prefix openjdk@17)/libexec/openjdk.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
java -version
```

Chỉ chạy nhánh Homebrew nếu đã cài JDK bằng Homebrew. Giữ các biến này trong terminal học hoặc cấu hình shell của chính bạn nếu cần; repo không sửa shell profile.

## 4. Kiểm tra Spark

```bash
python scripts/run_day.py 02
```

Phải in kiểm tra tổng 5, ghi Parquet rồi đọc lại hai dòng. Đầu ra nằm ở `artifacts/day-02/`. Nếu muốn xem Spark UI, thêm `input("Enter để dừng")` bên trong khối `with spark_session(...)`, rồi mở địa chỉ UI trong log khi phiên còn chạy. Cổng thường là 4040, có thể tăng khi cổng đã được dùng.

Ghi phiên bản sau khi chạy thành công:

```bash
python -m pip freeze > requirements-lock-local.txt
python -c "import pyspark, sys; print(sys.version); print(pyspark.__version__)"
```

Các file requirements của repo cố định dependency trực tiếp. `requirements-lock-local.txt` ghi cả dependency gián tiếp đã giải trên máy bạn; được Git bỏ qua mặc định. Nếu chia sẻ lock, kiểm tra không có đường dẫn riêng hay token rồi lưu bản đã kiểm tra với tên khác.

## 5. Bổ sung theo chặng

| Ngày | Cài thêm | Mục đích |
| --- | --- | --- |
| 02–13, 16 | `requirements.txt` | PySpark và pytest |
| 14–20 | `requirements-ml.txt` | pandas, Arrow, sklearn, MLflow |
| 21, 23, 24, 28 | `requirements-api.txt` | FastAPI, Pydantic, HTTP client |
| 22 | riêng `torch==2.6.0` hoặc `requirements-ai.txt` | Tensor và training CPU |
| 25–27 | `requirements-ai.txt` | Sentence Transformers và Qdrant local |

Ví dụ ngày 14:

```bash
python -m pip install -r requirements-ml.txt
```

Mỗi file chặng sau đã bao gồm chặng trước, không cần cài lại từng file. Môi trường đủ cả RAG sẽ nặng hơn nền Spark. Không bắt buộc API có phí; model embedding tải lần đầu cần mạng và dung lượng cache. Nếu dùng dịch vụ model, chọn provider, model và hạn mức riêng; secret đi qua biến môi trường ngoài Git.

Nhánh ML cố định thêm SQLAlchemy 2.0.40: kiểm tra thực tế cho thấy MLflow 2.22 không import được với SQLAlchemy 2.1 do API pool đã thay đổi. Giữ pin này nếu sử dụng bộ MLflow của repo.

## 6. MLflow local

Ngày 15 dùng MLflow **2.22.0**, SQLite tường minh và artifact local. Chạy từ gốc repo sau khi đã có run:

```bash
mlflow ui --backend-store-uri sqlite:///artifacts/mlflow.db --host 127.0.0.1 --port 5000
```

Mở `http://127.0.0.1:5000`; nếu cổng bận đổi thành 5001. Các lệnh trong bài dành cho MLflow 2.22; đừng đổi sang MLflow 3 rồi giữ nguyên mọi API mà chưa đối chiếu. UI dừng bằng Ctrl+C, dữ liệu SQLite/artifact vẫn còn nếu không xóa file.

## 7. API local

Sau khi hoàn thiện ngày 21, mở terminal thứ hai, kích hoạt môi trường và chạy từ gốc:

```bash
python -m uvicorn bai_lam:app --app-dir day-21 --host 127.0.0.1 --port 8000
```

Mở `http://127.0.0.1:8000/docs`. Trước khi hoàn thiện TODO, starter chỉ có `/health`; chưa có dự đoán thật. Ngày 23 cần API chạy song song lúc gửi tải. Dừng bằng Ctrl+C.

## 8. Airflow và Docker là môi trường riêng

Phần cốt lõi ngày 17 chạy workflow local. Nếu làm nhánh Airflow, dùng venv riêng với Python 3.11 và constraints đúng **Airflow 3.0.0**; không trộn vào venv ML:

```bash
uv venv --python 3.11 --seed .venv-airflow
source .venv-airflow/bin/activate
python -m pip install "apache-airflow==3.0.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.11.txt"
export AIRFLOW_HOME="$PWD/artifacts/airflow"
airflow standalone
```

Airflow standalone tạo môi trường demo, không phải cấu hình production. Theo [tài liệu Airflow 3.0](https://airflow.apache.org/docs/apache-airflow/3.0.0/start.html) để lấy thông tin đăng nhập và thư mục DAG. Task gọi code repo cần đúng working directory và interpreter của venv ML; đừng mặc định worker có PySpark chỉ vì terminal học có. Tắt standalone trước khi quay lại chặng khác; kích hoạt lại `.venv`.

Docker: dùng Docker Desktop hoặc runtime đã có trên máy, kiểm tra `docker version` và `docker compose version` khi tới ngày 18. Repo không tự khởi động daemon hay kéo image. Nếu chưa có runtime, thực hiện clean run bằng venv và ghi Docker chưa kiểm chứng. Chỉ gọi phần mở rộng hoàn thành khi build/run thật.

## 9. Chẩn đoán lỗi thường gặp

| Triệu chứng | Kiểm tra trước |
| --- | --- |
| `ModuleNotFoundError` | `sys.executable`, venv đang kích hoạt, package cài vào đúng Python |
| `JAVA_GATEWAY_EXITED` | `java -version`, `JAVA_HOME`, Java 17 và log nguyên nhân trước dòng lỗi cuối |
| Python worker khác phiên bản | `PYSPARK_PYTHON`, interpreter driver/worker; tiện ích repo đặt worker theo Python đang chạy |
| Lỗi bind/hostname trên máy local | Thử trong terminal học `export SPARK_LOCAL_IP=127.0.0.1`, rồi chạy lại; không dùng thiết lập này cho cluster thật |
| Cổng 4040/5000/8000 bận | Dừng phiên cũ hoặc chọn cổng khác, ghi cổng thực tế |
| Không tìm thấy artifact ngày trước | Chạy lại ngày tạo artifact theo nhật ký; không tạo tệp rỗng để bỏ qua |
| Timestamp/cast không đúng | Xem schema, chuỗi nguồn, timezone và cấu hình ANSI; thu nhỏ về tiny fixture |
| Thiếu RAM | Đóng dịch vụ khác, giảm dữ liệu/batch/worker, tránh collect/toPandas toàn bộ |

Khi gửi lỗi để được hỗ trợ, kèm ngày học, lệnh, phiên bản, phần đầu log có nguyên nhân và fixture nhỏ tái hiện.

