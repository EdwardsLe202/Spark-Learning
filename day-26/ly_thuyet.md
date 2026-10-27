# Ngày 26 — Vì sao Spark chưa tính ngay?

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Liên hệ transformation/action với các lệnh đã dùng và đọc plan cơ bản.

## 1. Đặt tên cho điều đã thực hành

Bạn đã dùng filter, select, groupBy nhiều lần. **Transformation (phép tạo kế hoạch biến đổi)** thường mô tả DataFrame mới mà chưa tính toàn bộ dữ liệu ngay. **Action (thao tác yêu cầu kết quả)** như show, count hoặc ghi file yêu cầu Spark thực hiện phần tính cần thiết.

**Lazy evaluation (thực thi trì hoãn)** nghĩa là Spark có thể gom các phép biến đổi thành kế hoạch trước khi chạy. Ví dụ giữ completed rồi chỉ lấy customer_id/amount cho phép bộ máy biết yêu cầu cuối cùng. Một số việc như đọc metadata vẫn có thể xảy ra sớm; đừng hiểu là Spark không làm bất cứ việc gì trước action.

## 2. Xem kế hoạch của một phép tính quen

`result.explain()` in **execution plan (kế hoạch thực thi)**. Trước tiên chỉ tìm tên liên quan: Scan đọc nguồn, Filter lọc, Aggregate tổng hợp, Exchange trao đổi dữ liệu giữa phần xử lý. Chưa cần giải thích mọi mã số trong plan.

Một lần count/show có thể tạo công việc thực thi; số job/stage phụ thuộc kế hoạch và môi trường. Bài này không bắt bạn đoán số cố định cho mọi truy vấn. Spark UI là công cụ xem thực thi, chỉ mở khi phiên còn sống; có thể để phần đó là bài bổ sung.

## 3. Vì sao học kiến trúc ở đây?

Bạn đã có phép tính cụ thể để nhìn, nên khái niệm mới gắn vào trải nghiệm thay vì học thuộc sơ đồ. Cấu trúc driver/executor/cluster được để ở phần đọc tiếp sau nền tảng, không cản việc viết báo cáo đúng hôm nay.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
filtered = orders.filter(F.col("status") == "completed")
result = filtered.groupBy("customer_id").agg(F.sum("amount").alias("total"))
print("Kế hoạch:")
result.explain()
print("Bây giờ yêu cầu hiển thị kết quả:")
result.show()
```

## Đọc từng phần của ví dụ

- Hai dòng đầu xây chuỗi yêu cầu lọc và nhóm.
- explain hiển thị cách Spark dự định làm; show yêu cầu kết quả hiển thị.
- Kết quả tiền vẫn như ngày 10; kiến thức mới là cách hiểu thực thi.

## Kết quả để đối chiếu

Có kế hoạch và báo cáo bốn khách tổng 1100000; không yêu cầu số job/stage cố định.

## Từ mới cần nhận ra hôm nay

- **Transformation (phép tạo kế hoạch biến đổi)**.
- **Action (thao tác yêu cầu kết quả)**.
- **Lazy evaluation (thực thi trì hoãn)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Filter có luôn tính xong mọi dòng ngay không?
2. Show thuộc nhóm nào?
3. Explain có tự sửa dữ liệu nguồn không?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Thường chỉ bổ sung kế hoạch, việc cần thiết chạy khi action yêu cầu.
2. Action.
3. Không.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
