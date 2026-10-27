# Vì sao khóa học được tổ chức lại

[Khóa đang học](../README.md)

Đánh giá ngày 26/10/2026: bản trước đủ chủ đề để tra cứu toàn cảnh, nhưng chưa đủ các bước giảng và luyện cho người chưa học Spark. Có nhiều file hoặc chạy được mẫu không đồng nghĩa tài liệu dạy được từ số 0.

## Những điểm gây khó cụ thể

| Vấn đề trong bản trước | Ảnh hưởng với người mới | Đã đổi |
| --- | --- | --- |
| Ngày 01 cùng lúc nói Spark, phân tán, streaming, churn, feature, MLflow, API | Chưa có thao tác cơ bản để gắn nghĩa cho thuật ngữ | Ngày 01 chỉ bảng 3 dòng, dòng/cột, tính tay và vai trò Spark |
| Bài đầu yêu cầu chọn công cụ cho 2 TB, vẽ pipeline và giả định tài nguyên | Bài tập thiết kế vượt quá kiến thức vừa được dạy | Luyện thay một đơn rồi tự tính, tăng độ khó theo kỹ năng |
| Mã khởi động thường ngắn hơn rất nhiều so với yêu cầu lab | Đọc mẫu xong vẫn không biết viết bước tiếp | Thêm vi_du.py hoàn chỉnh, giải thích từng phần, gợi ý và đối chiếu mở sau khi thử |
| Ngày 02 yêu cầu “đã xong ngày 02” | Điều kiện vòng lặp, không biết bắt đầu ở đâu | Cài đặt riêng ngày 03, chỉ yêu cầu ngày 02 Python cơ bản |
| Làm sạch ngày 05 cần Window ngày 06 | Phụ thuộc ngược, phải học trước mới làm được bài hiện tại | Tách NULL, trùng, cast; Window đến ngày 21 sau group/sort/join |
| Ngày 03 đi vào job/stage/task và plan | Học tên kiến trúc trước khi có trải nghiệm tính toán | Thực thi/partition đến ngày 26–27 sau các báo cáo thực tế |
| File ví dụ và nhật ký có lời giải mẫu dài nhưng chưa xác nhận người học hiểu | Dễ nhầm xem/chạy mẫu với tự thực hành | Giữ mẫu cũ, tách ví dụ và bài làm mới; tiến độ chỉ đánh dấu điều tự làm được |
| 30 ngày gồm Spark + ML + MLOps + API + RAG + fine-tuning | Độ rộng vượt quá mục tiêu xây nền ở 2–3 giờ/ngày | 30 ngày đầu tập trung Spark, một dự án nhỏ; các chặng khác nối sau |
| Bộ kiểm tra đếm file, link, 150 đầu mục | Chỉ xác nhận cấu trúc, chưa xác nhận khả năng dạy | Kiểm tra phụ thuộc xuôi, ví dụ tự chạy, dữ liệu tính tay, lời giải/gợi ý và bảo toàn bài cũ |

## Phạm vi hợp lý với 2–3 giờ/ngày

Khoảng 60–90 giờ trong 30 buổi dành cho nền PySpark: đọc và hiểu bảng, schema, thao tác cột/dòng, tổng hợp, lỗi dữ liệu, file, SQL, join, window, chạy theo ngày và thực thi cơ bản. Có buổi ôn ở ngày 14 và dự án/tự kiểm tra ở ngày 29–30.

Đây là ước lượng học tập, không bảo đảm ai cũng cần cùng số giờ. Nếu một kỹ năng chưa tự làm được, thêm một buổi cho nó thay vì bỏ qua để giữ lịch. Phần cluster thực tế, streaming đầy đủ, Machine Learning, MLOps và RAG có thứ tự nối tiếp ở HOC_TIEP.md.

## Bảo toàn bài làm đang có

Trước khi thay khóa đang học, toàn bộ 178 tệp nội dung cũ được sao chép vào tham_khao/lo_trinh_tong_hop và đối chiếu SHA-256. Có cả bai_lam.py/ghi_chu.md ngày 01 hiện có, tiến độ, dữ liệu, code tiện ích và file gốc. Danh mục hash nằm trong BAN_LUU.json.

Không sửa Git index hay tự commit. Nhật ký khóa nền được mở mới; bản cũ giữ nguyên để bạn tra lại. Tên ngày trong hai khóa có ý nghĩa khác nhau.

## Giới hạn cần hiểu

Kiểm tra chương trình mẫu xác nhận code/dữ liệu và đầu ra được kỳ vọng, không chứng minh người học đã hiểu. Tiêu chí học là tự làm biến thể, giải thích được kết quả và biết thu nhỏ một lỗi. Nếu một đoạn lý thuyết vẫn khó, đó là chỗ cần viết thêm ví dụ, không phải lý do ép chuyển ngày.
