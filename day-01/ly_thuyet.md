# Ngày 01 — Đọc một bảng và hiểu Spark dùng để làm gì

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Nhìn bảng ba đơn hàng, cộng đúng số tiền và nói được vai trò cơ bản của Spark.

## 1. Bắt đầu từ ba đơn hàng

Một cửa hàng ghi lại các đơn đã bán. Đây là **table (bảng dữ liệu)**, giống một vùng có hàng và cột trong Excel:

| order_id | customer_id | amount |
| --- | --- | ---: |
| O001 | C001 | 100000 |
| O002 | C001 | 200000 |
| O003 | C002 | 50000 |

`order_id` nghĩa là mã đơn; `customer_id` là mã khách hàng; `amount` là số tiền, tính bằng đồng Việt Nam. O001, C001 là mã giả lập để học, không phải cú pháp Spark cần học thuộc.

**Row (dòng dữ liệu)** mô tả một đơn hàng. Dòng đầu cho biết khách C001 có đơn O001 trị giá 100.000 đồng. **Column (cột dữ liệu)** mô tả một loại thông tin. Cột amount chứa số tiền của tất cả các đơn. Khách C001 xuất hiện hai lần vì họ có hai đơn; việc đó chưa phải lỗi trùng đơn.

Dừng đọc ở đây và tự trả lời: bảng có mấy đơn? Có mấy khách khác nhau? Đáp án là 3 đơn, 2 khách. Nếu bạn đếm 3 khách, hãy đối chiếu lại hai dòng có cùng C001.

## 2. Ta muốn làm gì với bảng?

Câu hỏi thứ nhất: cửa hàng đã bán bao nhiêu tiền? Cộng ba số: 100.000 + 200.000 + 50.000 = **350.000 đồng**.

Câu hỏi thứ hai: khách C001 mua bao nhiêu? Giữ hai dòng có customer_id bằng C001, rồi cộng amount: **300.000 đồng**. Bạn vừa làm hai thao tác thường gặp: chọn các dòng phù hợp và cộng số tiền. Hôm nay chỉ cần hiểu ý nghĩa, chưa cần nhớ tên lệnh.

Ở ngày 02 bạn làm hai việc này bằng Python quen thuộc. Ở các ngày tiếp theo, bạn dùng Spark để diễn đạt cùng câu hỏi. Bài toán được giữ nguyên để bạn nhìn ra công cụ mới thay đổi cách viết như thế nào.

## 3. Spark đứng ở đâu?

**Apache Spark (bộ máy xử lý dữ liệu)** là phần mềm nhận những yêu cầu như đọc bảng, chọn dòng, tính tổng rồi thực hiện chúng. Khi cần, Spark có thể chia công việc cho nhiều máy phối hợp. Trước mắt chúng ta chạy trên một máy của bạn; chưa cần học cách cấu hình nhiều máy.

Ví dụ gần gũi: file chứa đơn hàng giống cuốn sổ; Spark giống người đọc sổ và tính theo yêu cầu. Cuốn sổ giữ thông tin, người tính xử lý thông tin. File và Spark có vai trò khác nhau.

Với ba dòng trên, bạn cộng tay rất dễ và chưa cần Spark. Dữ liệu nhỏ được dùng để kiểm tra rằng bạn hiểu kết quả. Sau khi biết viết phép xử lý đúng, ta mới tìm hiểu cách Spark chia công việc và khi nào điều đó có ích. Bạn chưa cần lựa chọn Spark hay công cụ khác cho một hệ thống thật trong ngày này.

## 4. Học thế nào là đủ hôm nay?

Bạn chưa cần cài phần mềm, đọc file dữ liệu dài, vẽ kiến trúc hay huấn luyện mô hình. Chỉ cần giải thích được mỗi dòng/cột có ý nghĩa gì và tự tính được hai kết quả. Từ vựng ở cuối bài là để tra lại, không phải bài học thuộc.

Nếu gặp câu chưa hiểu, quay lại đúng bảng ba dòng và chỉ vào dữ liệu cụ thể. Ví dụ câu hỏi “khách xuất hiện hai lần” dễ hiểu hơn khi bạn chỉ vào hai mã C001.

## Ví dụ có thể chạy nguyên file

Ví dụ hôm nay dùng Python thông thường; ngày 01 có thể làm hoàn toàn trên giấy.

```python
print("order_id | customer_id | amount")
print("O001     | C001        | 100000")
print("O002     | C001        | 200000")
print("O003     | C002        | 50000")
print("Tổng ba đơn:", 100000 + 200000 + 50000)
```

## Đọc từng phần của ví dụ

- Ba lệnh print giữa in lại ba dòng bảng để bạn đối chiếu.
- Dòng cuối cộng ba số đã có trong bảng. Chưa có lệnh Spark nào.
- Chạy code chỉ là lựa chọn bổ sung; bạn hoàn thành bài bằng giấy hoặc ghi chú vẫn được.

## Kết quả để đối chiếu

Bảng có 3 dòng dữ liệu, 3 cột; 2 mã khách khác nhau. Tổng tiền 350000; riêng C001 là 300000.

## Từ mới cần nhận ra hôm nay

- **Row (dòng dữ liệu)**.
- **Column (cột dữ liệu)**.
- **Apache Spark (bộ máy xử lý dữ liệu)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Một dòng ở bảng này là một đơn hay một khách?
2. Vì sao C001 xuất hiện hai lần?
3. Spark giúp xử lý dữ liệu như thế nào trong ví dụ?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Một đơn hàng.
2. C001 có hai đơn khác nhau.
3. Nhận yêu cầu xử lý bảng, chẳng hạn chọn đơn của C001 rồi tính tổng.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
