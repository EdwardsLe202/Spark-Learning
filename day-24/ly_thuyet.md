# Ngày 24 — Xử lý riêng một ngày dữ liệu

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Viết hàm nhận ngày và ghi đúng đầu ra của ngày đó.

## 1. Từ xử lý toàn bảng sang một ngày

**Batch processing (xử lý một tập dữ liệu hữu hạn theo đợt)** có thể chỉ xử lý đơn của một ngày. **Data interval (khoảng dữ liệu được một lần chạy xử lý)** trong bài là ngày bạn truyền vào hàm. Ngày chạy chương trình thực tế có thể khác ngày đơn hàng.

`run_day("2025-01-03")` nên lấy O002/O003, kể cả bạn chạy nó trong năm 2026. Không dùng ngày hiện tại để chọn dữ liệu khi đang làm lại báo cáo quá khứ.

## 2. Đích riêng cho từng ngày

Hàm lọc nguồn orders độc lập, kiểm tra có dòng rồi ghi vào thư mục `order_date=2025-01-03`. Cấu trúc tên này giúp ta nhìn phạm vi đầu ra; ở đây bạn tự ghi đích từng ngày, chưa học mọi cơ chế partition tự động của storage.

Overwrite chỉ thay đúng thư mục ngày. Nếu ghi đè thư mục daily cha khi chạy ngày thứ hai, ngày đầu có thể mất. Luôn in đường dẫn thực trước khi ghi trong bài làm.

## 3. Hàm có tham số dễ tái chạy

Ta tách logic `run_day(day)` để việc đổi ngày chỉ đổi tham số. Python function đã quen là đủ. Không cần cài scheduler. Việc chạy lại một ngày và xử lý nguồn đến muộn được kiểm tra riêng ở ngày 25.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
target_root = ROOT / "artifacts/beginner/day-24/daily"
def run_day(day):
    part = orders.filter(F.col("order_date") == day)
    if part.count() == 0:
        raise ValueError("Không có dữ liệu ngày " + day)
    target = target_root / ("order_date=" + day)
    print("Ghi:", target)
    part.write.mode("overwrite").parquet(str(target))
run_day("2025-01-01")
run_day("2025-01-03")
print("Đọc cả hai ngày:", spark.read.parquet(str(target_root)).count())
```

## Đọc từng phần của ví dụ

- Hàm dùng ngày tham số, không dùng đồng hồ hiện tại.
- Mỗi ngày có đích riêng và nguồn đọc từ CSV gốc độc lập.
- Ngày 1 có một đơn, ngày 3 có hai; đọc cả hai được ba dòng.

## Kết quả để đối chiếu

Đầu ra hai ngày có 3 đơn, tổng 350000; thư mục ngày 1 vẫn còn sau khi ghi ngày 3.

## Từ mới cần nhận ra hôm nay

- **Batch processing (xử lý một tập dữ liệu hữu hạn theo đợt)**.
- **Data interval (khoảng dữ liệu được một lần chạy xử lý)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Ngày chạy và ngày dữ liệu có luôn giống nhau không?
2. Ghi ngày mới có nên xóa cả daily không?
3. Vì sao nên nhận ngày qua tham số?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không.
2. Không, chỉ thay đích ngày cần xử lý.
3. Để chủ động chạy lại hoặc chạy ngày khác.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
