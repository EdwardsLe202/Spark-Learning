# Ngày 03 — Cài đúng môi trường trước khi viết Spark

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Có Python 3.11, Java 17, PySpark 3.5.7 trong môi trường của repo.

## 1. Hôm nay cài gì?

Bạn viết Python, nhưng bộ máy Spark còn cần Java để chạy. **Dependency (thư viện chương trình cần)** trong khóa nền này chỉ là PySpark. Repo giữ bộ Python 3.11, Java 17 và PySpark 3.5.7 để ví dụ có môi trường nhất quán; chưa cần cài công cụ dữ liệu khác.

**Terminal (cửa sổ chạy lệnh)** là nơi bạn gõ `uv run python ...`. Một lệnh shell và một câu Python là hai thứ khác nhau: `uv run python --version` gõ trong terminal; `print(1 + 2)` viết trong file Python. Khi tài liệu đặt code trong khối bash, chạy ở terminal; khối python là nội dung Python.

## 2. Vì sao tạo môi trường riêng?

**Virtual environment (môi trường Python riêng)** là thư mục giữ Python và các gói dành cho repo. uv tạo thư mục `.venv` và chọn môi trường ấy mỗi lần bạn chạy `uv run`. Mở terminal khác, chỉ cần đứng ở gốc repo và chạy lại cùng lệnh; không cần activate.

`uv sync` cài các gói từ `pyproject.toml` theo phiên bản đã chốt trong `uv.lock`. `uv run` cũng tự đồng bộ môi trường trước khi chạy. `JAVA_HOME` chỉ tới JDK; bạn làm theo nhánh phù hợp trong hướng dẫn cài đặt, chưa cần tự sửa file cấu hình hệ thống.

## 3. Kiểm tra từng bước

Mở hướng dẫn cài đặt được liên kết ở bài thực hành và làm từng bước. Chỉ chạy bước kế khi bước trước đã có đầu ra đúng. Nếu Python hệ thống là 3.14, không cần gỡ nó; tạo `.venv` dùng 3.11. File `.python-version` nhắc uv chọn 3.11 nhưng không tự đổi mọi lệnh python của máy.

Chương trình mẫu hôm nay chỉ in phiên bản. Chưa có xử lý bảng Spark; ngày 04 mới tạo bảng đầu tiên. Nếu mắc lỗi cài đặt, dành thời gian sửa và dừng ở ngày 03, không chuyển sang bài khó hơn để bù lịch.

## Ví dụ có thể chạy nguyên file

Làm cài đặt ở bài thực hành trước khi chạy ví dụ này.

```python
import subprocess
import sys
import pyspark
print("Python:", sys.version.split()[0])
print("Python đang chạy:", sys.executable)
print("PySpark:", pyspark.__version__)
subprocess.run(["java", "-version"], check=True)
```

## Đọc từng phần của ví dụ

- sys.version cho biết Python của tiến trình hiện tại.
- sys.executable cho biết đường dẫn để nhận ra có đang ở .venv không.
- Import pyspark kiểm tra thư viện đã cài. java -version kiểm tra Java có chạy được, nhưng Spark đầy đủ còn được kiểm tra ngày 04.

## Kết quả để đối chiếu

Python 3.11.x, PySpark 3.5.7, Java 17; đường dẫn Python thuộc môi trường bạn chủ động chọn.

## Từ mới cần nhận ra hôm nay

- **Terminal (cửa sổ chạy lệnh)**.
- **Virtual environment (môi trường Python riêng)**.
- **Dependency (thư viện chương trình cần)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Dùng uv run ở terminal mới có cần activate lại không?
2. Import pyspark thành công đã kiểm tra toàn bộ Spark chưa?
3. Có cần gỡ Python toàn máy không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không; đứng ở gốc repo rồi dùng uv run, uv tự chọn môi trường.
2. Chưa; ngày 04 còn kiểm tra Java và phiên xử lý thật.
3. Không; dùng môi trường riêng.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
