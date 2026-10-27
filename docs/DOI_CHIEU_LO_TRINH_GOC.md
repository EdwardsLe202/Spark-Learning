# Đối chiếu với 30 phần và 150 ý của lộ trình gốc

[Lịch150 ngày](../LO_TRINH_DAY_DU.md) · [Tài liệu gốc](../Lo_trinh_Spark_MLOps_AI_Engineering.docx)

Bảng dưới ánh xạ từng ý gốc sang ngày học mới. Một ý có thể trải qua nhiều buổi; tên ngày cũ trong bản lưu không có cùng nghĩa với ngày mới. Bảng chứng minh phạm vi được bố trí, không tự chứng nhận đã thực hành xong.

Cloud/GPU/fine-tuning lớn giữ là nhánh mở rộng; có bài thiết kế và lab tùy điều kiện. Core triển khai có môi trường Standalone local; Docker/Airflow/dense/generation thật cần được chạy để nghiệm thu phần tương ứng.

## Phần 01

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 01.1 | Spark và PySpark là gì; phân biệt bộ máy xử lý với nơi lưu dữ liệu. | [01](../day-01/README.md) |
| 01.2 | Xử lý song song và phân tán; batch và streaming qua ví dụ đơn hàng. | [31](../day-31/README.md) |
| 01.3 | So sánh pandas, SQL và Spark theo bộ nhớ, thời gian và độ phức tạp. | [77](../day-77/README.md) |
| 01.4 | Phân biệt pipeline dữ liệu, pipeline ML và quy trình MLOps. | [81](../day-81/README.md), [86](../day-86/README.md) |
| 01.5 | Hai hướng ML: Spark chuẩn bị dữ liệu cho thư viện khác hoặc dùng Spark MLlib. | [67](../day-67/README.md), [78](../day-78/README.md) |

## Phần 02

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 02.1 | Kiểm tra chip Intel hay Apple Silicon, RAM, dung lượng trống và kiến trúc terminal. | [95](../day-95/README.md) |
| 02.2 | Chọn bộ phiên bản Java, Python và PySpark tương thích theo tài liệu chính thức. | [03](../day-03/README.md) |
| 02.3 | Tạo môi trường Python riêng, ghi dependency và cấu hình JAVA_HOME khi cần. | [03](../day-03/README.md) |
| 02.4 | Tạo SparkSession, dùng notebook và file Python; dừng session đúng cách. | [04](../day-04/README.md) |
| 02.5 | Kiểm tra local mode, Spark UI, log và các lỗi khởi động thường gặp. | [32](../day-32/README.md) |

## Phần 03

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 03.1 | Driver, executor, worker và cluster manager; trách nhiệm từng thành phần. | [31](../day-31/README.md) |
| 03.2 | Partition là gì; task xử lý dữ liệu và mức song song. | [27](../day-27/README.md) |
| 03.3 | Transformation, action và lazy evaluation qua ví dụ đọc lọc nhóm. | [26](../day-26/README.md) |
| 03.4 | Application, job, stage và task; nhận biết nơi xuất hiện shuffle. | [32](../day-32/README.md) |
| 03.5 | SparkSession, Spark Classic và Spark Connect ở mức khái niệm; giới hạn của local mode. | [31](../day-31/README.md), [100](../day-100/README.md) |

## Phần 04

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 04.1 | Tạo DataFrame, StructType, StructField; tên cột và kiểu dữ liệu. | [05](../day-05/README.md) |
| 04.2 | select, alias, filter, withColumn, drop và biểu thức Column. | [07](../day-07/README.md) |
| 04.3 | cast, when, otherwise, hàm số học; phân biệt biểu thức cột với giá trị Python. | [09](../day-09/README.md), [13](../day-13/README.md) |
| 04.4 | Temp view và spark.sql; dùng SQL quen thuộc để kiểm tra kết quả. | [17](../day-17/README.md) |
| 04.5 | show, count, schema, explain; thứ tự dòng chỉ được xác định khi có sắp xếp phù hợp. | [04](../day-04/README.md), [33](../day-33/README.md) |

