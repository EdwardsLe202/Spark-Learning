# Ngày 23 — Ghép các bước thành một lần làm sạch

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Làm sạch file lỗi nhỏ, đối soát từng bước và giữ nguồn để giải thích.

## 1. Tên mới cho những bước đã làm

**Pipeline (chuỗi bước xử lý có đầu vào và đầu ra)** hôm nay chỉ gồm đọc → chuyển kiểu → tách lỗi → bỏ trùng → kiểm tra mã khách. Các thao tác đã học từng ngày; không cần cài thêm công cụ điều phối.

File orders_dirty.csv có 10 dòng. Amount được đọc string trước, sau đó tạo amount_num bằng cast. Order_date chuyển thành order_day. Hợp lệ cơ bản nghĩa là có customer_id, ngày parse được, amount_num không thiếu và không âm. Khóa khách tồn tại được kiểm tra bằng join sau đó.

## 2. Tách lỗi trước khi bỏ trùng

**Quarantine (vùng giữ bản ghi lỗi để điều tra)** có thể là một DataFrame được lưu riêng cùng lý do. Bài này trước hết tách basic_errors để biết các dòng không đạt điều kiện cơ bản. Sau đó loại bản lặp hoàn toàn trong candidates bằng distinct. Vì O002 lặp giống cả dòng, quy tắc này đủ cho fixture.

Các mã khách không tồn tại được tìm bằng left anti join với customers. Không ghép bừa rồi bỏ mất dấu chúng. Kết quả clean dùng inner join với tập mã khách duy nhất đã kiểm tra.

## 3. Đối soát nhiều bước

10 dòng đầu = 5 lỗi cơ bản + 5 ứng viên. 5 ứng viên = 1 bản lặp + 4 dòng duy nhất. Trong 4 dòng, 1 mã C999 không tồn tại và 3 sạch. Toàn luồng: **10 = 5 + 1 + 1 + 3**. Tổng clean 390000, gồm O001, O002, O015.

Một chương trình ghi được file chưa chắc đã làm đúng. Nếu một bước mất dòng mà không có cách giải thích, thu nhỏ về chính mã đơn ấy. Hôm nay mục tiêu là truy được từng dòng qua chuỗi xử lý.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file.

```python
spark.conf.set("spark.sql.ansi.enabled", "false")
raw = spark.read.option("header", True).schema("order_id string, customer_id string, order_date string, amount string, status string").csv(str(DATA / "orders_dirty.csv"))
parsed = raw.withColumn("amount_num", F.col("amount").cast("long")).withColumn("order_day", F.to_date("order_date", "yyyy-MM-dd"))
valid = F.col("customer_id").isNotNull() & (F.col("customer_id") != "") & F.col("amount_num").isNotNull() & (F.col("amount_num") >= 0) & F.col("order_day").isNotNull()
candidates = parsed.filter(valid)
basic_errors = parsed.filter(~valid)
unique = candidates.distinct()
customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
unknown = unique.join(customers.select("customer_id"), "customer_id", "left_anti")
clean = unique.join(customers.select("customer_id"), "customer_id", "inner")
print("raw/basic_errors/candidates/unique/unknown/clean:", raw.count(), basic_errors.count(), candidates.count(), unique.count(), unknown.count(), clean.count())
clean.select("order_id", "customer_id", "amount_num").show()
```

## Đọc từng phần của ví dụ

- Chuyển kiểu giữ chuỗi gốc để truy lỗi.
- valid là biểu thức các kiểm tra kết hợp; ~ là phủ định điều kiện.
- distinct chỉ sau khi đã hiểu các bản lặp giống nhau.
- Anti join giữ dấu mã lạ; inner join tạo tập sạch cuối.

## Kết quả để đối chiếu

Các số lần lượt 10,5,5,4,1,3; sạch O001/O002/O015, tổng amount_num=390000.

## Từ mới cần nhận ra hôm nay

- **Pipeline (chuỗi bước xử lý có đầu vào và đầu ra)**.
- **Quarantine (vùng giữ bản ghi lỗi để điều tra)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Vì sao giữ amount chuỗi gốc?
2. Unknown customer có nên biến mất không có báo cáo không?
3. Đối soát toàn luồng bằng phương trình nào?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Để truy nguyên lỗi parse.
2. Không, cần tách và giải thích.
3. 10 = 5 lỗi cơ bản + 1 bản lặp + 1 mã lạ + 3 sạch.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
