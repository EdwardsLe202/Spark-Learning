# Thuật ngữ để tra khi học

[Khóa nền](../README.md)

**Không học thuộc cả bảng trước ngày 01.** Mỗi bài chỉ yêu cầu nhận ra những từ đã dùng trong ví dụ. Tên hàm giữ tiếng Anh để bạn viết code đúng; phần sau giải thích bằng tiếng Việt.

| English term | Nghĩa trong khóa học |
| --- | --- |
| Action | thao tác yêu cầu kết quả |
| Aggregation | tổng hợp nhiều dòng |
| AI — Artificial Intelligence | Trí tuệ nhân tạo; các ứng dụng model/LLM học ở chặng nối tiếp. |
| Alias | tên thay thế trong kết quả |
| amount | Số tiền, dùng đơn vị đồng Việt Nam trong dữ liệu của khóa. |
| Apache Spark | bộ máy xử lý dữ liệu |
| API — Application Programming Interface | Giao diện cho chương trình tương tác; trong DataFrame API là tập phương thức thao tác bảng. |
| assert | Lệnh Python báo lỗi nếu điều kiện kiểm tra sai. |
| Backfill | xử lý bù dữ liệu quá khứ |
| Baseline | mốc so sánh ban đầu |
| Batch processing | xử lý một tập dữ liệu hữu hạn theo đợt |
| Cache | giữ kết quả để tái dùng |
| Cardinality | quan hệ số lượng giữa các khóa |
| Cast | chuyển kiểu dữ liệu |
| Column | cột dữ liệu |
| Column expression | biểu thức tính trên cột |
| completed / cancelled | Trạng thái hoàn tất / đã hủy của đơn. |
| Condition | điều kiện giữ dòng |
| CSV — Comma-Separated Values | tệp văn bản có các trường phân cách bằng dấu phẩy |
| customer_id | Mã khách hàng; một khách có thể có nhiều đơn. |
| Data interval | khoảng dữ liệu được một lần chạy xử lý |
| DataFrame | bảng dữ liệu có cấu trúc |
| Date | kiểu ngày lịch |
| Deliverable | sản phẩm bàn giao có thể kiểm tra |
| Dependency | thư viện chương trình cần |
| Distinct | giữ các dòng khác nhau |
| Driver / Executor | Thành phần điều phối / thành phần thực thi trong kiến trúc Spark, đọc sâu sau nền. |
| Duplicate | bản ghi trùng theo quy tắc |
| Execution plan | Kế hoạch Spark dùng để thực hiện yêu cầu. |
| F.col | Hàm tạo biểu thức cột từ tên; cùng vai trò tham chiếu cột như df["amount"]. |
| F.lit | Hàm đưa giá trị cố định vào biểu thức Spark. |
| fillna | điền giá trị thiếu theo quy tắc |
| Filter | lọc dòng |
| Group | nhóm theo khóa |
| Header | dòng tên cột |
| Idempotency | tính lũy đẳng khi chạy lại |
| Inclusive / Exclusive | bao gồm / loại trừ mốc biên |
| Inner join | chỉ giữ các khóa khớp hai phía |
| isNull | kiểm tra giá trị thiếu |
| Join | ghép bảng theo điều kiện |
| Key | khóa nhận diện bản ghi |
| Lag | lấy giá trị của dòng trước |
| Lazy evaluation | thực thi trì hoãn |
| Left anti join | giữ dòng trái không có khóa khớp |
| Left join | ghép giữ mọi dòng phía trái |
| Long | kiểu số nguyên 64 bit |
| Machine Learning | Học máy; cần học feature, nhãn và đánh giá trước khi dùng pipeline model. |
| MLOps | Vận hành vòng đời mô hình học máy, thuộc chặng học sau nền Spark. |
| NULL | giá trị thiếu hoặc chưa biết |
| order_id | Mã đơn hàng; một đơn có một mã trong dữ liệu chuẩn. |
| Overwrite | ghi thay thế dữ liệu ở đích |
| Parquet | định dạng lưu dữ liệu theo cột |
| Parse | diễn giải văn bản thành kiểu mong muốn |
| Partition | phần dữ liệu để xử lý song song |
| Path | đường dẫn tệp |
| Pipeline | chuỗi bước xử lý có đầu vào và đầu ra |
| PySpark | giao diện Python của Spark |
| Quarantine | vùng giữ bản ghi lỗi để điều tra |
| Reconciliation | đối soát các số liệu liên quan |
| Record | một bản ghi |
| Repartition | chia lại dữ liệu thành các partition |
| Row | dòng dữ liệu |
| row_number | số thứ tự duy nhất trong nhóm |
| Running total | tổng tích lũy đến dòng hiện tại |
| Schema | lược đồ tên cột và kiểu |
| Select | chọn cột |
| Self-assessment | tự đánh giá bằng hành vi và kết quả |
| Shuffle | phân phối lại dữ liệu giữa các phần xử lý |
| Spark SQL | Cách truy vấn dữ liệu Spark bằng ngôn ngữ SQL. |
| SparkSession | phiên làm việc với Spark |
| String | kiểu chuỗi văn bản |
| String / Long | Chuỗi văn bản / số nguyên 64 bit, ví dụ mã đơn và số tiền. |
| Table | Bảng dữ liệu gồm các dòng và cột. |
| Temporary view | bảng nhìn tạm trong phiên |
| Terminal | cửa sổ chạy lệnh |
| Transformation | phép tạo kế hoạch biến đổi |
| Union | Nối các dòng từ các bảng cùng cấu trúc; không tự khử trùng. |
| Unique key | khóa có giá trị duy nhất |
| Validation | kiểm tra dữ liệu theo quy tắc |
| Virtual environment | môi trường Python riêng |
| Warm-up | lượt khởi động trước khi đo |
| Window frame | phạm vi dòng đưa vào phép tính |
| Window function | hàm tính trên nhóm dòng liên quan |
| withColumn | tạo hoặc thay cột trong bảng kết quả |

