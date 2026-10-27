# Ngày 20 — Phát hiện join làm nhân tiền

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Kiểm tra khóa và tổng tiền trước sau ghép; dừng khi bảng khách trùng mã.

## 1. Một lỗi dễ bỏ qua

**Unique key (khóa có giá trị duy nhất)** của customers phải là customer_id. **Cardinality (quan hệ số lượng giữa các khóa)** ở bài này là nhiều đơn ứng với một dòng khách. Nếu vô tình có hai dòng C001 trong customers, mỗi đơn C001 khớp cả hai và xuất hiện hai lần sau join.

Nguồn C001 tổng 700000. Nhân bản C001 ở bảng khách làm tổng sau join tăng thêm 700000, thành 2100000 thay vì 1400000. Đây là sai số dù code join không báo lỗi cú pháp và schema vẫn hợp lệ.

## 2. Chặn bằng kiểm tra nhỏ

`unionByName` **(nối dòng theo tên cột)** thêm các dòng của bảng thứ hai vào bảng thứ nhất; nó không tự loại trùng. Ví dụ dùng nó để tạo bảng khách sai có chủ đích.

`customers.groupBy("customer_id").count().filter("count > 1")` tìm khóa lặp. Nếu có, ném ValueError trước khi ghép. Kiểm tra schema thôi chưa bắt được lỗi quan hệ này. Không dùng distinct sau join để che lỗi mà chưa hiểu dòng nào đúng.

## 3. Giữ kiểm tra theo nghiệp vụ

Với join bổ sung tên ở bài này, kỳ vọng số đơn và tổng tiền giữ nguyên. Một loại join khác có thể chủ ý lọc dòng, nên cần ghi yêu cầu thay vì áp mọi phép đối soát một cách máy móc. Hôm nay chỉ dùng trường hợp đã hiểu để học nhận diện lỗi.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
customers = spark.read.option("header", True).schema("customer_id string, name string, region string").csv(str(DATA / "customers.csv"))
bad_customers = customers.unionByName(customers.filter(F.col("customer_id") == "C001"))
wrong = orders.join(bad_customers, "customer_id", "inner")
print("Số dòng sai:", wrong.count())
print("Tổng sai:", wrong.agg(F.sum("amount")).first()[0])
bad_customers.groupBy("customer_id").count().filter("count > 1").show()
```

## Đọc từng phần của ví dụ

- unionByName nối thêm một bản C001 để cố ý tạo lỗi.
- C001 có ba đơn, nên joined tăng từ 8 lên 11 dòng.
- Truy vấn khóa trùng chỉ ra C001 xuất hiện hai lần.

## Kết quả để đối chiếu

Ví dụ sai có 11 dòng, tổng 2100000; bảng khóa trùng có C001/count=2.

## Từ mới cần nhận ra hôm nay

- **Unique key (khóa có giá trị duy nhất)**.
- **Cardinality (quan hệ số lượng giữa các khóa)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Vì sao tên/kiểu cột đúng mà tiền sai?
2. Hai dòng C001 bên phải gây gì?
3. Distinct sau join có thay kiểm tra khóa không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Sai số lượng quan hệ, không sai schema.
2. Mỗi đơn C001 khớp hai lần.
3. Không.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
