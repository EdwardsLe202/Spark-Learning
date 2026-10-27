# Nguồn học Spark

[Khóa nền](../README.md)

Bạn học bằng nội dung tiếng Việt của từng ngày trước. Các liên kết dưới dùng để kiểm chứng hoặc đọc thêm khi đã hiểu ví dụ, không phải danh sách phải đọc hết trước ngày 01.

- [PySpark 3.5.7 — cài đặt](https://spark.apache.org/docs/3.5.7/api/python/getting_started/install.html): bộ yêu cầu môi trường, dùng ở ngày 03.
- [PySpark 3.5.7 — DataFrame quickstart](https://spark.apache.org/docs/3.5.7/api/python/getting_started/quickstart_df.html): tạo bảng và các phép biến đổi cơ bản.
- [Spark SQL — NULL semantics](https://spark.apache.org/docs/3.5.7/sql-ref-null-semantics.html): giá trị thiếu, điều kiện lọc và tổng hợp, dùng ở ngày 11.
- [Spark SQL — CSV](https://spark.apache.org/docs/3.5.7/sql-data-sources-csv.html): header, schema và cách đọc file.
- [Spark SQL — Parquet](https://spark.apache.org/docs/3.5.7/sql-data-sources-parquet.html): đọc/ghi dữ liệu theo cột.
- [PySpark API reference](https://spark.apache.org/docs/3.5.7/api/python/reference/index.html): tra một hàm khi đã biết mình muốn làm gì.
- [Spark SQL performance tuning](https://spark.apache.org/docs/3.5.7/sql-performance-tuning.html): đọc sau ngày 26–28.

Khóa giữ PySpark 3.5.7, Python 3.11 và Java 17 để tránh mỗi ngày đổi API. Bộ dữ liệu, thứ tự bài, thời lượng, câu hỏi và tiêu chí là thiết kế học tập của repo, không phải một giáo trình chứng nhận chính thức.

Tài liệu gốc đầy đủ và nguồn về ML/MLOps/AI nằm trong [bản tham khảo](../tham_khao/lo_trinh_tong_hop/docs/NGUON_HOC.md). Chưa cần đọc chúng ở những ngày đầu.

## Nguồn cho ngày31–150

- [Delta compatibility](https://docs.delta.io/releases/) và [merge/upsert](https://docs.delta.io/latest/delta-update.html).
- [Structured Streaming3.5.7](https://spark.apache.org/docs/3.5.7/structured-streaming-programming-guide.html).
- [Spark ML pipelines](https://spark.apache.org/docs/3.5.7/ml-pipeline.html), [tuning](https://spark.apache.org/docs/3.5.7/ml-tuning.html), [Arrow](https://spark.apache.org/docs/3.5.7/api/python/user_guide/sql/arrow_pandas.html).
- [Sklearn1.5 common pitfalls](https://scikit-learn.org/1.5/common_pitfalls.html).
- [MLflow2.22 tracking](https://mlflow.org/docs/2.22.0/tracking/) và [registry](https://mlflow.org/docs/2.22.0/model-registry.html).
- [Airflow3 TaskFlow](https://airflow.apache.org/docs/apache-airflow/3.0.0/tutorial/taskflow.html).
- [Docker get started](https://docs.docker.com/get-started/) và [Spark submitting applications](https://spark.apache.org/docs/3.5.7/submitting-applications.html).
- [FastAPI body](https://fastapi.tiangolo.com/tutorial/body/) và [lifespan](https://fastapi.tiangolo.com/advanced/events/).
- [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html).
- [Embedding model card](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2), [generator model card](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct), [reranker model card](https://huggingface.co/cross-encoder/mmarco-mMiniLMv2-L12-H384-v1).
- [Qdrant local](https://qdrant.tech/documentation/quickstart/).
- [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/).
- [PEFT LoRA](https://huggingface.co/docs/peft/v0.15.0/package_reference/lora).

Những trang không gắn phiên bản có thể đổi. Ưu tiên API khớp requirements và ghi resolved revision cho model. Tài liệu/câu hỏi/rubric/thời lượng trong repo là thiết kế học tập, không phải cam kết chất lượng ứng dụng hay tuyển dụng.