## Phần 05

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 05.1 | NULL, NaN, chuỗi rỗng và giá trị không hợp lệ; điều kiện ba trạng thái trong SQL. | [11](../day-11/README.md), [13](../day-13/README.md) |
| 05.2 | Duplicate theo cả dòng hoặc khóa nghiệp vụ; quy tắc giữ bản ghi. | [12](../day-12/README.md) |
| 05.3 | Xử lý chuỗi, ngày giờ, timezone và parse dữ liệu lỗi. | [15](../day-15/README.md) |
| 05.4 | Struct, array, map, JSON và explode; ảnh hưởng đến số dòng. | [41](../day-41/README.md) |
| 05.5 | Thống kê, tần suất, phân vị xấp xỉ, lấy mẫu để vẽ biểu đồ. | [37](../day-37/README.md), [77](../day-77/README.md) |

## Phần 06

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 06.1 | groupBy, agg, distinct và các phép tổng hợp điều kiện. | [10](../day-10/README.md) |
| 06.2 | Inner, left, full, semi và anti join; kiểm tra khóa và cardinality. | [18](../day-18/README.md) |
| 06.3 | Join làm nhân số dòng; cột trùng tên, NULL và khóa không khớp. | [20](../day-20/README.md) |
| 06.4 | Window partitionBy, orderBy, row_number, rank, lag và lead. | [21](../day-21/README.md) |
| 06.5 | rowsBetween và rangeBetween; cách xác định cửa sổ thời gian và xử lý giá trị bằng nhau. | [22](../day-22/README.md), [46](../day-46/README.md) |

## Phần 07

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 07.1 | CSV, JSON, Parquet; schema rõ ràng và chi phí đọc theo cột. | [06](../day-06/README.md), [16](../day-16/README.md) |
| 07.2 | Chế độ append, overwrite, error và ignore; kiểm tra đích trước khi ghi. | [16](../day-16/README.md), [25](../day-25/README.md), [42](../day-42/README.md) |
| 07.3 | Partition theo thư mục, partition pruning và predicate pushdown. | [42](../day-42/README.md) |
| 07.4 | JDBC, object storage, data lake; quyền truy cập và quản lý thông tin kết nối. | [43](../day-43/README.md) |
| 07.5 | Catalog, metadata, bảng và giới thiệu Delta Lake hoặc Iceberg cho transaction và lịch sử. | [42](../day-42/README.md), [44](../day-44/README.md) |

## Phần 08

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 08.1 | Partition trong thực thi khác với partition theo thư mục lưu trữ. | [36](../day-36/README.md) |
| 08.2 | Narrow và wide dependency; các thao tác thường tạo shuffle. | [27](../day-27/README.md) |
| 08.3 | repartition và coalesce; ảnh hưởng đến song song và kích thước đầu ra. | [36](../day-36/README.md) |
| 08.4 | RDD, map, filter, reduceByKey, lineage và khả năng tính lại dữ liệu. | [34](../day-34/README.md) |
| 08.5 | Broadcast variable, accumulator và rủi ro side effect khi task chạy lại. | [35](../day-35/README.md) |

## Phần 09

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 09.1 | explain, logical plan, physical plan; vai trò tối ưu truy vấn và AQE. | [33](../day-33/README.md) |
| 09.2 | Broadcast join, sort merge join; kích thước dữ liệu và điều kiện lựa chọn. | [38](../day-38/README.md) |
| 09.3 | Data skew, task chậm, spill và lỗi thiếu bộ nhớ ở driver hoặc executor. | [37](../day-37/README.md) |
| 09.4 | cache, persist, unpersist; chọn điểm tái sử dụng và đo lợi ích. | [28](../day-28/README.md), [45](../day-45/README.md) |
| 09.5 | Small files, số partition, built in function, Python UDF, pandas UDF và Arrow. | [40](../day-40/README.md) |

