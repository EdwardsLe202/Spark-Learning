# Ngày 12 — Nhận diện dòng trùng

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Dùng distinct/dropDuplicates và hiểu cần định nghĩa trùng theo gì.

## 1. Hai lần xuất hiện có thể là lỗi hoặc bình thường

**Key (khóa nhận diện bản ghi)** trong bảng đơn là order_id. C001 mua hai đơn khác nhau không phải trùng đơn. **Duplicate (bản ghi trùng theo quy tắc)** cần nói rõ trùng cả dòng hay trùng mã đơn. Hôm nay thử ba dòng: O001=100000, O001=100000 lần nữa và O002=200000.

`distinct()` giữ những dòng khác nhau khi so tất cả cột. Hai O001 giống toàn bộ nên còn một; O002 giữ nguyên. Tổng từ 400000 trở về 300000 nếu bản O001 thứ hai thực sự là ghi lặp.

## 2. Khóa trùng nhưng nội dung khác

`dropDuplicates(["order_id"])` giữ một dòng cho mỗi mã. Nếu hai phiên bản O001 có tiền khác nhau, lệnh này không hứa chọn bản mới nhất. Chúng ta chưa dùng nó để quyết định dữ liệu phiên bản; ngày 21 mới học cách chọn theo thứ tự rõ ràng.

Vì vậy, bài này chỉ tự loại bản lặp giống toàn dòng. Khi thấy cùng mã nhưng dữ liệu khác, đánh dấu cần quy tắc thay vì chọn đại. Distinct không phải thuốc chữa mọi lỗi dữ liệu.

## 3. Kiểm tra trước sau

Ghi số dòng trước, sau và tổng tiền. Nếu số dòng giảm mà không giải thích được dòng nào đã bị bỏ, bạn chưa đủ bằng chứng rằng làm sạch đúng. Viết quy tắc bằng lời trước khi gọi hàm.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file.

```python
orders = spark.createDataFrame([("O001", 100000), ("O001", 100000), ("O002", 200000)], "order_id string, amount long")
clean = orders.distinct()
print("Trước:", orders.count(), "Sau:", clean.count())
clean.agg(F.sum("amount").alias("total")).show()
```

## Đọc từng phần của ví dụ

- Hai tuple đầu giống toàn bộ nên distinct gộp lại.
- Trước có 3 dòng; sau 2; tổng sạch 300000.
- Đây là bảng nhỏ riêng, chưa phải bài làm sạch toàn file dirty.

## Kết quả để đối chiếu

Trước 3, sau 2, tổng 300000. Không tuyên bố dropDuplicates theo khóa luôn chọn đúng phiên bản.

## Từ mới cần nhận ra hôm nay

- **Duplicate (bản ghi trùng theo quy tắc)**.
- **Distinct (giữ các dòng khác nhau)**.
- **Key (khóa nhận diện bản ghi)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Hai đơn cùng customer_id có trùng order_id không?
2. Distinct xét cột nào?
3. DropDuplicates theo khóa có bảo đảm giữ bản mới nhất không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không nhất thiết.
2. Tất cả cột đang có.
3. Không.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
