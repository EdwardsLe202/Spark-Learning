# Thuật ngữ tiếng Anh và giải thích tiếng Việt

[Lộ trình](../README.md)

Các nghĩa dưới đây theo ngữ cảnh của repo; đọc ví dụ trong từng ngày để thấy điều kiện áp dụng. Khi viết nhật ký, thử giải thích lại bằng lời của bạn.

| English term | Giải thích tiếng Việt |
| --- | --- |
| AI Engineering | Kỹ thuật xây dựng, đánh giá và vận hành hệ thống ứng dụng trí tuệ nhân tạo. |
| Data Science | Khoa học dữ liệu, dùng dữ liệu và phương pháp phân tích để trả lời câu hỏi hoặc xây mô hình. |
| Feature engineering | Kỹ thuật tạo, lựa chọn và kiểm tra đặc trưng đầu vào theo đúng thời điểm dự đoán. |
| Inference | Suy luận hoặc dự đoán bằng mô hình đã học, không phải huấn luyện thêm. |
| Machine Learning | Học máy, xây mô hình học quy luật từ dữ liệu. |
| MLlib | Thư viện học máy của Spark; bài này ưu tiên API DataFrame trong pyspark.ml. |
| TODO | Nhãn đánh dấu phần việc người học cần hoàn thiện trong code. |
| Training | Huấn luyện, dùng dữ liệu để học tham số hoặc quy tắc của mô hình. |
| Workflow | Luồng công việc gồm các bước và quan hệ phụ thuộc để hoàn thành tác vụ. |
| Accumulator | Biến tích lũy để thống kê; không dùng làm sổ cái nghiệp vụ khi có retry. |
| Action | Thao tác yêu cầu kết quả hoặc ghi dữ liệu và kích hoạt thực thi cần thiết. |
| Agent loop / Step budget | Vòng lặp chọn bước tiếp / giới hạn số bước được chạy. |
| Aggregation | Tổng hợp nhiều dòng thành kết quả theo nhóm. |
| Alias | Bí danh có thể thay đổi để trỏ tới một model version. |
| Allowlist | Danh sách thành phần được phép, ngoài danh sách phải bị chặn. |
| Apache Spark | Bộ máy xử lý dữ liệu có thể phân phối việc tính toán trên nhiều máy. |
| API / HTTP | Giao diện ứng dụng giao tiếp / giao thức yêu cầu-phản hồi trên web. |
| AQE | Adaptive Query Execution, điều chỉnh kế hoạch dựa vào thống kê lúc chạy. |
| Artifact | File đầu ra cần lưu như model, biểu đồ, báo cáo hoặc cấu hình. |
| Attention / Transformer | Cơ chế kết hợp thông tin theo mức liên quan / kiến trúc mạng dùng attention. |
| Authentication / Authorization | Xác thực danh tính / kiểm tra quyền được làm gì. |
| Autologging | Tự động ghi một số thông tin huấn luyện, không thay mọi metadata nghiệp vụ. |
| Backend store / Artifact store | Kho metadata thí nghiệm / kho các tệp đầu ra. |
| Backfill | Xử lý bù một khoảng dữ liệu trong quá khứ. |
| Baseline | Mốc code, cấu hình và kết quả để so sánh thay đổi. |
| Batch inference | Dự đoán một tập dữ liệu theo đợt. |
| Batch processing | Xử lý một tập dữ liệu hữu hạn theo đợt. |
| Broadcast join | Ghép bằng cách phát phía nhỏ tới nơi xử lý phía còn lại khi phù hợp. |
| Broadcast variable | Biến chỉ đọc được phân phối để các task tái sử dụng. |
| Cache | Giữ kết quả tính để tái sử dụng, có chi phí vật hóa và chiếm bộ nhớ. |
| Canary / Shadow | Phát hành cho phần nhỏ lưu lượng / chạy quan sát song song chưa dùng kết quả. |
| Cardinality | Quan hệ số lượng giữa khóa của các bảng, như một-nhiều hay nhiều-nhiều. |
| Catalog | Danh mục giữ tên bảng, schema và thông tin mô tả bảng. |
| Checkpoint | Trạng thái hoặc dữ liệu lưu để hỗ trợ phục hồi theo cơ chế cụ thể. |
| Churn | Ngừng hoạt động theo định nghĩa; bài này là không giao dịch trong 30 ngày sau cutoff. |
| CI / CD | Kiểm tra khi tích hợp code / chuẩn bị hoặc thực hiện phát hành theo chính sách. |
| CI CD | Kiểm tra và phát hành thay đổi bằng quy trình có kiểm soát. |
| Class imbalance | Sự chênh lệch số mẫu giữa các lớp. |
| Client mode / Cluster mode | Driver chạy phía gửi job / driver chạy trong cụm máy. |
| Cluster manager | Bộ phận cấp tài nguyên cho ứng dụng trong cụm máy. |
| Coalesce | Gộp giảm partition, thường tránh shuffle đầy đủ nhưng có thể lệch tải. |
| Column expression | Biểu thức cột mô tả phép tính cho dữ liệu mà chưa kéo từng giá trị về Python. |
| Concept drift | Thay đổi quan hệ giữa đầu vào và mục tiêu, cần bằng chứng phù hợp. |
| Configuration | Các lựa chọn của một lần chạy hoặc môi trường. |
| Confusion matrix | Bảng TP, FP, TN, FN để thấy đúng và sai theo lớp. |
| Contamination | Dữ liệu test hoặc thông tin đáp án lọt vào train hay quá trình chọn cấu hình. |
| Correctness / Citation / Abstention | Đúng nội dung / trích dẫn hỗ trợ / từ chối khi thiếu căn cứ. |
| Cross-validation | Đánh giá qua nhiều lần chia tập phù hợp cấu trúc dữ liệu. |
| Cutoff time | Mốc chốt thông tin được phép dùng tại lúc giả định dự đoán. |
| DAG | Directed Acyclic Graph, đồ thị có hướng không chu trình biểu diễn workflow. |
| Data contract | Hợp đồng gồm schema, khóa, miền giá trị và ý nghĩa dữ liệu. |
| Data freshness | Mức mới của dữ liệu đang được dùng so với yêu cầu cập nhật. |
| Data interval | Khoảng dữ liệu một lần chạy chịu trách nhiệm xử lý. |
| Data lake | Kho dữ liệu trên lưu trữ dạng tệp hoặc đối tượng. |
| Data skew | Dữ liệu lệch khóa khiến một số task nhận việc nhiều hơn hẳn. |
| DataFrame | Bảng dữ liệu có tên cột và kiểu dữ liệu, được Spark biểu diễn bằng kế hoạch thực thi. |
| Dataset / DataLoader | Đối tượng cấp mẫu dữ liệu / bộ đọc theo lô. |
| Dense / Sparse retrieval | Truy xuất bằng vector đặc / bằng biểu diễn thưa. |
| Dependency | Thư viện hoặc thành phần mà chương trình cần để chạy. |
| Distributed processing | Phối hợp xử lý trên nhiều máy. |
| Dockerfile / Docker Compose | Tệp mô tả build image / cấu hình phối hợp nhiều container. |
| Drift | Sự thay đổi dữ liệu hoặc quan hệ thống kê; cần phân tích ảnh hưởng tới model. |
| Driver | Tiến trình điều phối ứng dụng Spark và lập kế hoạch thực thi. |
| Duplicate | Bản ghi trùng toàn dòng hoặc trùng khóa theo định nghĩa nghiệp vụ. |
| EDA | Exploratory Data Analysis, phân tích khám phá để hiểu dữ liệu và lỗi. |
| Embedding | Biểu diễn dữ liệu bằng vector theo một model cụ thể. |
| Entity | Đối tượng dự đoán như khách hàng, cùng khóa và thời điểm tương ứng. |
| Estimator | Thành phần có thể fit dữ liệu để tạo Model trong Spark ML. |
| Event time / Processing time | Thời gian sự kiện xảy ra / thời gian hệ thống xử lý sự kiện. |
| Exactly-once | Bảo đảm hiệu ứng ghi đúng một lần theo điều kiện nguồn, đích và thiết kế cụ thể. |
| Exception / Exit code | Ngoại lệ biểu thị lỗi / mã kết thúc để bên gọi biết thành công hay thất bại. |
| Execution plan | Kế hoạch cho biết Spark sẽ thực hiện phép tính như thế nào. |
| Executor | Tiến trình thực hiện task và quản lý phần dữ liệu được giao. |
| Experiment / Run | Nhóm thí nghiệm / một lần thực thi trong nhóm. |
| Feature | Biến đầu vào cung cấp thông tin cho mô hình. |
| Fine tuning | Điều chỉnh tham số model bằng dữ liệu huấn luyện bổ sung. |
| Fixture | Dữ liệu hoặc thiết lập nhỏ dùng cho kiểm thử. |
| Forward / Loss / Backward / Optimizer | Tính đầu ra / đo sai lệch / tính gradient / cập nhật trọng số. |
| Gradient | Đạo hàm dùng xác định hướng cập nhật trọng số. |
| Groundedness | Mức độ câu trả lời được hỗ trợ bởi bằng chứng cung cấp. |
| Health / Readiness | Tiến trình còn sống / ứng dụng sẵn sàng nhận công việc. |
| Hybrid search / RRF | Kết hợp nhiều nguồn tìm kiếm / hợp nhất bằng nghịch đảo thứ hạng. |
| Hyperparameter tuning | Chọn cấu hình của quá trình học như mức regularization. |
| I/O | Input/Output, các thao tác đọc ghi với bên ngoài. |
| IAM / Service account | Quản lý danh tính và quyền / danh tính dành cho ứng dụng. |
| Idempotency | Chạy lại cùng tác vụ có kiểm soát mà không gây tác dụng lặp ngoài ý muốn. |
| Image / Container / Volume | Mẫu môi trường đóng gói / tiến trình chạy từ image / vùng lưu gắn bên ngoài. |
| Imputer | Bộ học và áp dụng quy tắc điền giá trị thiếu. |
| Incremental processing | Xử lý phần dữ liệu mới hoặc thay đổi thay vì tính lại tất cả. |
| Ingestion / Chunk / Overlap | Đưa dữ liệu vào hệ thống / đoạn để truy xuất / phần giao giữa các đoạn. |
| Input example | Mẫu đầu vào minh họa contract cho model. |
| JDBC | Java Database Connectivity, giao diện kết nối cơ sở dữ liệu từ Java. |
| Job | Công việc thực thi được Spark tạo khi cần tính kết quả. |
| JVM | Java Virtual Machine, máy ảo chạy mã Java và bộ máy Spark. |
| Late-arriving data | Dữ liệu có thời gian sự kiện cũ nhưng đến hệ thống muộn. |
| Latency / Throughput / Concurrency | Độ trễ mỗi yêu cầu / lưu lượng xử lý mỗi đơn vị thời gian / số yêu cầu đồng thời. |
| Lazy evaluation | Trì hoãn thực thi phần tính toán cho tới khi cần kết quả. |
| Leakage | Dùng thông tin chưa có tại lúc dự đoán hoặc làm lộ tập đánh giá vào quá trình học. |
| Lifespan | Giai đoạn khởi động và kết thúc tài nguyên của ứng dụng. |
| Lineage | Quan hệ nguồn gốc giữa dữ liệu, bước xử lý, thí nghiệm và kết quả. |
| LLM / Token / Context window | Mô hình ngôn ngữ lớn / đơn vị tokenizer / giới hạn ngữ cảnh của model. |
| Logical plan | Kế hoạch mô tả ý nghĩa truy vấn và phép biến đổi. |
| Logistic regression | Mô hình phân loại tuyến tính qua xác suất logistic. |
| Metadata / Content hash | Thông tin mô tả / mã băm định danh nội dung. |
| Micro-batch | Lô nhỏ được xử lý lặp lại để xử lý luồng tăng dần. |
| Model registry | Nơi quản lý phiên bản và metadata của mô hình. |
| Model signature | Mô tả kiểu và cấu trúc đầu vào, đầu ra của model. |
| Module / CLI | Đơn vị mã nguồn Python / giao diện chạy qua dòng lệnh. |
| Monitoring | Theo dõi hoạt động hệ thống, dữ liệu và chất lượng model. |
| MPS / CUDA | Backend tính toán cho thiết bị Apple phù hợp / nền tảng tính toán GPU của NVIDIA. |
| NaN | Not a Number, giá trị số không xác định theo cách biểu diễn số thực. |
| Narrow dependency | Phụ thuộc hẹp giữa các partition, thường không cần shuffle toàn bộ. |
| NULL | Giá trị thiếu hoặc chưa biết, khác chuỗi rỗng và khác số 0. |
| Object storage | Lưu trữ đối tượng với khóa định danh, thường dùng cho dữ liệu dạng file. |
| Observation window / Label window | Khoảng lịch sử tạo feature / khoảng tương lai xác định nhãn. |
| OneHotEncoder | Bộ mã hóa nhóm thành vector chỉ báo. |
| Online inference | Dự đoán theo request với yêu cầu thời gian phản hồi. |
| OOM | Out-of-memory, lỗi hết bộ nhớ ở driver hoặc nơi thực thi. |
| Orchestration | Điều phối các bước theo phụ thuộc, lịch và chính sách lỗi. |
| Overfitting | Mô hình học quá sát train nên kém trên dữ liệu mới. |
| p50 / p95 / p99 | Các phân vị độ trễ 50, 95 và 99, cần nêu số mẫu và cách đo. |
| Parallel processing | Thực hiện nhiều phần công việc đồng thời, có thể trên cùng một máy. |
| Parameter / Metric / Tag | Cấu hình / chỉ số đo / nhãn metadata của thí nghiệm. |
| Partition | Phần dữ liệu làm đơn vị xử lý song song; khác với thư mục phân vùng. |
| Partition pruning | Bỏ qua các thư mục phân vùng không phù hợp điều kiện truy vấn. |
| PEFT / LoRA | Fine-tuning ít tham số / điều chỉnh bằng các ma trận hạng thấp. |
| Physical plan | Kế hoạch lựa chọn cách xử lý cụ thể như loại join. |
| Point-in-time correctness | Chỉ dùng thông tin thực sự đã có ở thời điểm dự đoán. |
| Portfolio / Model card / Runbook | Bộ dự án minh chứng / mô tả model và giới hạn / hướng dẫn vận hành sự cố. |
| PR AUC / ROC AUC | Diện tích dưới đường precision–recall / ROC, cần ghi định nghĩa cách tính. |
| Precision / Recall | Tỷ lệ đúng trong dự đoán dương / tỷ lệ tìm được mẫu dương thực tế. |
| Predicate pushdown | Đưa điều kiện lọc xuống bộ đọc để giảm dữ liệu phải xử lý. |
| Prediction drift | Thay đổi phân bố score hoặc nhãn dự đoán. |
| Preprocessing | Tiền xử lý như điền thiếu, mã hóa và chuẩn hóa đầu vào. |
| Pretrained model | Mô hình đã được huấn luyện từ trước. |
| Prompt injection | Nội dung không tin cậy chèn chỉ dẫn làm lệch tác vụ hoặc quyền. |
| Prompt template / Few-shot | Mẫu lời nhắc / các ví dụ minh họa cách làm trong ngữ cảnh. |
| PySpark | Giao diện Python để làm việc với Spark. |
| Quality gate | Điều kiện chất lượng cần đạt trước khi chuyển sang bước tiếp. |
| Quantization / Distillation | Giảm độ chính xác biểu diễn số / chuyển kiến thức sang model khác. |
| Quarantine | Vùng giữ dữ liệu lỗi cùng lý do để điều tra và sửa. |
| Queue / Backpressure | Hàng đợi / cơ chế hạn chế nhận thêm việc khi quá tải. |
| RAG | Truy xuất thông tin liên quan rồi dùng thông tin đó hỗ trợ sinh câu trả lời. |
| Range-based window | Cửa sổ theo khoảng giá trị của cột sắp xếp. |
| Rate limit / Payload limit | Giới hạn tần suất / giới hạn kích thước dữ liệu yêu cầu. |
| RDD | Resilient Distributed Dataset, tập dữ liệu phân tán có thể tính lại qua lineage. |
| Recall@k / MRR / nDCG | Độ bao phủ relevant trong k kết quả / vị trí đúng đầu tiên / chất lượng thứ hạng có mức liên quan. |
| Regression test / LLM judge | Test bắt lỗi quay lại / model dùng chấm kết quả nhưng vẫn có thể sai. |
| Release manifest | Bản ghi code, image, model, schema và config của một lần phát hành. |
| Repartition | Phân phối lại dữ liệu thành các partition, thường có shuffle. |
| Request / Response / Status code | Yêu cầu / phản hồi / mã trạng thái xử lý. |
| Reranker | Thành phần sắp xếp lại các ứng viên truy xuất. |
| Resource limit / Quota | Giới hạn tài nguyên của tác vụ / hạn mức sử dụng. |
| Retraining | Huấn luyện lại bằng dữ liệu và điều kiện đánh giá mới. |
| Retry / Timeout | Thử lại có chính sách / giới hạn thời gian chờ hoặc chạy. |
| Rollback | Quay lại phiên bản trước khi phiên bản mới có vấn đề. |
| Row-based window | Cửa sổ theo số vị trí dòng trong thứ tự đã chọn. |
| Runtime | Môi trường thực thi gồm bộ chạy và thư viện cần thiết. |
| Sampling | Lấy một phần mẫu theo quy tắc đã chọn và ghi rõ. |
| Scaling | Chuẩn hóa thang đo feature theo một quy tắc đã học từ train. |
| Schema | Tên cột, kiểu dữ liệu và thông tin cấu trúc của dữ liệu. |
| Schema drift / Data drift | Thay đổi lược đồ / thay đổi phân bố dữ liệu. |
| Schema evolution | Thay đổi lược đồ với chính sách tương thích và kiểm tra rõ ràng. |
| SHA-256 | Hàm băm tạo định danh nội dung; không tự lưu hoặc tái tạo tệp. |
| Shard | Một phần dữ liệu đã chia để đọc hoặc xử lý dần. |
| Shuffle | Phân phối lại dữ liệu giữa các phần thực thi, thường tốn mạng và IO. |
| Side effect | Tác động ra ngoài phép tính như gửi tin hoặc gọi API ghi dữ liệu. |
| Slice evaluation | Đánh giá theo nhóm dữ liệu, chẳng hạn vùng hoặc gói dịch vụ. |
| SLO | Mục tiêu vận hành được đặt cho một chỉ số trong điều kiện xác định. |
| Small files | Nhiều tệp nhỏ gây chi phí liệt kê, mở và lập lịch xử lý. |
| Smoke check | Kiểm tra tối thiểu để biết luồng khởi động, tính toán và đọc ghi hoạt động. |
| Snapshot | Bản dữ liệu tại một mốc được định danh để dùng lại. |
| Sort-merge join | Ghép dữ liệu đã sắp xếp theo khóa, thường đi cùng shuffle. |
| Source / Sink | Nguồn cấp dữ liệu / đích nhận kết quả. |
| SparkSession | Đối tượng làm việc với bảng và SQL trong Spark. |
| Sparse vector / Dense vector | Vector thưa lưu phần tử khác 0 / vector đặc lưu mọi phần tử. |
| Spill | Ghi dữ liệu xử lý tạm ra đĩa khi vượt phần bộ nhớ được dùng. |
| Stage | Giai đoạn gồm các task, thường được tách ở ranh giới shuffle. |
| State | Trạng thái tích lũy giữa các lô, ví dụ kết quả cửa sổ chưa đóng. |
| Stream processing | Xử lý dữ liệu mới tới liên tục hoặc thành các lô nhỏ. |
| StringIndexer | Thành phần Spark ML ánh xạ nhóm dạng chuỗi sang chỉ số. |
| Structured output | Đầu ra có cấu trúc theo schema, chưa bảo đảm đúng dữ kiện. |
| Sync / Async | Thực thi đồng bộ / bất đồng bộ, không tự làm CPU mạnh hơn. |
| Task | Phần việc xử lý một partition trong một stage. |
| Temporary view | Tên bảng nhìn tồn tại trong phạm vi phiên để truy vấn SQL. |
| Tensor / Shape / Dtype / Device | Mảng nhiều chiều / kích thước chiều / kiểu số / thiết bị chạy. |
| Three-valued logic | Logic ba trạng thái đúng, sai và chưa biết trong SQL. |
| Threshold | Ngưỡng đổi score hoặc xác suất thành quyết định. |
| Time zone | Múi giờ dùng diễn giải hoặc hiển thị thời gian. |
| Timestamp | Mốc thời gian; cần hiểu theo múi giờ và quy tắc parse. |
| Tool calling | Model đề xuất gọi công cụ; ứng dụng kiểm tra và thực thi theo quyền. |
| Top-k / Metadata filter | Lấy k kết quả đứng đầu / lọc theo thông tin như quyền và phiên bản. |
| Trace | Dấu vết các bước và thời gian xử lý trong một request. |
| Transformation | Phép tạo dữ liệu biến đổi và thường bổ sung kế hoạch chưa thực thi ngay. |
| Transformer | Thành phần biến đổi DataFrame; một Model đã fit cũng có thể là Transformer. |
| Type casting | Chuyển kiểu dữ liệu, có thể lỗi hoặc tạo NULL tùy cấu hình. |
| UDF | User-Defined Function, hàm do người dùng định nghĩa. |
| Unit test / Integration test | Kiểm thử đơn vị logic / kiểm thử thành phần kết hợp. |
| Upsert | Cập nhật bản ghi đã có theo khóa, thêm nếu chưa có. |
| Validation | Kiểm tra cấu trúc, kiểu, miền giá trị và quy tắc đầu vào hoặc đầu ra. |
| Vector store | Kho lưu và tìm kiếm vector cùng metadata. |
| VectorAssembler | Thành phần Spark ML ghép cột thành vector feature. |
| Virtual environment | Môi trường Python tách riêng dependency cho một dự án. |
| Warm-up / Batching | Khởi động nóng trước đo / gom nhiều mẫu hoặc yêu cầu thành lô. |
| Watermark | Mốc tiến độ theo thời gian sự kiện để quản lý state và dữ liệu trễ. |
| Wide dependency | Phụ thuộc rộng cần phân phối lại dữ liệu theo khóa hoặc cách chia mới. |
| Window function | Hàm tính trên nhóm dòng liên quan và thường giữ nguyên số dòng. |
| Worker node | Máy hoặc thành phần nơi chạy tiến trình thực thi trong cluster. |