Từ vựng ML/MLOps/AI đầy đủ hơn nằm ở [bản cũ](../tham_khao/lo_trinh_tong_hop/docs/THUAT_NGU.md); chỉ đọc khi sang chặng tương ứng.

## Tra theo các chặng nâng cao, chỉ đọc khi gặp

| English term | Nghĩa tiếng Việt |
| --- | --- |
| Abstention | từ chối khi thiếu bằng chứng |
| Acceptance test | kiểm tra nghiệm thu |
| ACID transaction | giao dịch bảo đảm tính nhất quán |
| ACL — Access Control List | danh sách quyền |
| Adapter | lớp giao tiếp tách model/provider |
| Agent loop | vòng model chọn bước tiếp |
| Alias | bí danh có thể đổi |
| Allowlist | danh sách được phép |
| Answerability | khả năng trả lời bằng nguồn |
| API contract | hợp đồng giao tiếp |
| Append / Update / Complete | ghi dòng hoàn tất / cập nhật / toàn kết quả |
| AQE — Adaptive Query Execution | điều chỉnh kế hoạch khi chạy |
| Array | mảng phần tử |
| Arrow | định dạng trao đổi dữ liệu theo cột |
| Artifact | đầu ra lưu kèm run |
| Artifact store | kho tệp đầu ra |
| Atomic replace | thay con trỏ nguyên tử trên filesystem |
| Attention | kết hợp thông tin theo mức liên quan |
| Authentication | xác thực danh tính |
| Authorization | kiểm tra quyền |
| Authorization filter | bộ lọc theo quyền |
| Autograd | cơ chế tự tính gradient |
| Autologging | ghi thí nghiệm tự động |
| Average precision | trung bình precision theo thứ hạng |
| Backend store | kho metadata |
| Backpressure | hạn chế nhận việc khi quá tải |
| Baseline | mốc dự đoán đơn giản |
| Baseline comparison | so với mốc ban đầu |
| Batch embedding | tính vector theo lô |
| Batch ID | mã lô trong một query |
| Batch inference | dự đoán theo lô |
| Batching | gom nhiều mẫu |
| Benchmark | thử nghiệm đo có điều kiện |
| BM25 | xếp hạng từ vựng |
| Broadcast join | ghép bằng phát bảng nhỏ |
| Broadcast variable | biến chỉ đọc phân phối tới task |
| Build artifact | sản phẩm build có định danh |
| Build context | tập tệp gửi cho builder |
| Built-in function | hàm Spark có sẵn |
| Calibration | hiệu chỉnh độ phù hợp xác suất |
| Canary release | phát hành cho phần nhỏ lưu lượng |
| Candidate gate | điều kiện chấp nhận model ứng viên |
| Catalog | danh mục quản lý bảng |
| Catalyst | bộ tối ưu truy vấn Spark SQL |
| Catchup | tạo bù các kỳ chưa chạy |
| Censoring | chưa quan sát đủ kết quả |
| Checkpoint | bản lưu trạng thái model |
| Chunk | đoạn để truy xuất |
| Churn | không hoạt động theo định nghĩa |
| CI — Continuous Integration | kiểm tra khi tích hợp code |
| Citation | trích dẫn nguồn |
| Class imbalance | mất cân bằng lớp |
| Classification | phân loại |
| CLI — Command Line Interface | giao diện dòng lệnh |
| Client / Cluster mode | driver phía gửi / trong cụm |
| Clustering | gom nhóm không có nhãn |
| Coalesce | gộp giảm partition |
| Code reference | định danh code của lần chạy |
| ColumnTransformer | xử lý các nhóm cột |
| Compatibility | tính tương thích |
| Compose | cấu hình các dịch vụ container |
| Concept drift | thay đổi quan hệ đầu vào và mục tiêu |
| Confidence interval | khoảng bất định ước lượng |
| Confusion matrix | ma trận nhầm lẫn |
| Container | tiến trình từ image |
| Contamination | nhiễm dữ liệu test vào train |
| Content hash | mã băm nội dung |
| Context window | giới hạn ngữ cảnh |
| Correctness | độ đúng nội dung |
| Cosine similarity | độ gần theo góc vector |
| CPU-bound / IO-bound | nặng tính toán / chờ vào ra |
| Cross-encoder | model xem query và đoạn cùng nhau |
| Cutoff | mốc chốt thông tin |
| DAG — Directed Acyclic Graph | đồ thị có hướng không chu trình |
| Data contract | hợp đồng dữ liệu |
| Data drift | thay đổi phân bố đầu vào |
| Data freshness | độ mới dữ liệu |
| Data lineage | nguồn gốc các bước tạo dữ liệu |
| Data rights | quyền sử dụng dữ liệu |
| Data skew | dữ liệu lệch khóa |
| DataLoader | bộ đọc theo lô |
| Deadline | hạn thời gian toàn yêu cầu |
| Decision tree | cây quyết định |
| Delayed labels | nhãn đến trễ |
| Dense retrieval | tìm bằng vector đặc |
| Dependency | quan hệ bước cần chạy trước |
| Dependency environment | môi trường thư viện |
| Device | thiết bị chứa và tính dữ liệu |
| Dispatcher | bộ chọn và gọi công cụ |
| Distributed training | huấn luyện phân tán một model |
| Dockerfile | tệp mô tả build image |
| Document ID / Chunk ID | mã tài liệu / đoạn |
| Driver | tiến trình điều phối |
| Embedding | biểu diễn ngữ nghĩa bằng vector |
| End-to-end evaluation | đánh giá toàn luồng |
| Endpoint | đường dẫn chức năng |
| Entity | đối tượng dự đoán |
| Equivalence | tính tương đương kết quả |
| Estimator | thành phần cần fit |
| Event time | thời gian sự kiện xảy ra |
| Exception | ngoại lệ |
| Executor | tiến trình thực thi |
| Exit code | mã kết thúc |
| Experiment | nhóm thí nghiệm |
| Explode | tách phần tử mảng thành dòng |
| Fail closed | từ chối khi kiểm tra quyền không thành công |
| Failure propagation | truyền trạng thái thất bại |
| FastAPI | framework API Python |
| Feature | biến đầu vào |
| Feature engineering | tạo đặc trưng từ dữ liệu |
| Few-shot | ví dụ trong ngữ cảnh |
| Field accuracy | tỷ lệ trường trích đúng |
| Fine-tuning | điều chỉnh tham số bằng dữ liệu |
| Finite number | số hữu hạn |
| Fit / Transform | học quy tắc / áp dụng quy tắc |
| Fixture | dữ liệu hoặc thiết lập dùng cho test |
| foreachBatch | xử lý từng micro-batch bằng hàm |
| Gap | khoảng cách để tránh cửa sổ chồng |
| Gradient | đạo hàm dùng cập nhật trọng số |
| Groundedness | mức câu được bằng chứng hỗ trợ |
| Group split | chia theo nhóm đối tượng |
| Health | tiến trình còn sống |
| Healthcheck | kiểm tra trạng thái dịch vụ |
| Holdout | tập giữ riêng để chấm cuối |
| HTTP | giao thức yêu cầu và phản hồi |
| HTTPException | phản hồi lỗi có trạng thái |
| Hybrid search | kết hợp nhiều cách tìm |
| Hyperparameter | siêu tham số |
| IAM — Identity and Access Management | quản lý danh tính và quyền |
| Idempotency key | khóa chống lặp |
| Image | mẫu môi trường |
| Imputer | bộ điền thiếu |
| Index rollback | quay về chỉ mục trước |
| Ingestion | đưa tài liệu vào hệ thống |
| Ingestion time | thời gian dữ liệu được nhận |
| Input contract | hợp đồng đầu vào |
| Input example | mẫu đầu vào |
| Instruction / Data | chỉ dẫn / dữ liệu |
| Instruction dataset | tập ví dụ hướng dẫn |
| Integration test | kiểm thử các thành phần kết hợp |
| JDBC — Java Database Connectivity | giao diện kết nối database |
| Job | công việc thực thi |
| Label / Target | nhãn mục tiêu |
| Label window | cửa sổ tương lai xác định nhãn |
| Late data | dữ liệu đến muộn |
| Latency | độ trễ mỗi request |
| Leakage | rò rỉ thông tin vào học máy |
| Lifespan | vòng đời ứng dụng |
| Lineage | quan hệ nguồn gốc phép tính |
| LLM judge | model dùng để chấm |
| Logical date | mốc logic của lần chạy |
| Logical plan | kế hoạch logic |
| Logistic regression | hồi quy logistic cho phân loại |
| LoRA — Low Rank Adaptation | điều chỉnh bằng ma trận hạng thấp |
| Loss | hàm đo sai lệch |
| Memory budget | ngân sách bộ nhớ |
| Merge | ghép thay đổi vào bảng theo khóa |
| Metric | chỉ số đo |
| Micro-batch | lô nhỏ liên tiếp |
| Missing rate | tỷ lệ thiếu |
| Model | kết quả đã fit |
| Model card | mô tả mục đích và giới hạn |
| Model registry | sổ quản lý model |
| Model signature | mô tả kiểu đầu vào/đầu ra |
| Module | đơn vị mã nguồn |
| MPS | backend tính toán cho thiết bị Apple |
| MRR | nghịch đảo hạng đúng đầu tiên trung bình |
| nDCG | chất lượng thứ hạng có chuẩn hóa |
| Normalization | chuẩn hóa vector |
| Object storage | kho lưu đối tượng |
| Offset | vị trí tiến độ của nguồn |
| One-hot encoding | mã hóa nhóm bằng vector chỉ báo |
| Online inference | dự đoán theo yêu cầu |
| Online path | luồng trả lời yêu cầu |
| OOM — Out of memory | hết bộ nhớ |
| Overlap | phần giao giữa các đoạn |
| p95 | phân vị độ trễ 95 phần trăm |
| Parallel experiments | nhiều thí nghiệm độc lập |
| Parameter | tham số cấu hình |
| Parameter grid | lưới cấu hình |
| Parametrization | chạy cùng test với nhiều ca |
| Parser quality | chất lượng trích xuất nguồn |
| Partition pruning | bỏ qua thư mục phân vùng |
| Payload | metadata kèm vector |
| PEFT | fine-tuning ít tham số |
| Persistence | lưu trạng thái để dùng lại |
| Physical plan | kế hoạch vật lý |
| PII — Personally Identifiable Information | thông tin nhận diện cá nhân |
| Pipeline | chuỗi bước fit và transform |
| Point-in-time selection | chọn phiên bản đã có ở mốc chốt |
| Pool | nhóm giới hạn số task |
| Portfolio | bộ dự án minh chứng |
| Precision | tỷ lệ đúng trong dự đoán dương |
| Predicate pushdown | đẩy điều kiện xuống bộ đọc |
| Prediction key | khóa của bản dự đoán |
| Prediction lineage | nguồn gốc dự đoán |
| Preprocessing | tiền xử lý |
| Pretrained model | model đã học trước |
| Probability | xác suất model ước lượng |
| Processing time | thời gian hệ thống xử lý |
| Prompt injection | nội dung không tin cậy chèn chỉ dẫn |
| Prompt template | mẫu lời nhắc |
| Pydantic | thư viện kiểm tra dữ liệu |
| Quality gate | điều kiện chất lượng để đi tiếp |
| Quantization | lượng tử hóa số |
| Queue | hàng đợi |
| Quota | hạn mức tài nguyên |
| RAG — Retrieval-Augmented Generation | sinh câu trả lời có truy xuất |
| Rate limit | giới hạn tần suất |
| RDD — Resilient Distributed Dataset | tập dữ liệu phân tán có thể tính lại |
| Read-only | chỉ đọc |
| Readiness | sẵn sàng phục vụ |
| Recall | tỷ lệ tìm được mẫu dương |
| Recall@k | tỷ lệ tài liệu liên quan tìm được |
| Recency | số ngày từ lần hoạt động gần nhất |
| reduceByKey | tổng hợp giá trị theo khóa |
| Refusal / Error | từ chối / lỗi |
| Regression | dự đoán số |
| Regression test | kiểm thử lỗi quay lại |
| Reindex | tạo lại chỉ mục |
| Release manifest | bản ghi thành phần phát hành |
| Reproducibility | khả năng tái lập |
| Request ID | mã nối các sự kiện |
| Reranker | model chấm lại ứng viên |
| Retraining | huấn luyện lại |
| Retry budget | giới hạn thử lại |
| Retry policy | chính sách thử lại |
| Retryable error | lỗi có thể thử lại |
| ROC AUC | diện tích dưới đường ROC |
| Rollback | quay về phiên bản trước |
| Root cause | nguyên nhân gốc |
| RRF — Reciprocal Rank Fusion | hợp nhất theo nghịch đảo thứ hạng |
| Rubric | bảng tiêu chí chấm |
| Run | một lần thực thi |
| Runbook | cách vận hành phục hồi |
| Sampling | cách chọn token kế tiếp |
| Scaling | chuẩn hóa thang đo |
| Scheduler | bộ lập lịch thực thi |
| Schema drift | thay đổi lược đồ |
| Schema evolution | thay đổi lược đồ |
| Schema pass rate | tỷ lệ đầu ra đạt schema |
| Schema validation | kiểm tra theo lược đồ |
| Secret | thông tin bí mật cần bảo vệ |
| Service account | danh tính ứng dụng |
| Service level objective — SLO | mục tiêu mức phục vụ |
| Shadow traffic | chạy quan sát song song |
| Shape | kích thước các chiều |
| Shard | phần dữ liệu chia sẵn |
| Side effect | tác động ra hệ thống ngoài |
| Slice evaluation | đánh giá theo nhóm |
| Small files | nhiều tệp nhỏ |
| Sort merge join | ghép bằng sắp xếp và trộn |
| Source / Sink | nguồn / đích |
| Sparse retrieval | tìm bằng biểu diễn thưa |
| Sparse vector | vector thưa |
| Spill | tràn dữ liệu tạm ra đĩa |
| Stage | giai đoạn thực thi |
| Standalone cluster | cụm Spark tự quản |
| State | trạng thái giữ giữa các batch |
| Status code | mã trạng thái |
| Step budget | giới hạn số bước |
| Struct | cấu trúc có trường |
| Structured log | log có cấu trúc |
| Structured output | đầu ra có cấu trúc |
| Structured Streaming | xử lý luồng trên bảng |
| Synchronous / Asynchronous | đồng bộ / bất đồng bộ |
| Task | tác vụ xử lý một partition |
| TaskFlow | API tạo task từ hàm |
| Temporal fold | cặp train và validation theo thời gian |
| Temporal split | chia tập theo thời gian |
| Tenant | nhóm dữ liệu tách biệt |
| Tensor | mảng số nhiều chiều |
| TF-IDF | trọng số từ theo tần suất |
| Threshold | ngưỡng quyết định |
| Throughput | số request mỗi đơn vị thời gian |
| Tie-breaker | tiêu chí phụ để phân thứ tự |
| Time travel | đọc phiên bản dữ liệu cũ |
| Timeout | giới hạn thời gian |
| tmp_path | thư mục tạm riêng của test |
| Token | đơn vị văn bản của tokenizer |
| Tokenizer | bộ chia mã hóa token |
| Tool calling | model đề xuất sử dụng công cụ |
| Tool schema | lược đồ tham số công cụ |
| Top-k | k kết quả đầu |
| Trace | dấu vết các bước |
| Trade-off | đánh đổi kỹ thuật |
| Train / Eval mode | chế độ học / đánh giá |
| Train-only statistics | thống kê chỉ học từ train |
| Transformer | kiến trúc mạng dùng attention |
| Trusted role | vai trò từ tầng xác thực |
| UDF — User Defined Function | hàm do người dùng định nghĩa |
| Unit test | kiểm thử đơn vị logic |
| Unseen category | giá trị nhóm chưa gặp |
| Upsert | thêm hoặc cập nhật theo ID |
| Usage | lượng token sử dụng |
| Validation | kiểm tra cấu trúc và quy tắc |
| Vector store | kho tìm vector |
| VectorAssembler | bộ ghép cột thành vector |
| Version | phiên bản cụ thể |
| Volume | vùng lưu gắn ngoài |
| Watermark | mốc tiến độ theo thời gian sự kiện |
| Worker | tiến trình phục vụ |
| Workflow | luồng bước định trước |
