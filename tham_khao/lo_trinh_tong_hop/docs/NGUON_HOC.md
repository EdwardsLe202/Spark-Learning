# Nguồn học và đối chiếu

Repo được biên soạn theo 30 phần của [tài liệu gốc](../Lo_trinh_Spark_MLOps_AI_Engineering.docx), mỗi phần có năm ý, tương ứng một ngày. Phần “Năm ý đối chiếu” trong từng lý thuyết giữ thứ tự gốc; phần giải thích và lab được viết cho vòng học 30 ngày.

Bộ nền: Python 3.11, Java 17, PySpark 3.5.7. Nhánh ML dùng scikit-learn 1.5.2 và MLflow 2.22.0; nhánh API dùng FastAPI 0.115.12/Pydantic 2; PyTorch 2.6.0. Các file requirements cố định dependency trực tiếp, chưa phải lock đầy đủ phụ thuộc gián tiếp. Sau khi cài thành công và smoke check, lưu pip freeze để tái lập máy của bạn.

Tài liệu không gắn phiên bản hoặc trỏ tới main có thể cập nhật. Đối chiếu API với package đã cài; main của PEFT chỉ dùng định hướng khái niệm, không là yêu cầu phải cài main. Không nâng toàn bộ thư viện giữa lộ trình chỉ để khớp trang latest.

Các nguồn chính thức sau hỗ trợ khái niệm và API; ví dụ, fixture, thời lượng, câu hỏi và rubric là thiết kế học tập của repo. Nguồn đã đối chiếu khi biên soạn gồm yêu cầu PySpark, Structured Streaming, ML pipelines/tuning, FastAPI, PyTorch, MLflow, hybrid search và LoRA; các liên kết khác là tài liệu đọc thêm, không thay thế kiểm chứng môi trường.

## Ngày 01 — Spark trong công việc Data Science

- [Spark overview](https://spark.apache.org/docs/3.5.7/)
- [PySpark overview](https://spark.apache.org/docs/3.5.7/api/python/index.html)

## Ngày 02 — Môi trường Spark trên macOS

- [PySpark installation 3.5.7](https://spark.apache.org/docs/3.5.7/api/python/getting_started/install.html)

## Ngày 03 — Kiến trúc và cách Spark thực thi

- [Cluster overview](https://spark.apache.org/docs/3.5.7/cluster-overview.html)

## Ngày 04 — DataFrame và Spark SQL căn bản

- [DataFrame quickstart](https://spark.apache.org/docs/3.5.7/api/python/getting_started/quickstart_df.html)

## Ngày 05 — Làm sạch và khám phá dữ liệu

- [Spark SQL NULL semantics](https://spark.apache.org/docs/3.5.7/sql-ref-null-semantics.html)

## Ngày 06 — Join tổng hợp và window function

- [PySpark Window](https://spark.apache.org/docs/3.5.7/api/python/reference/pyspark.sql/api/pyspark.sql.Window.html)

## Ngày 07 — Đọc ghi và tổ chức lưu trữ

- [Parquet data source](https://spark.apache.org/docs/3.5.7/sql-data-sources-parquet.html)

## Ngày 08 — Partition shuffle và nền tảng RDD

- [RDD programming guide](https://spark.apache.org/docs/3.5.7/rdd-programming-guide.html)

## Ngày 09 — Tối ưu và xử lý lỗi hiệu năng

- [Spark SQL performance tuning](https://spark.apache.org/docs/3.5.7/sql-performance-tuning.html)

## Ngày 10 — Pipeline tăng dần và Structured Streaming

- [Structured Streaming guide](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html)

## Ngày 11 — Feature engineering và phòng tránh leakage

- [Common ML pitfalls](https://scikit-learn.org/1.5/common_pitfalls.html)
- [TimeSeriesSplit](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)

## Ngày 12 — Pipeline Machine Learning với Spark

- [Spark ML pipelines](https://spark.apache.org/docs/3.5.7/ml-pipeline.html)

## Ngày 13 — Đánh giá lựa chọn và tuning mô hình

- [Spark ML tuning](https://spark.apache.org/docs/3.5.7/ml-tuning.html)

## Ngày 14 — Kết hợp Spark với hệ sinh thái ML

- [scikit-learn Pipeline](https://scikit-learn.org/1.5/modules/compose.html)
- [PySpark pandas/Arrow integration](https://spark.apache.org/docs/3.5.7/api/python/user_guide/sql/arrow_pandas.html)

## Ngày 15 — Theo dõi thí nghiệm và quản lý mô hình

- [MLflow 2.22 tracking](https://mlflow.org/docs/2.22.0/tracking/)
- [MLflow model registry](https://mlflow.org/docs/2.22.0/model-registry.html)

## Ngày 16 — Cấu trúc project kiểm thử và chất lượng code

- [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)

## Ngày 17 — Lập lịch và điều phối pipeline

- [Airflow 3.0 core concepts](https://airflow.apache.org/docs/apache-airflow/3.0.0/core-concepts/index.html)

## Ngày 18 — Đóng gói và dự đoán hàng loạt

- [Docker get started](https://docs.docker.com/get-started/)
- [Spark submit](https://spark.apache.org/docs/3.5.7/submitting-applications.html)

## Ngày 19 — CI CD và nền tảng triển khai

- [Spark deployment overview](https://spark.apache.org/docs/3.5.7/cluster-overview.html)
- [GitHub Actions Python](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python)

## Ngày 20 — Giám sát drift và huấn luyện lại

- [MLflow tracking](https://mlflow.org/docs/2.22.0/tracking/)

## Ngày 21 — Backend và API cho hệ thống AI

- [FastAPI request body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI lifespan](https://fastapi.tiangolo.com/advanced/events/)

## Ngày 22 — PyTorch và nền tảng Transformer

- [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

## Ngày 23 — Model serving hiệu năng và độ tin cậy

- [FastAPI deployment](https://fastapi.tiangolo.com/deployment/)

## Ngày 24 — LLM prompting và đầu ra có cấu trúc

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)

## Ngày 25 — Chuẩn bị tài liệu và xây chỉ mục RAG

- [Sentence Transformers model card](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)
- [Qdrant local quickstart](https://qdrant.tech/documentation/quickstart/)

## Ngày 26 — Truy xuất hybrid search và reranking

- [Qdrant hybrid queries](https://qdrant.tech/documentation/search/hybrid-queries/)

## Ngày 27 — Đánh giá bảo mật và quan sát ứng dụng RAG

- [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

## Ngày 28 — Tool calling và workflow có tác nhân

- [OWASP GenAI security](https://genai.owasp.org/)

## Ngày 29 — Fine tuning và tối ưu mô hình nâng cao

- [Hugging Face LoRA](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)

## Ngày 30 — Dự án cuối khóa và chuẩn bị ứng tuyển

- [Spark guide](https://spark.apache.org/docs/3.5.7/)
- [MLflow guide](https://mlflow.org/docs/2.22.0/index.html)