## Phần 10

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 10.1 | Batch theo data interval, incremental load và idempotency. | [46](../day-46/README.md) |
| 10.2 | Late data, dedup, upsert theo khả năng của storage và xử lý schema thay đổi. | [47](../day-47/README.md), [48](../day-48/README.md) |
| 10.3 | Backfill, retry, checkpoint dữ liệu và kiểm tra chất lượng tại mỗi bước. | [49](../day-49/README.md), [51](../day-51/README.md) |
| 10.4 | Structured Streaming, micro batch, source, sink và checkpointLocation. | [50](../day-50/README.md) |
| 10.5 | Event time, processing time, watermark, state và giới hạn bảo đảm xử lý. | [52](../day-52/README.md), [53](../day-53/README.md), [54](../day-54/README.md), [55](../day-55/README.md) |

## Phần 11

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 11.1 | Định nghĩa entity, thời điểm dự đoán, observation window và label window. | [56](../day-56/README.md) |
| 11.2 | Tạo nhãn churn cùng quy tắc xử lý khách hàng chưa đủ thời gian quan sát. | [58](../day-58/README.md) |
| 11.3 | Feature lịch sử, point in time join và dữ liệu được cập nhật muộn. | [57](../day-57/README.md) |
| 11.4 | Chia train, validation và test theo thời gian hoặc nhóm phù hợp bài toán. | [59](../day-59/README.md) |
| 11.5 | Fit imputer, scaler, encoder trên train; lưu feature schema và phiên bản dữ liệu. | [66](../day-66/README.md) |

## Phần 12

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 12.1 | Phân biệt Estimator, Transformer, Model và Pipeline trong pyspark.ml. | [67](../day-67/README.md) |
| 12.2 | Imputer, StringIndexer, OneHotEncoder, VectorAssembler và xử lý category chưa gặp. | [68](../day-68/README.md), [69](../day-69/README.md) |
| 12.3 | Scaling khi phù hợp thuật toán; vector đặc trưng thưa và đặc. | [68](../day-68/README.md) |
| 12.4 | Logistic regression, tree model, regression và clustering ở mức ứng dụng. | [70](../day-70/README.md), [71](../day-71/README.md) |
| 12.5 | fit, transform, save, load; giữ nhất quán tên cột, schema và preprocessing. | [72](../day-72/README.md) |

## Phần 13

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 13.1 | Baseline, class imbalance, confusion matrix, precision, recall, PR AUC và ROC AUC. | [62](../day-62/README.md), [63](../day-63/README.md), [64](../day-64/README.md) |
| 13.2 | Chọn threshold bằng validation và chi phí nghiệp vụ; hiệu chỉnh xác suất khi cần. | [73](../day-73/README.md) |
| 13.3 | CrossValidator, TrainValidationSplit và ParamGridBuilder. | [74](../day-74/README.md) |
| 13.4 | Validation theo thời gian bằng fold hoặc vòng lặp phù hợp; tránh dùng mặc định sai bài toán. | [75](../day-75/README.md) |
| 13.5 | Đánh giá theo nhóm, khoảng bất định và chốt test sau khi quyết định mô hình. | [76](../day-76/README.md) |

## Phần 14

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 14.1 | Spark MLlib và scikit learn giải quyết các phạm vi khác nhau. | [77](../day-77/README.md) |
| 14.2 | Sampling, aggregation và ước lượng bộ nhớ trước khi chuyển sang pandas. | [77](../day-77/README.md) |
| 14.3 | pandas API on Spark, pandas UDF và mapInPandas ở mức sử dụng có mục đích. | [40](../day-40/README.md), [77](../day-77/README.md) |
| 14.4 | Spark chuẩn bị dữ liệu cho PyTorch; định dạng, shard và hợp đồng dữ liệu. | [79](../day-79/README.md) |
| 14.5 | Phân biệt huấn luyện phân tán một mô hình với chạy nhiều thí nghiệm độc lập. | [79](../day-79/README.md) |

