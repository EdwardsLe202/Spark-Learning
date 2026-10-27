# Ngày 05 — Lý thuyết: Làm sạch và khám phá dữ liệu

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Tách dữ liệu lỗi, giữ bản ghi mới nhất và đối soát số dòng.

## 1. Thiếu dữ liệu và dữ liệu sai khác nhau
**NULL (giá trị thiếu hoặc chưa biết)** không bằng chuỗi rỗng. **NaN — Not a Number (giá trị số không xác định)** cũng khác NULL. SQL dùng **three-valued logic (logic ba trạng thái)**: đúng, sai, chưa biết. Ví dụ `NULL > 0` cho kết quả chưa biết, nên filter giữ điều kiện đúng sẽ không giữ dòng đó. Dùng `isNull()` thay cho `== None`.

**Data quality rule (quy tắc chất lượng dữ liệu)** phải gắn với nghiệp vụ: giao dịch cần khóa, thời gian hợp lệ, số tiền không âm và khách hàng tồn tại. **Quarantine (vùng cách ly dữ liệu lỗi)** giữ bản ghi cùng lý do để sửa, thay vì xóa rồi mất dấu. Nếu một dòng có nhiều lỗi, chốt cách đếm theo một lý do ưu tiên hoặc nhiều cờ; đừng cộng tỷ lệ lỗi chồng nhau như các nhóm rời nhau.

## 2. Trùng khóa phải có quy tắc chọn
**Duplicate (bản ghi trùng)** có thể trùng toàn dòng hoặc trùng khóa nghiệp vụ. Hai dòng D002 trong fixture có cùng event_id nhưng số tiền khác nhau; `dropDuplicates(["event_id"])` không nói rõ dòng nào được giữ. Bài này quy định giữ `ingested_at` lớn nhất. Dùng window ngày 6 để bảo đảm xác định, thêm tiêu chí phụ nếu timestamp bằng nhau.

## 3. Parse và quan sát
**Timestamp (mốc thời gian)** cần được hiểu với **time zone (múi giờ)** cụ thể. Dữ liệu repo dùng UTC với hậu tố Z. Chuẩn hóa thời gian trước khi lọc theo ngày để không lệch cửa sổ. **EDA — Exploratory Data Analysis (phân tích khám phá dữ liệu)** gồm tỷ lệ thiếu, phân bố và các trường hợp biên; với dữ liệu lớn, tổng hợp hoặc lấy mẫu rồi mới vẽ. Struct, array và map là các cấu trúc lồng nhau; `explode` một mảng tạo nhiều dòng và có thể thay đổi mẫu số báo cáo.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
dirty = read_events(spark, "events_dirty.csv")
parsed = (dirty.withColumn("amount_num", F.col("amount").cast("long"))
          .withColumn("event_ts", F.to_timestamp("event_time")))
parsed.select("event_id", "customer_id", "amount_num", "event_ts").show(truncate=False)
```

## Năm ý đối chiếu với lộ trình gốc

- 05.1 — NULL, NaN, chuỗi rỗng và giá trị không hợp lệ; điều kiện ba trạng thái trong SQL.
- 05.2 — Duplicate theo cả dòng hoặc khóa nghiệp vụ; quy tắc giữ bản ghi.
- 05.3 — Xử lý chuỗi, ngày giờ, timezone và parse dữ liệu lỗi.
- 05.4 — Struct, array, map, JSON và explode; ảnh hưởng đến số dòng.
- 05.5 — Thống kê, tần suất, phân vị xấp xỉ, lấy mẫu để vẽ biểu đồ.

Các ý trên giữ phạm vi phần 05 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. NULL khác chuỗi rỗng thế nào?
2. D002 phải giữ bản nào và vì sao?
3. Vì sao kiểm tra số dòng chưa đủ?

## Đọc thêm từ nguồn chính thức

- [Spark SQL NULL semantics](https://spark.apache.org/docs/3.5.7/sql-ref-null-semantics.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
