# Ngày 14 — Lý thuyết: Kết hợp Spark với hệ sinh thái ML

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Tạo nhánh scikit-learn có giới hạn dữ liệu và giữ preprocessing trong artifact.

## 1. Chia trách nhiệm theo bước
Spark có thể xử lý nguồn lớn rồi tạo một bảng feature đủ nhỏ để scikit-learn học trên một máy. **Single-machine training (huấn luyện trên một máy)** vẫn là huấn luyện trên một máy dù file đầu vào do Spark tạo. **Distributed training (huấn luyện phân tán một mô hình)** phải dùng cơ chế phối hợp được thuật toán hỗ trợ. Chạy nhiều thí nghiệm độc lập trên nhiều worker là một kiểu song song khác.

## 2. Trước khi toPandas phải có giới hạn
**Sampling (lấy mẫu)** và **aggregation (tổng hợp)** giảm dữ liệu có chủ đích. Đặt **memory budget (giới hạn bộ nhớ)** và giới hạn số dòng, chọn đúng cột rồi mới toPandas. Với file nhỏ, byte trên đĩa không bằng bộ nhớ sau giải nén hoặc sau tạo đối tượng. Một cách chặn đơn giản trong bài là đọc tối đa 10.001 dòng và dừng nếu vượt 10.000; với dữ liệu thật còn cần ước lượng chiều rộng và bộ nhớ.

**pandas API on Spark (API giống pandas nhưng chạy trên Spark)** không biến mọi thư viện pandas thành phân tán tự động. **Pandas UDF (hàm Python xử lý theo lô pandas)** và mapInPandas hữu ích khi có logic phù hợp, nhưng phải chốt schema, kích thước lô và tránh API ngoài thiếu kiểm soát.

## 3. Chọn artifact phù hợp nơi phục vụ
Nhánh scikit-learn dùng Pipeline để điền thiếu, mã hóa và học cùng nhau; lưu bằng joblib rồi phục vụ bằng FastAPI ở ngày 21. Artifact này khác PipelineModel của Spark. Giữ hai tên và phiên bản riêng. Với PyTorch, Spark nên xuất **shard (phần dữ liệu huấn luyện được chia sẵn)** để DataLoader đọc dần; không cần kéo toàn bộ dữ liệu lên driver trước.

So hai nhánh bằng cùng định nghĩa nhãn, cùng snapshot và metric cùng ý nghĩa. Không yêu cầu hai thuật toán có xác suất bằng nhau; yêu cầu mỗi nhánh tái lập được và có hợp đồng đầu vào rõ ràng.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
# Ví dụ giới hạn trước khi đưa dữ liệu nhỏ về driver.
small = read_events(spark, "events_tiny.csv").select("customer_id", "amount").limit(10001)
if small.count() > 10000:
    raise ValueError("Vượt giới hạn lab 10.000 dòng; cần lấy mẫu hoặc xuất shard")
print(small.toPandas())
```

## Năm ý đối chiếu với lộ trình gốc

- 14.1 — Spark MLlib và scikit learn giải quyết các phạm vi khác nhau.
- 14.2 — Sampling, aggregation và ước lượng bộ nhớ trước khi chuyển sang pandas.
- 14.3 — pandas API on Spark, pandas UDF và mapInPandas ở mức sử dụng có mục đích.
- 14.4 — Spark chuẩn bị dữ liệu cho PyTorch; định dạng, shard và hợp đồng dữ liệu.
- 14.5 — Phân biệt huấn luyện phân tán một mô hình với chạy nhiều thí nghiệm độc lập.

Các ý trên giữ phạm vi phần 14 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Spark chuẩn bị dữ liệu khác distributed training thế nào?
2. Cần giới hạn gì trước toPandas?
3. Vì sao API sẽ dùng nhánh sklearn?

## Đọc thêm từ nguồn chính thức

- [scikit-learn Pipeline](https://scikit-learn.org/1.5/modules/compose.html)
- [PySpark pandas/Arrow integration](https://spark.apache.org/docs/3.5.7/api/python/user_guide/sql/arrow_pandas.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
