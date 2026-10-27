# Ngày 03 — Cài môi trường, từng bước

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

Nếu máy đã có lệnh python3.11, có thể dùng `python3.11 -m venv .venv` thay bước uv tạo môi trường. Các bước activate, pip và kiểm tra phía sau vẫn giữ nguyên.

</details>

## Bước 3 — Tạo và chọn Python riêng cho repo

**Virtual environment (môi trường Python riêng)** được lưu trong thư mục .venv. Chạy từng lệnh:

```bash
uv venv --python 3.11 --seed .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
```

Bạn cần thấy Python 3.11.x và đường dẫn Python bên trong .venv. `--seed` cài pip để dùng ở bước 5. uv có thể tải Python nếu chưa có, nên bước đầu cần mạng.

Nếu đã có .venv của repo từ trước, thử activate và kiểm tra phiên bản trước; không xóa môi trường đang có để tạo lại một cách mù quáng. Khi Python chưa đúng, dừng và ghi kết quả cần sửa.

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

## Bước 5 — Cài PySpark vào đúng môi trường

Vẫn ở terminal đã activate .venv:

```bash
python -m pip install -r requirements.txt
python -c "import pyspark; print(pyspark.__version__)"
```

Bạn cần thấy **3.5.7**. Package Spark tương đối lớn, lần cài đầu cần mạng và thời gian tải. `python -m pip` dùng pip gắn với chính Python đang chạy. Các requirements-ml/api/ai ở repo thuộc bản tham khảo cũ; chưa cài chúng ở khóa nền này.

## Bước 6 — Chạy kiểm tra phiên bản của ngày 03

```bash
python scripts/run_day.py 03 --example
```

Ghi Python 3.11.x, PySpark 3.5.7, Java 17 và đường dẫn interpreter vào nhật ký ngày 03. Sau đó mở terminal mới, activate lại và chạy được cùng lệnh là đạt mục tiêu.

Ngày 04 mới chạy Spark thật bằng `python scripts/run_day.py 04 --example`, có bảng ba dòng và count=3. Không cần tự học Parquet hay Spark UI để hoàn thành cài đặt.

## Khi gặp lỗi

| Thấy gì? | Kiểm tra trước |
| --- | --- |
| Không tìm được scripts/run_day.py | pwd có đang ở Spark-Learning không? |
| ModuleNotFoundError: pyspark | Python có thuộc .venv không? Đã cài requirements bằng chính Python đó chưa? |
| Java gateway exited ở ngày 04 | java -version, JAVA_HOME và dòng nguyên nhân Java trước thông báo cuối |
| Python worker lệch phiên bản | Chạy qua runner; nó đặt Python worker theo Python đang chạy nếu chưa cấu hình khác |
| Lỗi bind/hostname local | Có thể thử `export SPARK_LOCAL_IP=127.0.0.1` trong terminal học rồi chạy lại; đây chỉ là cấu hình local |
| Notebook chạy khác terminal | Khóa bắt đầu bằng file Python; chưa cần notebook để hoàn thành các ngày đầu |

Khi hỏi lỗi, gửi ngày học, nguyên lệnh, phiên bản và phần log có nguyên nhân. Không cần tự debug tất cả lỗi cài đặt trong một buổi.
