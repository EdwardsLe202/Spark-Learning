# Spark, MLOps và AI Engineering trong 30 ngày

Lộ trình thực hành tiếng Việt dành cho người đã dùng Python và SQL, bám theo 30 phần và 150 ý học trong [tài liệu gốc](Lo_trinh_Spark_MLOps_AI_Engineering.docx). Mỗi ngày có lý thuyết dễ hiểu, ví dụ khởi động, bài tự làm, kết quả đối chiếu và nhật ký. Thuật ngữ mới được ghi bằng tiếng Anh kèm nghĩa tiếng Việt khi giới thiệu.

## Bắt đầu

1. Mở [ngày 01](day-01/README.md), đọc lý thuyết rồi làm lab ngay trong thư mục ngày.
2. Đến ngày 02, làm theo [cài đặt macOS](docs/CAI_DAT.md): Python 3.11, Java 17, PySpark 3.5.7. Không dùng Python mặc định mà chưa kiểm tra phiên bản.
3. Sửa `day-XX/bai_lam.py`, chạy `python scripts/run_day.py XX` từ repo, lưu kết quả vào `ghi_chu.md` của ngày.
4. Tự kiểm tra tiêu chí rồi cập nhật [TIEN_DO.md](TIEN_DO.md). Khi cần hướng dẫn, gửi ngày, bước, code, lệnh chạy và kết quả.

## Nhịp học và phạm vi

Dành khoảng **3–4 giờ/ngày**, ưu tiên viết, chạy, đọc lỗi và giải thích lại. Đây là vòng học cốt lõi tăng tốc, khoảng 90–120 giờ, có bài mở rộng để đào sâu. Tài liệu gốc ước tính **306–430 giờ**: thực hiện đầy đủ cùng độ sâu trong 30 ngày tương đương khoảng 10–14 giờ/ngày. Vì vậy hoàn thành lịch 30 ngày không đồng nghĩa đã có độ sâu của toàn bộ lộ trình dài.

Một phần gốc tương ứng một ngày để bạn tra cứu dễ dàng. Mỗi file lý thuyết giữ cả năm ý gốc để không bỏ sót phạm vi. Airflow, Docker, cloud, model lớn và LoRA có nhánh mở rộng; phần cốt lõi dùng dữ liệu nhỏ và local. Ba dự án được tích lũy từ các ngày trước; dùng ngày 30 để nghiệm thu, sửa thiếu và demo.

## Lịch học

