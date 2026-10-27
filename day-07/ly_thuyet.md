# Ngày 07 — Chọn cột và đặt tên cho kết quả

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Dùng select và alias để tạo bảng chỉ chứa thông tin cần xem.

## 1. Chọn cột khác chọn dòng

**Select (chọn cột)** trả một bảng với các cột được yêu cầu. `orders.select("order_id", "amount")` giữ hai cột và vẫn có tám đơn. Thao tác này chưa loại đơn bị hủy hay lọc số tiền; các việc đó là chọn dòng ở ngày 08.

Tên trong dấu ngoặc kép như "amount" là tên cột. `orders["amount"]` tạo đối tượng đại diện cho cột để gọi thêm phương thức. Đừng nhầm nó với một số tiền duy nhất đã được lấy ra Python.

## 2. Đặt tên dễ hiểu

**Alias (tên thay thế trong kết quả)** đặt tên mới cho một cột đang chọn: `orders["amount"].alias("amount_vnd")`. Tên mới nói rõ đơn vị đồng Việt Nam. Nó không đổi giá trị và không tự đổi mọi bảng từng được tạo.

Spark trả một DataFrame kết quả. `result = orders.select(...)` giữ kết quả trong biến result; orders vẫn có năm cột như ban đầu. Nếu chỉ gọi select mà sau đó lại show orders, bạn sẽ xem bảng nguồn, dễ tưởng lệnh không hoạt động.

## 3. Thói quen kiểm tra

Sau một phép chọn cột, in `result.columns` và `result.count()`. Kỳ vọng tên cột đổi đúng yêu cầu, số đơn vẫn 8. Số dòng có thay đổi hay không là một cách nhanh để tự hỏi mình đang dùng đúng thao tác chưa.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
result = orders.select("order_id", orders["amount"].alias("amount_vnd"))
result.show()
print("Cột kết quả:", result.columns)
print("Cột nguồn:", orders.columns)
```

## Đọc từng phần của ví dụ

- select nhận tên cột order_id và biểu thức cột amount có tên mới.
- result là bảng mới chỉ hai cột.
- orders giữ nguyên cấu trúc năm cột, không bị sửa tại chỗ.

## Kết quả để đối chiếu

result có order_id, amount_vnd và 8 dòng; orders vẫn có 5 cột.

## Từ mới cần nhận ra hôm nay

- **Select (chọn cột)**.
- **Alias (tên thay thế trong kết quả)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. select có loại đơn bị hủy không?
2. alias có đổi số tiền không?
3. Vì sao phải dùng result sau khi gán?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Không, nó chọn cột.
2. Không, chỉ đặt tên.
3. result là DataFrame đã biến đổi; orders vẫn là nguồn.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
