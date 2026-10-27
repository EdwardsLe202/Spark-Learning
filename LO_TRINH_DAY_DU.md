# Lộ trình đầy đủ 150 ngày học

[Bắt đầu từ số 0](BAT_DAU.md) · [Tiến độ](TIEN_DO.md) · [Đối chiếu tài liệu gốc](docs/DOI_CHIEU_LO_TRINH_GOC.md)

Mỗi số ngày là một buổi học theo thứ tự. Với 2–3 giờ/buổi, kế hoạch là khoảng **300–450 giờ**, có thể cần thêm buổi để sửa lỗi hoặc ôn. Phạm vi gồm Spark, ML, MLOps, API/PyTorch, LLM/RAG/tool workflow và portfolio. Không cần mở toàn bộ lịch ngay ngày 01.

Ngày 01–30 và bài làm/ghi chú của bạn được giữ nguyên. Các ngày 31–150 bổ sung nối tiếp, không yêu cầu học lại bản cũ trong tham_khao.

## Các chặng

| Ngày | Chặng | Đầu ra |
| --- | --- | --- |
| 01–30 | Nền Spark | Báo cáo đơn hàng nhỏ |
| 31–45 | Spark nâng cao | Plan/UI, RDD, tối ưu, lưu trữ |
| 46–60 | Incremental, streaming, feature | Dự án 1: dữ liệu và feature đúng thời điểm |
| 61–80 | ML và Spark ML | Model có split/metric/threshold/persistence |
| 81–105 | MLOps | Tracking, tests, DAG, container, release, monitoring |
| 106–120 | API/PyTorch/serving | Dự án 2: hệ ML có API và vận hành |
| 121–145 | LLM/RAG/tool workflow | Dự án 3: truy xuất, generation, eval và quyền |
| 146–150 | Fine-tuning mở rộng và portfolio | Quyết định kỹ thuật, clean run, demo |

Các lab local/Docker/Airflow phải chạy để nghiệm thu phần tương ứng. Cloud trả phí, GPU lớn và train LoRA là nhánh mở rộng khi đủ điều kiện; nếu chỉ thiết kế thì ghi rõ. Đủ ngày không tự đồng nghĩa thành thạo production hoặc có việc.

## Nền Spark — ngày 1–30

| Ngày | Bài |
| --- | --- |
| [01](day-01/README.md) | Đọc một bảng và hiểu Spark dùng để làm gì |
| [02](day-02/README.md) | Làm cùng bài toán bằng Python quen thuộc |
| [03](day-03/README.md) | Cài đúng môi trường trước khi viết Spark |
| [04](day-04/README.md) | Tạo bảng Spark đầu tiên |
| [05](day-05/README.md) | Tên cột và kiểu dữ liệu |
| [06](day-06/README.md) | Đọc file CSV tám đơn hàng |
| [07](day-07/README.md) | Chọn cột và đặt tên cho kết quả |
| [08](day-08/README.md) | Lọc các đơn cần tính |
| [09](day-09/README.md) | Tạo cột mới bằng withColumn |
| [10](day-10/README.md) | Tổng hợp tiền theo từng khách |
| [11](day-11/README.md) | Giá trị thiếu và cách lọc NULL |
| [12](day-12/README.md) | Nhận diện dòng trùng |
| [13](day-13/README.md) | Đọc số tiền sai kiểu và ghi lý do lỗi |
| [14](day-14/README.md) | Ôn tập lần một bằng báo cáo đơn hàng |
| [15](day-15/README.md) | Ngày tháng và khoảng thời gian |
| [16](day-16/README.md) | Lưu và đọc lại kết quả Parquet |
| [17](day-17/README.md) | Viết lại phép tính bằng Spark SQL |
| [18](day-18/README.md) | Ghép đơn hàng với thông tin khách |
| [19](day-19/README.md) | Giữ cả khách chưa có đơn |
| [20](day-20/README.md) | Phát hiện join làm nhân tiền |
| [21](day-21/README.md) | Chọn đơn mới nhất cho mỗi khách |
| [22](day-22/README.md) | Xem đơn trước và tổng tích lũy |
| [23](day-23/README.md) | Ghép các bước thành một lần làm sạch |
| [24](day-24/README.md) | Xử lý riêng một ngày dữ liệu |
| [25](day-25/README.md) | Chạy lại không làm nhân dữ liệu |
| [26](day-26/README.md) | Vì sao Spark chưa tính ngay? |
| [27](day-27/README.md) | Partition và chi phí shuffle |
| [28](day-28/README.md) | Đo một thay đổi hiệu năng đơn giản |
| [29](day-29/README.md) | Dự án nhỏ báo cáo doanh thu |
| [30](day-30/README.md) | Tự làm lại và quyết định học tiếp |

## Spark nâng cao — ngày 31–45