## Phần 15

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 15.1 | MLflow experiment, run, parameter, metric, tag và artifact. | [86](../day-86/README.md) |
| 15.2 | Ghi thông tin pipeline Spark và mô hình từ thư viện khác; hiểu giới hạn autolog. | [87](../day-87/README.md) |
| 15.3 | Lưu model signature, input example, dependency và metadata dữ liệu. | [88](../day-88/README.md) |
| 15.4 | Registry, version, alias; chọn model candidate theo điều kiện đánh giá. | [89](../day-89/README.md) |
| 15.5 | Backend store, artifact store, local server và nguyên tắc quản lý quyền truy cập. | [90](../day-90/README.md) |

## Phần 16

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 16.1 | Git, nhánh, commit, package, CLI và tách logic khỏi thao tác đọc ghi. | [81](../day-81/README.md) |
| 16.2 | Cấu hình theo môi trường, logging, exception và mã thoát. | [85](../day-85/README.md) |
| 16.3 | Unit test cho feature; integration test cho đọc ghi, train và predict. | [83](../day-83/README.md) |
| 16.4 | Kiểm tra schema, unique key, NULL, timestamp, leakage và data contract. | [84](../day-84/README.md) |
| 16.5 | Kiểm tra dependency, lint, kiểm thử nhanh trước khi chạy pipeline lớn. | [82](../day-82/README.md) |

## Phần 17

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 17.1 | DAG, task, dependency, data interval và lịch chạy trong Airflow. | [91](../day-91/README.md) |
| 17.2 | Tách ingest, validate, features, train, evaluate, register và score. | [92](../day-92/README.md) |
| 17.3 | Retry, timeout, backfill, idempotency và checkpoint theo bước. | [93](../day-93/README.md) |
| 17.4 | Điều kiện dừng khi dữ liệu lỗi hoặc model không đạt; truyền metadata thay vì dữ liệu lớn. | [94](../day-94/README.md) |
| 17.5 | Theo dõi trạng thái, thông báo lỗi, hạn chế tài nguyên và tránh chạy chồng ngoài ý muốn. | [94](../day-94/README.md) |

## Phần 18

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 18.1 | Docker image, container, network, volume và kiến trúc ARM hoặc x86. | [95](../day-95/README.md) |
| 18.2 | Dockerfile, dependency cố định, model artifact và cấu hình ngoài image. | [96](../day-96/README.md) |
| 18.3 | spark submit, batch scoring và ghi prediction cùng entity, thời gian, model version. | [97](../day-97/README.md) |
| 18.4 | So sánh batch inference với online inference; tái sử dụng preprocessing. | [78](../day-78/README.md) |
| 18.5 | Docker Compose cho mô hình học tập; health check và lưu dữ liệu bền vững. | [98](../day-98/README.md) |

## Phần 19

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 19.1 | Local, development, staging và production; client mode và cluster mode. | [100](../day-100/README.md) |
| 19.2 | Spark Standalone, YARN, Kubernetes; chọn một môi trường để thực hành triển khai. | [100](../day-100/README.md) |
| 19.3 | Object storage, IAM, service account, network và secret management. | [101](../day-101/README.md) |
| 19.4 | CI cho test và build; CD cho phát hành có kiểm tra và rollback. | [99](../day-99/README.md) |
| 19.5 | Version image, model, dữ liệu, cấu hình; resource limit, quota và dự toán chi phí. | [102](../day-102/README.md) |

