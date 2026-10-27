# Ngày 06 — Đọc file CSV tám đơn hàng

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Đọc một CSV thật, kiểm tra header, số dòng và schema.

## 1. Từ dữ liệu viết trong code sang file

**CSV — Comma-Separated Values (tệp văn bản có các trường phân cách bằng dấu phẩy)** lưu bảng dưới dạng văn bản. File hôm nay nằm ở `data/beginner/orders.csv`, có tám đơn hàng. **Header (dòng tên cột)** là dòng đầu: order_id,customer_id,order_date,amount,status. Header không phải một đơn.

Ba cột đầu đã quen: mã đơn, mã khách, số tiền. Ta thêm order_date là ngày đặt đơn dạng năm-tháng-ngày và status là trạng thái. completed nghĩa là hoàn tất; cancelled nghĩa là đã hủy. Từ ngày 08, ta sẽ chỉ tính các đơn completed cho báo cáo doanh thu.

## 2. Đọc chuỗi lệnh từ trái sang phải

Trong file mẫu, `spark.read` chọn bộ đọc, `.option("header", True)` nói có dòng tên cột, `.schema(...)` dùng cấu trúc đã học hôm qua, `.csv(str(path))` đọc nguồn CSV tại đường dẫn. Giá trị amount được đọc thành long theo schema; order_date tạm là string tới ngày 15.

**Path (đường dẫn tệp)** chỉ vị trí file. Phần `ROOT / "data" / "beginner" / "orders.csv"` ghép đường dẫn bằng thư viện pathlib của Python. File mẫu xác định ROOT từ vị trí của chính file nên không lệ thuộc đường dẫn cá nhân. Bạn chưa cần tự viết tiện ích đọc file.

## 3. Luôn kiểm tra sau khi đọc

Chạy show để xem tên và giá trị, printSchema để xem kiểu, count để biết số đơn. Nếu count=9 thay vì 8, hãy kiểm tra header. Nếu amount là string thay long, kiểm tra schema bạn thực sự truyền. Không sửa file gốc để làm kết quả trông đúng; sửa code hoặc tạo bản thử khác.

Từ hôm nay, phần đọc bảng orders được chuẩn bị sẵn trong hai file Python. Bạn tập trung vào các dòng trong vùng bài học, nhưng vẫn có thể đọc toàn bộ phần mở phiên và đọc CSV.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
orders.show(truncate=False)
orders.printSchema()
print("Số đơn:", orders.count())
```

## Đọc từng phần của ví dụ

- orders được đọc từ CSV ở phần đầu vi_du.py bằng schema tường minh.
- truncate=False giúp xem đầy đủ chuỗi ngắn trong bảng.
- count không tính header vì bộ đọc đã nhận header=True.

## Kết quả để đối chiếu

8 đơn, 5 cột. amount là long; order_date vẫn là string; O004 có status=cancelled.

## Từ mới cần nhận ra hôm nay

- **CSV — Comma-Separated Values (tệp văn bản có các trường phân cách bằng dấu phẩy)**.
- **Header (dòng tên cột)**.
- **Path (đường dẫn tệp)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Header có phải một đơn hàng không?
2. option header=True làm gì?
3. order_date hiện là string hay date?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không.
2. Dùng dòng đầu làm tên cột.
3. String; học chuyển thành date ở ngày 15.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