| Ngày | Bài |
| --- | --- |
| [31](day-31/README.md) | Driver và executor qua báo cáo đã biết |
| [32](day-32/README.md) | Theo dõi job stage task trong Spark UI |
| [33](day-33/README.md) | Logical plan và physical plan |
| [34](day-34/README.md) | RDD với word count nhỏ |
| [35](day-35/README.md) | Lineage broadcast và task retry |
| [36](day-36/README.md) | Repartition coalesce và file đầu ra |
| [37](day-37/README.md) | Nhận diện data skew spill và OOM |
| [38](day-38/README.md) | Broadcast join và sort merge join |
| [39](day-39/README.md) | AQE và đo kế hoạch sau thực thi |
| [40](day-40/README.md) | Built-in Python UDF và pandas UDF |
| [41](day-41/README.md) | JSON struct array map và explode |
| [42](day-42/README.md) | Partition pruning predicate pushdown và catalog |
| [43](day-43/README.md) | JDBC object storage và quyền truy cập |
| [44](day-44/README.md) | Delta Lake transaction và time travel |
| [45](day-45/README.md) | Ôn Spark nâng cao và báo cáo hiệu năng |

## Incremental, streaming và feature — ngày 46–60

| Ngày | Bài |
| --- | --- |
| [46](day-46/README.md) | Data interval và hai loại thời gian |
| [47](day-47/README.md) | Dedup và chọn phiên bản đã biết tại cutoff |
| [48](day-48/README.md) | Upsert bằng Delta merge |
| [49](day-49/README.md) | Backfill và thay đổi schema có kiểm soát |
| [50](day-50/README.md) | Structured Streaming từ file hữu hạn |
| [51](day-51/README.md) | Dừng và phục hồi bằng checkpoint |
| [52](day-52/README.md) | Event time khác processing time trong stream |
| [53](day-53/README.md) | Watermark và tiến độ thời gian sự kiện |
| [54](day-54/README.md) | Cửa sổ streaming và output mode |
| [55](day-55/README.md) | ForeachBatch và chống lặp tác động ghi |
| [56](day-56/README.md) | Định nghĩa entity cutoff và hai cửa sổ |
| [57](day-57/README.md) | Tạo feature 30 ngày bằng Spark |
| [58](day-58/README.md) | Tạo nhãn churn khi đủ quan sát |
| [59](day-59/README.md) | Chia tập thời gian và test chống leakage |
| [60](day-60/README.md) | Nghiệm thu dự án 1 dữ liệu và feature |

## Machine Learning và Spark ML — ngày 61–80

| Ngày | Bài |
| --- | --- |
| [61](day-61/README.md) | Từ bảng feature đến bài toán dự đoán |
| [62](day-62/README.md) | Baseline trước khi dùng model phức tạp |
| [63](day-63/README.md) | Confusion matrix precision recall |
| [64](day-64/README.md) | Xếp hạng bằng ROC AUC và PR AUC |
| [65](day-65/README.md) | Lắp pipeline scikit-learn |
| [66](day-66/README.md) | Fit preprocessing chỉ trên train |
| [67](day-67/README.md) | Estimator và Transformer trong Spark ML |
| [68](day-68/README.md) | Imputer scaler và vector đặc trưng |
| [69](day-69/README.md) | Category chưa gặp và one-hot encoding |
| [70](day-70/README.md) | Baseline Logistic Regression bằng Spark |
| [71](day-71/README.md) | Chọn thuật toán theo loại bài toán |
| [72](day-72/README.md) | Lưu và load toàn Spark PipelineModel |
| [73](day-73/README.md) | Threshold chi phí và calibration |
| [74](day-74/README.md) | Giới hạn số lần fit khi tuning |
| [75](day-75/README.md) | Đánh giá theo nhiều fold thời gian |
| [76](day-76/README.md) | Metric theo nhóm và độ bất định |
| [77](day-77/README.md) | Giới hạn trước khi toPandas |
| [78](day-78/README.md) | Artifact sklearn riêng cho API |
| [79](day-79/README.md) | Shard cho PyTorch và hai loại song song |
| [80](day-80/README.md) | Chốt model và model card |

## MLOps — ngày 81–105