## Phần 20

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 20.1 | Log, metric, trace; theo dõi runtime, lỗi, độ trễ và tài nguyên. | [103](../day-103/README.md) |
| 20.2 | Schema drift, missing rate, phân bố feature, prediction drift và data freshness. | [103](../day-103/README.md) |
| 20.3 | Data drift, concept drift và hiệu năng khi có nhãn; nhãn đến trễ. | [104](../day-104/README.md) |
| 20.4 | Ngưỡng cảnh báo, điều tra lỗi và phân tích theo nhóm khách hàng. | [104](../day-104/README.md) |
| 20.5 | Chính sách retrain, đánh giá candidate, rollout và rollback; lưu lịch sử quyết định. | [105](../day-105/README.md) |

## Phần 21

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 21.1 | HTTP, request, response, status code, JSON và API contract. | [106](../day-106/README.md) |
| 21.2 | FastAPI, validation, schema, dependency và cấu hình dịch vụ. | [107](../day-107/README.md) |
| 21.3 | Load model khi khởi động, endpoint predict, health và readiness. | [109](../day-109/README.md) |
| 21.4 | Authentication, authorization, rate limit, timeout và giới hạn payload. | [110](../day-110/README.md) |
| 21.5 | Sync, async, queue và công việc nền; phân biệt tác vụ IO với tác vụ CPU hoặc GPU. | [111](../day-111/README.md) |

## Phần 22

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 22.1 | Tensor, shape, dtype, device và thao tác cơ bản. | [112](../day-112/README.md) |
| 22.2 | Dataset, DataLoader, batch, forward, loss, backward và optimizer. | [113](../day-113/README.md) |
| 22.3 | Train, eval, no grad, overfitting, checkpoint và lưu load trọng số. | [114](../day-114/README.md) |
| 22.4 | Embedding, attention, Transformer và pretrained model ở mức ứng dụng. | [115](../day-115/README.md) |
| 22.5 | CPU, GPU, Apple MPS khi được hỗ trợ; bộ nhớ, batch size và giới hạn phần cứng. | [116](../day-116/README.md) |

## Phần 23

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 23.1 | Latency, throughput, concurrency và p50, p95, p99. | [117](../day-117/README.md) |
| 23.2 | Model warm up, batching, worker, queue và giới hạn tài nguyên. | [118](../day-118/README.md) |
| 23.3 | Cache có khóa đúng, timeout, retry có giới hạn và backpressure. | [118](../day-118/README.md), [119](../day-119/README.md) |
| 23.4 | Version endpoint, canary hoặc shadow theo nhu cầu; rollback. | [119](../day-119/README.md) |
| 23.5 | Load test, kiểm tra độ tương đương và phân tích điểm nghẽn. | [120](../day-120/README.md) |

## Phần 24

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 24.1 | Token, context window, sinh văn bản, tham số lấy mẫu và giới hạn đầu ra. | [121](../day-121/README.md) |
| 24.2 | System instruction, prompt template, few shot và tách dữ liệu khỏi chỉ dẫn. | [122](../day-122/README.md) |
| 24.3 | Structured output, schema validation, retry có giới hạn và xử lý từ chối hoặc lỗi. | [123](../day-123/README.md) |
| 24.4 | Embedding, similarity; phân biệt prompting, RAG và fine tuning. | [124](../day-124/README.md), [129](../day-129/README.md) |
| 24.5 | Chi phí, rate limit, timeout; tạo tập ví dụ để so sánh prompt. | [125](../day-125/README.md) |

## Phần 25

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 25.1 | RAG gồm ingest, chunk, embed, index, retrieve và generate. | [126](../day-126/README.md) |
| 25.2 | Trích xuất văn bản, chất lượng parser, chunk size, overlap và ranh giới nội dung. | [127](../day-127/README.md) |
| 25.3 | Document ID, chunk ID, content hash, nguồn, phiên bản và quyền truy cập. | [128](../day-128/README.md) |
| 25.4 | Spark làm sạch và dedup hàng loạt; embedding job có batching, rate limit và retry. | [131](../day-131/README.md) |
| 25.5 | Vector store, upsert, xóa tài liệu, reindex và thay embedding model. | [130](../day-130/README.md) |

