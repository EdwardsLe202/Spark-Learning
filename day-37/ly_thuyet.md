# Ngày 37 — Nhận diện data skew spill và OOM

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Nhận diện data skew spill và OOM”. Kết quả cần đạt: Key 0=9100; key 1–9 mỗi key=100; không cần gây OOM.

## Từ mới gắn với bài này

- **Data skew (dữ liệu lệch khóa)**.
- **Spill (tràn dữ liệu tạm ra đĩa)**.
- **OOM — Out of memory (hết bộ nhớ)**.

## Tình huống và cách hiểu

**Data skew (dữ liệu lệch khóa)** làm một nhóm hoặc task nhận phần việc lớn hơn hẳn các phần còn lại. Tăng tổng số partition chưa chắc chữa được một khóa cực phổ biến. **Spill (tràn dữ liệu tạm ra đĩa)** và **OOM — Out of memory (hết bộ nhớ)** là hai hiện tượng khác nhau.

OOM ở driver có thể do collect/toPandas lớn; phía thực thi có thể thiếu bộ nhớ cho join, sort hoặc nhóm. Đọc log và UI để xác định nơi lỗi trước khi tăng bộ nhớ. Không cố làm máy hết RAM để chứng minh đã học.

Ví dụ tạo 10000 dòng với 90% cùng một khóa. Đây là dữ liệu lệch để quan sát; nó chưa bảo đảm gây spill trên máy bạn. Ghi phần đã thấy và phần mới chỉ là giả thuyết.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-037/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
df = spark.range(10000).withColumn("key", F.when(F.col("id") < 9000, F.lit(0)).otherwise(F.col("id") % 10))
df.groupBy("key").count().orderBy(F.desc("count")).show()
print("Không cố tạo OOM; xem phân bố trước khi thay tài nguyên.")
```

## Đọc từng phần của ví dụ

Key 0 nhận 9000 dòng đầu và thêm 100 dòng ở phần còn lại; các key khác 100 dòng.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Key 0=9100; key 1–9 mỗi key=100; không cần gây OOM.

## Ba câu kiểm tra hiểu bài

1. Data skew có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: dữ liệu lệch khóa.
- Luồng chính: Key 0 nhận 9000 dòng đầu và thêm 100 dòng ở phần còn lại; các key khác 100 dòng.
- Đối chiếu tiêu chí: Key 0=9100; key 1–9 mỗi key=100; không cần gây OOM. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 09 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).

## EDA nhỏ trước khi tối ưu

**EDA — Exploratory Data Analysis (phân tích khám phá dữ liệu)** gồm tần suất, thiếu và phân vị. **Approximate quantile (phân vị xấp xỉ)** đổi độ chính xác thứ hạng lấy chi phí; không diễn giải relativeError như phần trăm sai số giá trị. Chỉ lấy mẫu/tổng hợp vừa RAM để vẽ, không collect nguồn lớn.

```python
orders.agg(F.mean("amount").alias("mean"), F.min("amount").alias("min"), F.max("amount").alias("max")).show()
print(orders.stat.approxQuantile("amount", [0.5, 0.9], 0.01))
orders.sample(fraction=0.5, seed=42).show()
```

Sample fraction là xác suất chọn gần đúng, không hứa đúng một nửa số dòng. Ghi seed, nguồn/partition và phiên bản nếu so kết quả.
