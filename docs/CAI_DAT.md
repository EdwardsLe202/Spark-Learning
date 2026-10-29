# Ngày 03 — Cài môi trường và chạy bằng uv

[Về ngày 03](../day-03/README.md)

Mục tiêu là Python 3.11, Java 17, PySpark 3.5.7. Chỉ làm bước tiếp theo khi bước hiện tại đã đúng. Bạn chưa cần hiểu cách Spark thực thi dữ liệu, chưa cần Docker hoặc công cụ ML.

## Bước 1 — Mở terminal ở thư mục repo

Trong trình soạn thảo, mở terminal tích hợp của thư mục Spark-Learning. **Terminal (cửa sổ chạy lệnh)** là nơi gõ những khối có nhãn bash. Chạy:

```bash
pwd
```

Kết quả phải kết thúc bằng `Spark-Learning`. Các lệnh bên dưới giả định bạn đang ở đây. Đừng dán nguyên cả file Python vào shell.

## Bước 2 — Kiểm tra công cụ tạo môi trường

Repo dùng **uv (công cụ quản lý môi trường Python)** để chọn Python 3.11 mà không phải thay Python toàn máy:

```bash
uv --version
```

Nếu hiện phiên bản uv, sang bước 3. Nếu command not found, mở phần này:

<details>
<summary>Chưa có uv</summary>

Nếu máy đã dùng Homebrew, chạy `brew install uv`, rồi kiểm tra `uv --version`. Nếu cũng chưa có Homebrew, ghi lại lỗi và nhờ hướng dẫn cài công cụ trước; bạn không cần tự đoán lệnh hệ thống. [Tài liệu uv](https://docs.astral.sh/uv/getting-started/installation/) có các cách cài chính thức.

Sau khi có uv, tiếp tục bước 3 bên dưới.

</details>

## Bước 3 — Để uv chuẩn bị môi trường của repo

Repo có `.python-version` chọn Python 3.11, `pyproject.toml` khai báo PySpark 3.5.7 và `uv.lock` chốt phiên bản phụ thuộc. Chạy ở gốc repo:

```bash
uv sync --locked
uv run python --version
uv run python -c "import sys; print(sys.executable)"
```

Bạn cần thấy Python 3.11.x và đường dẫn Python bên trong `.venv`. uv tự tạo môi trường và có thể tải Python nếu chưa có. Lần đầu cần mạng để tải PySpark; gói này khá lớn.

Không cần `source .venv/bin/activate`. Mỗi lần `uv run`, uv tự chọn môi trường của dự án. Python toàn máy không bị thay đổi.

## Bước 4 — Kiểm tra Java

Java là thành phần chạy bộ máy Spark, khác với thư viện Python. Chạy:

```bash
java -version
```

Nếu thấy phiên bản 17.x, tiếp tục. Nếu có Java 17 nhưng terminal đang chọn phiên bản khác, chọn JDK 17 đã được macOS nhận diện:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
export PATH="$JAVA_HOME/bin:$PATH"
java -version
```

`JAVA_HOME` là đường dẫn bộ Java. Hai lệnh export chỉ áp dụng trong terminal hiện tại.

<details>
<summary>Máy chưa có Java 17</summary>

Nếu dùng Homebrew, có thể cài `brew install openjdk@17`. Sau khi cài:

```bash
export JAVA_HOME="$(brew --prefix openjdk@17)/libexec/openjdk.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
java -version
```

Chỉ dùng nhánh này nếu cài Java bằng Homebrew. Không cần tạo symlink hệ thống hay sửa shell profile để bắt đầu học. Nếu lệnh không đúng trên máy của bạn, gửi lại kết quả, không thử trộn nhiều bản cài.

</details>

## Bước 5 — Kiểm tra PySpark bằng uv

```bash
uv run python -c "import pyspark; print(pyspark.__version__)"
```

Bạn cần thấy **3.5.7**. `uv sync` ở bước 3 đã cài thư viện; không cần gọi pip. Các file requirements cho ML/API/AI thuộc chặng nâng cao, chưa cần cài ở khóa nền này.

## Bước 6 — Chạy bài học bằng uv

```bash
uv run python scripts/run_day.py 03 --example
uv run python scripts/run_day.py 03
```

Bài làm in và kiểm tra Python 3.11.x, PySpark 3.5.7, Java 17 cùng đường dẫn interpreter. Mở terminal mới ở gốc repo và chạy lại cùng lệnh; không cần activate.

Ngày 04 chạy Spark thật bằng `uv run python scripts/run_day.py 04 --example`, có bảng ba dòng và count=3. Bài làm ngày 04 thêm O004, nên bảng cuối có 4 dòng.

Bạn cũng có thể chạy trực tiếp file của ngày 01–08, ví dụ:

```bash
uv run python day-08/bai_lam.py
uv run python day-08/vi_du.py
```

Runner là cách dùng chung cho cả lộ trình, tự thêm đường dẫn import và đặt thư mục làm việc đúng. Các ngày nâng cao có thể cần thư viện và dịch vụ riêng theo README của ngày.

## Khi gặp lỗi

| Thấy gì? | Kiểm tra trước |
| --- | --- |
| Không tìm được scripts/run_day.py | pwd có đang ở Spark-Learning không? |
| ModuleNotFoundError: pyspark | Có đang chạy bằng uv run ở gốc repo không? Thử uv sync --locked. |
| Java gateway exited ở ngày 04 | java -version, JAVA_HOME và dòng nguyên nhân Java trước thông báo cuối |
| Python worker lệch phiên bản | Chạy uv run python scripts/run_day.py; runner đặt Python worker theo Python đang chạy nếu chưa cấu hình khác |
| Lỗi bind/hostname local | Có thể thử `export SPARK_LOCAL_IP=127.0.0.1` trong terminal học rồi chạy lại; đây chỉ là cấu hình local |
| Notebook chạy khác terminal | Khóa bắt đầu bằng file Python; chưa cần notebook để hoàn thành các ngày đầu |

Khi hỏi lỗi, gửi ngày học, nguyên lệnh, phiên bản và phần log có nguyên nhân. Không cần tự debug tất cả lỗi cài đặt trong một buổi.
