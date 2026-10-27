# Ngày 01 — Lý thuyết: Spark trong công việc Data Science

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Chọn đúng nơi dùng Spark và vẽ được luồng dữ liệu đến dự đoán churn.

## 1. Spark giải quyết việc gì?
**Apache Spark (bộ máy xử lý dữ liệu phân tán)** nhận một kế hoạch tính toán rồi chia công việc thành nhiều phần. Spark không phải nơi lưu dữ liệu: CSV, Parquet hoặc cơ sở dữ liệu mới là nơi dữ liệu tồn tại lâu dài. **PySpark (giao diện Python của Spark)** cho phép bạn mô tả phép tính bằng Python, còn nhiều phép xử lý bảng chạy trong bộ máy Spark.

Hãy tưởng tượng có một người tổng hợp hóa đơn và nhiều người phụ trách từng chồng hóa đơn. Chia việc có ích khi khối lượng đủ lớn; với 20 hóa đơn, thời gian phân công có thể lớn hơn thời gian tự cộng. Vì vậy, dữ liệu vừa RAM và phép tính đơn giản thường phù hợp với pandas hoặc SQL sẵn có. Đừng chọn Spark chỉ vì tên công cụ.

## 2. Phân biệt các luồng công việc
**Batch processing (xử lý theo lô)** xử lý một tập dữ liệu hữu hạn, chẳng hạn đơn hàng hôm qua. **Stream processing (xử lý luồng)** xử lý dữ liệu mới liên tục, chẳng hạn sự kiện trên ứng dụng. **Parallel processing (xử lý song song)** có thể nằm trên một máy; **distributed processing (xử lý phân tán)** phối hợp nhiều máy. Chạy Spark local nhiều luồng chưa chứng minh hệ thống hoạt động trên nhiều máy.

**Data pipeline (chuỗi xử lý dữ liệu)** đọc, kiểm tra, làm sạch và tạo bảng. **ML pipeline (chuỗi xử lý học máy)** biến đổi đầu vào và huấn luyện hoặc dự đoán. **MLOps (vận hành vòng đời mô hình học máy)** bổ sung phiên bản, kiểm thử, phát hành và giám sát để biết mô hình nào đang chạy, tạo từ dữ liệu nào.

## 3. Bài toán xuyên suốt
**Churn (ngừng hoạt động theo định nghĩa bài toán)** ở đây là không có giao dịch trong 30 ngày tiếp theo. Spark tạo đặc trưng lịch sử; Spark ML hoặc scikit-learn huấn luyện; MLflow ghi thí nghiệm; FastAPI nhận yêu cầu dự đoán. Một công cụ không thay toàn bộ vai trò còn lại. Ở ngày 11 bạn sẽ chốt mốc thời gian để tránh dùng dữ liệu tương lai.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
from spark_lab import DATA
print("Dữ liệu giao dịch:", DATA / "raw" / "events.csv")
print("raw -> validate -> features -> train -> evaluate -> predict -> monitor")
```

## Năm ý đối chiếu với lộ trình gốc

- 01.1 — Spark và PySpark là gì; phân biệt bộ máy xử lý với nơi lưu dữ liệu.
- 01.2 — Xử lý song song và phân tán; batch và streaming qua ví dụ đơn hàng.
- 01.3 — So sánh pandas, SQL và Spark theo bộ nhớ, thời gian và độ phức tạp.
- 01.4 — Phân biệt pipeline dữ liệu, pipeline ML và quy trình MLOps.
- 01.5 — Hai hướng ML: Spark chuẩn bị dữ liệu cho thư viện khác hoặc dùng Spark MLlib.

Các ý trên giữ phạm vi phần 01 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Vì sao không đưa toàn bộ bảng Spark về pandas?
2. Batch khác streaming ở điểm nào?
3. MLflow lưu thí nghiệm còn Spark làm gì?

## Đọc thêm từ nguồn chính thức

- [Spark overview](https://spark.apache.org/docs/3.5.7/)
- [PySpark overview](https://spark.apache.org/docs/3.5.7/api/python/index.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
