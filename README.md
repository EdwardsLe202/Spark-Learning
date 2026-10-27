# Spark từ số 0 đến MLOps và AI Engineering

**Bắt đầu ở [BAT_DAU.md](BAT_DAU.md). Hôm nay chỉ cần mở ngày 01.**

Khóa này dành cho bạn đã dùng Python/SQL nhưng chưa biết Spark, học khoảng **2–3 giờ/ngày**. Mục tiêu 30 ngày đầu là tự xử lý bảng bằng PySpark và hoàn thành một báo cáo dữ liệu nhỏ có kiểm tra kết quả.

Mỗi ngày chỉ thêm một cụm kỹ năng. Có bảng nhỏ để tính tay, ví dụ chạy được, giải thích lệnh, bài thay đổi nhỏ và gợi ý/lời giải mở sau khi tự thử. Mỗi ngày bắt đầu từ README của ngày; không cần mở toàn bộ repo cùng lúc.

## Toàn bộ lộ trình đã có 150 ngày

Giữ nguyên 30 ngày nền bên dưới. Sau đó học nối đến ngày150, khoảng **300–450 giờ** ở nhịp2–3 giờ/buổi. Xem [lịch đầy đủ](LO_TRINH_DAY_DU.md), [đối chiếu150 ý gốc](docs/DOI_CHIEU_LO_TRINH_GOC.md) và [cài đặt từng chặng](docs/CAI_DAT_NANG_CAO.md).

| Ngày | Chặng |
| --- | --- |
| 31–45 | Spark nâng cao |
| 46–60 | Incremental, streaming, feature và dự án1 |
| 61–80 | ML và Spark ML |
| 81–105 | MLOps |
| 106–120 | API, PyTorch, serving và dự án2 |
| 121–145 | LLM/RAG/tool workflow và dự án3 |
| 146–150 | Fine-tuning mở rộng, portfolio và nghiệm thu |

Đây là kế hoạch học theo đầu ra, không phải hạn phải vượt qua khi chưa hiểu. Ngày01 vẫn chỉ cần mở BAT_DAU.md.

## Mở đúng chỗ

| Bạn đang cần | Mở |
| --- | --- |
| Bắt đầu từ số 0 | [BAT_DAU.md](BAT_DAU.md) |
| Học bài đầu | [Ngày 01](day-01/README.md) |
| Cài môi trường, tới ngày 03 mới làm | [Cài đặt](docs/CAI_DAT.md) |
| Ghi mình đã tự làm được gì | [Tiến độ](TIEN_DO.md) |
| Hiểu vì sao cấu trúc đã đổi | [Đánh giá và thay đổi](docs/DANH_GIA_VA_THAY_DOI.md) |

## 30 ngày đầu — nền Spark

| Ngày | Mỗi buổi tập trung vào |
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

Ngày 14 là buổi ôn; ngày 29–30 dành để tự ghép lại và sửa phần chưa vững. Nếu một ngày cần hai buổi, tiếp tục ở đúng chỗ đang vướng. Không lấy số thư mục đã đọc làm mức thành thạo.

## Cách dùng thư mục một ngày

- `README.md`: điểm bắt đầu, mục tiêu nhỏ và thứ tự mở file.
- `ly_thuyet.md`: giải thích từ ví dụ, thuật ngữ English (tiếng Việt), đọc từng lệnh.
- `thuc_hanh.md`: đoán → chạy mẫu → thay đổi nhỏ → tự làm → đối chiếu.
- `vi_du.py`: chương trình mẫu hoàn chỉnh; từ ngày 04 có đủ mở/đóng Spark.
- `bai_lam.py`: chỗ bạn tự viết; dùng mẫu khởi tạo, tập trung logic đang học.
- `ghi_chu.md`: ghi ngắn điều hiểu, kết quả và câu chưa rõ.

Từ ngày 03, dùng môi trường đã cài. Ví dụ ngày 08:

```bash
python scripts/run_day.py 08 --example
python scripts/run_day.py 08
```

Lệnh đầu chạy mẫu; lệnh sau chạy bài làm của bạn. Chưa cần hiểu hay sửa code trong scripts.

## Đọc sau, khi cần

- [Bảng dữ liệu tám đơn hàng](data/beginner/README.md), bắt đầu dùng từ ngày 06.
- [Từ vựng đang học](docs/THUAT_NGU.md), chỉ tra khi gặp từ.
- [Dự án đầu tiên](projects/01-spark-report/README.md), làm ngày 29.
- [Học tiếp ML, MLOps và AI sau nền Spark](docs/HOC_TIEP.md).
- [Nguồn chính thức](docs/NGUON_HOC.md) và [phạm vi đã kiểm tra](docs/KIEM_TRA.md).

Bản trước ghép cả Spark, MLOps và AI vào 30 ngày nên đi quá nhanh cho người mới. Toàn bộ nội dung cũ, **bài làm và ghi chú ngày 01 đang có**, cùng tiến độ cũ đã được giữ tại [tham_khao](tham_khao/README.md). Tài liệu gốc vẫn có ở [file Word](Lo_trinh_Spark_MLOps_AI_Engineering.docx). Bạn không cần học lại bản cũ song song.