## Phần 26

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 26.1 | Dense retrieval, sparse retrieval, keyword search và hybrid search. | [132](../day-132/README.md), [133](../day-133/README.md), [134](../day-134/README.md) |
| 26.2 | Top k, metadata filter, phân quyền truy xuất và các truy vấn theo phiên bản. | [140](../day-140/README.md) |
| 26.3 | Reranker, lựa chọn context và ảnh hưởng đến độ trễ. | [135](../day-135/README.md) |
| 26.4 | Recall at k, MRR, nDCG và mức độ đầy đủ của nhãn relevance. | [136](../day-136/README.md) |
| 26.5 | Phân tích lỗi do parser, chunk, embedding, retrieval và ranking. | [136](../day-136/README.md) |

## Phần 27

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 27.1 | Bộ đánh giá gồm câu hỏi trả lời được, thiếu bằng chứng, mơ hồ và ngoài phạm vi. | [138](../day-138/README.md) |
| 27.2 | Correctness, groundedness, citation, abstention; tách metric retrieval với generation. | [137](../day-137/README.md) |
| 27.3 | Trace theo request, phiên bản prompt, model, index, token, latency và chi phí. | [139](../day-139/README.md) |
| 27.4 | Prompt injection từ tài liệu, rò rỉ dữ liệu, quyền truy cập và xử lý nội dung không tin cậy. | [141](../day-141/README.md) |
| 27.5 | Regression test, đánh giá thủ công và giới hạn của LLM judge. | [141](../day-141/README.md) |

## Phần 28

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 28.1 | Tool calling, schema công cụ, workflow cố định và agent loop. | [142](../day-142/README.md) |
| 28.2 | Kiểm tra tham số, xử lý lỗi, timeout và phân loại lỗi có thể retry. | [143](../day-143/README.md) |
| 28.3 | Giới hạn số bước, token, thời gian và chi phí; điều kiện dừng. | [144](../day-144/README.md) |
| 28.4 | Công cụ chỉ đọc, quyền tối thiểu và xác nhận cho hành động ảnh hưởng dữ liệu. | [140](../day-140/README.md) |
| 28.5 | Đánh giá thành công của tác vụ, trace và kiểm thử tình huống công cụ trả dữ liệu xấu. | [145](../day-145/README.md) |

## Phần 29

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 29.1 | Chọn giữa cải thiện dữ liệu, prompt, retrieval và fine tuning. | [146](../day-146/README.md) |
| 29.2 | Dataset hướng dẫn, quyền sử dụng, dedup, train validation test và contamination. | [147](../day-147/README.md) |
| 29.3 | Full fine tuning, PEFT, LoRA và quantization ở mức khái niệm. | [148](../day-148/README.md) |
| 29.4 | Chi phí train, checkpoint, metric và so sánh với baseline giữ nguyên. | [148](../day-148/README.md) |
| 29.5 | Distillation, distributed training và inference engine ở mức định hướng học tiếp. | [148](../day-148/README.md) |

## Phần 30

| Ý gốc | Nội dung | Ngày mới |
| --- | --- | --- |
| 30.1 | Chốt yêu cầu, dữ liệu, metric, giới hạn tài nguyên và tiêu chí nghiệm thu. | [149](../day-149/README.md) |
| 30.2 | Hoàn thiện ba mốc dự án dữ liệu, ML vận hành và ứng dụng RAG. | [60](../day-60/README.md), [120](../day-120/README.md), [145](../day-145/README.md) |
| 30.3 | Tạo README, sơ đồ, data dictionary, model card và runbook. | [149](../day-149/README.md) |
| 30.4 | Demo khởi động sạch, lỗi có chủ ý, phục hồi và rollback. | [150](../day-150/README.md) |
| 30.5 | Ôn SQL, PySpark, ML, MLOps, API, RAG và phỏng vấn thiết kế hệ thống. | [150](../day-150/README.md) |
