# Ngày 14 — Ôn tập lần một bằng báo cáo đơn hàng

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Tự kết hợp đọc, lọc, tổng hợp và kiểm tra số liệu mà không thêm API mới.

## 1. Ngày ôn tập, không chạy thêm công nghệ

Bạn đã đọc file, chọn cột, lọc dòng, thêm cột và tổng hợp. Hôm nay ghép chúng thành báo cáo doanh thu hoàn tất theo khách. Đầu vào vẫn orders.csv tám dòng; không cần xử lý file dirty trong bài chính.

Viết kế hoạch bằng lời: đọc tám đơn → giữ completed → nhóm customer_id → cộng tiền, đếm đơn → kiểm tra. Mỗi bước dùng kiến thức đã học. Nếu chưa viết được một bước, quay lại ngày tương ứng thay vì tìm một thư viện mới.

## 2. Đối soát để biết báo cáo có hợp lý

**Reconciliation (đối soát các số liệu liên quan)** ở đây là kiểm tra 8 đơn đầu vào bằng 7 completed + 1 cancelled; tổng 1400000 bằng 1100000 completed + 300000 cancelled. Báo cáo theo khách cũng phải cộng về 1100000.

`assert điều_kiện` của Python báo lỗi nếu điều kiện sai. Với kết quả nhỏ, bạn có thể dùng nó kiểm tra count hoặc giá trị tổng đã lấy về. Chỉ dùng first trên bảng tổng một dòng, không gom toàn bộ nguồn lớn.

## 3. Giải thích quan trọng hơn chép mẫu

Tự chỉ ra vì sao filter phải trước groupBy, vì sao kết quả có bốn dòng và một dòng biểu thị một khách. Nếu chương trình chạy nhưng vẫn cộng đơn hủy, nó sai yêu cầu dù không có lỗi cú pháp. Đây là lúc sửa hiểu biết trước khi học phần ghép bảng.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
completed = orders.filter(F.col("status") == "completed")
summary = completed.groupBy("customer_id").agg(F.sum("amount").alias("total_amount"), F.count("*").alias("order_count"))
summary.show()
assert orders.count() == 8
assert completed.count() == 7
assert summary.agg(F.sum("total_amount")).first()[0] == 1100000
print("Đã đối soát ví dụ.")
```

## Đọc từng phần của ví dụ

- Đây là các bước đã học, chỉ ghép thành một luồng ngắn.
- agg cuối tạo một dòng tổng của báo cáo, first lấy đúng dòng đó.
- assert kiểm tra các kỳ vọng đã tính tay; nó không tự thiết kế quy tắc thay bạn.

## Kết quả để đối chiếu

Báo cáo 4 khách, tổng 1100000; đối soát số đơn 8=7+1 và tổng tiền 1400000=1100000+300000.

## Từ mới cần nhận ra hôm nay

- **Reconciliation (đối soát các số liệu liên quan)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Bỏ filter sai nghiệp vụ dù code vẫn chạy ra sao?
2. Một dòng summary là gì?
3. Nếu assert sai thì có nên đổi số kỳ vọng để chạy qua không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Nó cộng cả đơn hủy thành 1400000.
2. Một khách hàng có đơn hoàn tất.
3. Không; kiểm tra dữ liệu và logic trước.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
