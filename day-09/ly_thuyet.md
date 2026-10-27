# Ngày 09 — Tạo cột mới bằng withColumn

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Tạo tiền theo nghìn đồng và hiểu biểu thức được áp dụng cho mọi dòng.

## 1. Cột mới để diễn đạt thông tin mới

Bảng giữ amount bằng đồng. Ta muốn thêm amount_k bằng nghìn đồng. **Column expression (biểu thức tính trên cột)** `orders["amount"] / 1000` mô tả phép chia áp dụng cho từng dòng. Nó chưa phải một số tiền duy nhất của một đơn.

`withColumn("amount_k", biểu_thức)` trả DataFrame có thêm cột amount_k. Nếu tên cột đã có, nó tạo kết quả với cột đó được thay. Vì vậy đặt tên mới rõ nghĩa giúp tránh hiểu nhầm đơn vị.

## 2. Giữ nguyên cột gốc

O001 có amount=100000 và amount_k=100.0; O003 có 50000 và 50.0. Tiền không giảm về mặt nghiệp vụ, chỉ đổi đơn vị thể hiện. Kết quả vẫn tám dòng. Không nên đổi tên amount thành amount_vnd nếu thực tế đã chia 1000.

Phép tính này không yêu cầu vòng for hay sửa từng Row bằng Python. Bạn nối phép biến đổi rồi dùng bảng trả về. Kiểu amount_k thường là số có phần thập phân; xem printSchema để xác nhận, không đoán từ cách show in số.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
result = orders.withColumn("amount_k", orders["amount"] / 1000)
result.select("order_id", "amount", "amount_k").show()
result.printSchema()
```

## Đọc từng phần của ví dụ

- Tên cột mới được truyền đầu tiên cho withColumn.
- Biểu thức chia đứng ở tham số thứ hai.
- select chỉ dùng để nhìn ba cột liên quan; không xóa cột trong result đã tạo.

## Kết quả để đối chiếu

8 dòng; O001 amount_k=100.0, O008=400.0; amount nguồn vẫn là long và không đổi.

## Từ mới cần nhận ra hôm nay

- **Column expression (biểu thức tính trên cột)**.
- **withColumn (tạo hoặc thay cột trong bảng kết quả)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Biểu thức cột có phải một số Python đã lấy về không?
2. Bảng có tăng số dòng khi thêm cột không?
3. Vì sao cần tên cột thể hiện đơn vị?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không, nó mô tả phép tính cho cột.
2. Không trong phép biến đổi này.
3. Để người đọc không nhầm đồng với nghìn đồng.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