| Ngày | Chủ đề | Đầu ra chính |
| --- | --- | --- |
| [01](day-01/README.md) | Spark trong công việc Data Science | Sơ đồ và quyết định dùng công cụ |
| [02](day-02/README.md) | Môi trường Spark trên macOS | Môi trường và smoke check |
| [03](day-03/README.md) | Kiến trúc và cách Spark thực thi | Plan, UI, giải thích thực thi |
| [04](day-04/README.md) | DataFrame và Spark SQL căn bản | DataFrame/SQL cùng kết quả |
| [05](day-05/README.md) | Làm sạch và khám phá dữ liệu | Clean/quarantine và đối soát |
| [06](day-06/README.md) | Join tổng hợp và window function | Join/window có kiểm tra khóa |
| [07](day-07/README.md) | Đọc ghi và tổ chức lưu trữ | Parquet và thiết kế lưu trữ |
| [08](day-08/README.md) | Partition shuffle và nền tảng RDD | Word count, partition, shuffle |
| [09](day-09/README.md) | Tối ưu và xử lý lỗi hiệu năng | Báo cáo tối ưu theo phép đo |
| [10](day-10/README.md) | Pipeline tăng dần và Structured Streaming | Incremental và stream phục hồi |
| [11](day-11/README.md) | Feature engineering và phòng tránh leakage | Dự án 1: feature đúng thời điểm |
| [12](day-12/README.md) | Pipeline Machine Learning với Spark | PipelineModel lưu/load |
| [13](day-13/README.md) | Đánh giá lựa chọn và tuning mô hình | Bảng metric và chọn threshold |
| [14](day-14/README.md) | Kết hợp Spark với hệ sinh thái ML | Nhánh model sklearn cho API |
| [15](day-15/README.md) | Theo dõi thí nghiệm và quản lý mô hình | MLflow run, artifact, version |
| [16](day-16/README.md) | Cấu trúc project kiểm thử và chất lượng code | Module, CLI và test nghiệp vụ |
| [17](day-17/README.md) | Lập lịch và điều phối pipeline | Workflow, retry và backfill |
| [18](day-18/README.md) | Đóng gói và dự đoán hàng loạt | Batch prediction có metadata |
| [19](day-19/README.md) | CI CD và nền tảng triển khai | CI, release và rollback local |
| [20](day-20/README.md) | Giám sát drift và huấn luyện lại | Drift report và policy retrain |
| [21](day-21/README.md) | Backend và API cho hệ thống AI | API dự đoán có validation |
| [22](day-22/README.md) | PyTorch và nền tảng Transformer | PyTorch train/checkpoint/load |
| [23](day-23/README.md) | Model serving hiệu năng và độ tin cậy | Dự án 2: báo cáo tải và vận hành |
| [24](day-24/README.md) | LLM prompting và đầu ra có cấu trúc | Prompt, schema và đánh giá đầu ra |
| [25](day-25/README.md) | Chuẩn bị tài liệu và xây chỉ mục RAG | Chunk/index và update/delete |
| [26](day-26/README.md) | Truy xuất hybrid search và reranking | Benchmark dense và hybrid |
| [27](day-27/README.md) | Đánh giá bảo mật và quan sát ứng dụng RAG | 40 ca eval, trace và quyền |
| [28](day-28/README.md) | Tool calling và workflow có tác nhân | Workflow dùng công cụ có giới hạn |
| [29](day-29/README.md) | Fine tuning và tối ưu mô hình nâng cao | Quyết định fine-tune và kế hoạch |
| [30](day-30/README.md) | Dự án cuối khóa và chuẩn bị ứng tuyển | Nghiệm thu ba dự án và demo |

## Cấu trúc để tự làm trong repo

```text
day-01/ ... day-30/
  README.md       Mục tiêu, điều kiện và thứ tự học
  ly_thuyet.md    Giải thích, thuật ngữ, ví dụ và nguồn
  thuc_hanh.md    Bước làm, kết quả, lỗi thường gặp và mở rộng
  bai_lam.py      Ví dụ khởi động + TODO để bạn viết tiếp
  ghi_chu.md      Lệnh chạy, kết quả, câu hỏi và nhật ký
data/raw/         CSV giả lập, tiny fixture, dirty fixture và hash
data/rag/         Tài liệu tự tạo và 40 câu hỏi có nhãn
projects/         Đặc tả, checklist và nơi gom code của ba mốc
scripts/          Chạy bài, tạo dữ liệu, kiểm tra repo
artifacts/        Đầu ra local, được Git bỏ qua
```

File khởi động minh họa một phần kiến thức để bạn có điểm bắt đầu; chạy thành công file này **chưa hoàn thành lab**. Bạn tự viết các bước, test và báo cáo còn lại. Các đoạn TODO được giữ có chủ đích. Không có đáp án hoàn chỉnh làm thay phần thực hành.

## Tài liệu dùng chung

- [Cài đặt và xử lý lỗi](docs/CAI_DAT.md)
- [Quy ước dữ liệu, thời gian và nhãn churn](data/README.md)
- [Corpus và tập eval RAG](data/rag/README.md)
- [Thuật ngữ Anh–Việt](docs/THUAT_NGU.md)
- [Nguồn chính thức và đối chiếu lộ trình](docs/NGUON_HOC.md)
- [Ba dự án và rubric tự đánh giá](projects/README.md)
- [Phạm vi kiểm tra bộ học](docs/KIEM_TRA.md)

Mọi dữ liệu đi kèm là giả lập phục vụ học tập. Chỉ lưu số liệu bạn đã đo; ghi rõ giới hạn local, mock và phần chưa triển khai. Các artifact của ngày trước cần giữ lại hoặc tái tạo theo nhật ký để làm ngày sau.
