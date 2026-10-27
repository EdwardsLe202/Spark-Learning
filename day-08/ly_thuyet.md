# Ngày 08 — Lọc các đơn cần tính

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Dùng filter với một hoặc hai điều kiện và kiểm tra các giá trị biên.

## 1. Câu hỏi trước, biểu thức sau

Ta muốn xem đơn đã hoàn tất. **Condition (điều kiện giữ dòng)** là status bằng completed. `orders.filter(orders["status"] == "completed")` tạo bảng chỉ giữ các dòng có điều kiện đúng. O004 bị hủy nên không còn trong kết quả, các đơn khác vẫn giữ.

So với vòng for ngày 02, bạn vẫn diễn tả điều kiện nhưng không tự duyệt từng dòng Python. `orders["status"]` là cột; `"completed"` là giá trị chuỗi dùng so sánh. Hai dấu `==` kiểm tra bằng nhau; một dấu `=` dùng gán biến ở Python.

## 2. Ghép hai điều kiện

Muốn đơn vừa hoàn tất vừa có tiền từ 150000 trở lên, dùng `(điều kiện 1) & (điều kiện 2)`. Dấu & kết hợp biểu thức cột; `and` của Python không dùng theo cách này cho cột Spark. Mỗi vế cần ngoặc vì thứ tự ưu tiên toán tử có thể làm câu lệnh hiểu khác ý bạn.

`>= 150000` giữ cả đúng 150000, còn `> 150000` loại giá trị ấy. Hãy tìm O005 trong nguồn để kiểm tra sự khác biệt này bằng dòng thật thay vì chỉ nhớ công thức.

## 3. Đọc kết quả theo mã đơn

Chưa có orderBy nên đừng dựa vào vị trí dòng để kết luận đúng sai. So tập mã đơn, số lượng và từng giá trị. Bài này không tính tổng; hãy chắc chắn biết chính xác những đơn nào còn lại trước khi tổng hợp ở ngày 10.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
result = orders.filter((orders["status"] == "completed") & (orders["amount"] >= 150000))
result.select("order_id", "amount", "status").show()
print("Số đơn phù hợp:", result.count())
```

## Đọc từng phần của ví dụ

- Vế đầu loại đơn cancelled; vế sau chọn mức tiền.
- Dấu & yêu cầu cả hai vế đúng.
- Có 3 đơn: O002=200000, O005=150000, O008=400000.

## Kết quả để đối chiếu

Ví dụ giữ O002, O005, O008. Nếu chỉ lọc completed thì có 7 đơn.

## Từ mới cần nhận ra hôm nay

- **Condition (điều kiện giữ dòng)**.
- **Filter (lọc dòng)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Vì sao không dùng and?
2. >= và > khác nhau ở dòng nào?
3. Lọc có sửa bảng orders không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Đây là biểu thức cột Spark, cần & và ngoặc từng vế.
2. O005 có amount đúng 150000.
3. Không; dùng DataFrame kết quả.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