| Ngày | Bài |
| --- | --- |
| [81](day-81/README.md) | Tách notebook thành module và CLI |
| [82](day-82/README.md) | Data contract và quality gate |
| [83](day-83/README.md) | Unit test và fixture với pytest |
| [84](day-84/README.md) | Integration test cho dữ liệu và model |
| [85](day-85/README.md) | Cấu hình log exception và exit code |
| [86](day-86/README.md) | MLflow experiment run và parameter |
| [87](day-87/README.md) | Ghi metric và artifact từ lần train thật |
| [88](day-88/README.md) | Model signature input example và dependency |
| [89](day-89/README.md) | Registry version và alias |
| [90](day-90/README.md) | Backend store artifact store và truy vết prediction |
| [91](day-91/README.md) | DAG và dependency của pipeline |
| [92](day-92/README.md) | Chạy Airflow TaskFlow trong môi trường riêng |
| [93](day-93/README.md) | Retry timeout và gate không được bỏ qua |
| [94](day-94/README.md) | Backfill Airflow data interval và giới hạn tài nguyên |
| [95](day-95/README.md) | Image container volume và kiến trúc máy |
| [96](day-96/README.md) | Build image và chạy batch từ môi trường sạch |
| [97](day-97/README.md) | Batch scoring Spark và prediction metadata |
| [98](day-98/README.md) | Compose readiness và dữ liệu bền vững |
| [99](day-99/README.md) | CI chạy test và tạo artifact |
| [100](day-100/README.md) | Chạy Spark Standalone với worker thật |
| [101](day-101/README.md) | Cloud object storage IAM và ngân sách |
| [102](day-102/README.md) | Release manifest promote và rollback |
| [103](day-103/README.md) | Giám sát schema missing và độ mới dữ liệu |
| [104](day-104/README.md) | Data drift concept drift và nhãn đến trễ |
| [105](day-105/README.md) | Chính sách retrain và nghiệm thu MLOps |

## API, PyTorch và model serving — ngày 106–120

| Ngày | Bài |
| --- | --- |
| [106](day-106/README.md) | HTTP JSON request và response |
| [107](day-107/README.md) | Pydantic kiểm tra kiểu miền giá trị và trường thừa |
| [108](day-108/README.md) | FastAPI route và mã lỗi |
| [109](day-109/README.md) | Lifespan load model health và readiness |
| [110](day-110/README.md) | Xác thực phân quyền và kiểm thử API |
| [111](day-111/README.md) | Sync async queue và công việc CPU |
| [112](day-112/README.md) | Tensor shape dtype và device |
| [113](day-113/README.md) | DataLoader forward loss backward optimizer |
| [114](day-114/README.md) | Train eval no_grad và checkpoint |
| [115](day-115/README.md) | Embedding attention và Transformer |
| [116](day-116/README.md) | Pretrained tokenizer và CPU MPS |
| [117](day-117/README.md) | Đo latency throughput và percentile |
| [118](day-118/README.md) | Batching worker cache và backpressure |
| [119](day-119/README.md) | Timeout retry canary và rollback dịch vụ |
| [120](day-120/README.md) | Nghiệm thu dự án 2 từ dữ liệu tới API |

## LLM, RAG và tool workflow — ngày 121–145

| Ngày | Bài |
| --- | --- |
| [121](day-121/README.md) | Token context window và giới hạn sinh |
| [122](day-122/README.md) | Prompt template few-shot và dữ liệu không tin cậy |
| [123](day-123/README.md) | Structured output và validation lỗi |
| [124](day-124/README.md) | Adapter model local và usage budget |
| [125](day-125/README.md) | Đánh giá prompt bằng tập cố định |
| [126](day-126/README.md) | RAG ingest tách khỏi luồng hỏi đáp |
| [127](day-127/README.md) | Parser chunk boundary size và overlap |
| [128](day-128/README.md) | ID content hash version và xóa tài liệu |
| [129](day-129/README.md) | Embedding thật normalization và model revision |
| [130](day-130/README.md) | Qdrant local upsert filter delete |
| [131](day-131/README.md) | Spark chuẩn bị corpus và embedding theo batch |
| [132](day-132/README.md) | Dense retrieval có lọc quyền |
| [133](day-133/README.md) | Sparse retrieval TF-IDF và mã chính xác |
| [134](day-134/README.md) | Hybrid search bằng RRF |
| [135](day-135/README.md) | Reranker chỉ sửa thứ hạng ứng viên |
| [136](day-136/README.md) | Recall MRR nDCG và tách dev test |
| [137](day-137/README.md) | Ghép context sinh trả lời và kiểm tra citation |
| [138](day-138/README.md) | Bộ 40 câu và đánh giá generation riêng |
| [139](day-139/README.md) | Trace request version usage và dữ liệu riêng tư |
| [140](day-140/README.md) | ACL trước retrieval và context |
| [141](day-141/README.md) | Prompt injection regression và lỗi dịch vụ |
| [142](day-142/README.md) | Tool schema và công cụ chỉ đọc |
| [143](day-143/README.md) | Dispatcher validation timeout và lỗi có thể retry |
| [144](day-144/README.md) | Workflow cố định và agent loop có budget |
| [145](day-145/README.md) | Nghiệm thu dự án 3 RAG có đánh giá |

## Fine-tuning mở rộng và portfolio — ngày 146–150

| Ngày | Bài |
| --- | --- |
| [146](day-146/README.md) | Quyết định fine-tune hay sửa retrieval |
| [147](day-147/README.md) | Dataset instruction và chống contamination |
| [148](day-148/README.md) | PEFT LoRA quantization và thí nghiệm tùy chọn |
| [149](day-149/README.md) | Clean run data dictionary model card và runbook |
| [150](day-150/README.md) | Nghiệm thu toàn lộ trình và demo portfolio |
