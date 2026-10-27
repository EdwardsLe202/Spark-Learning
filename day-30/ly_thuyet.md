# Ngày 30 — Tự làm lại và quyết định học tiếp

[Trang ngày](README.md) · [Sang thực hành sau khi đọc](thuc_hanh.md)

**Mục tiêu nhỏ:** Tự giải ba bài tổng hợp và xác định lỗ hổng trước khi sang Machine Learning.

## 1. Tự kiểm tra thay vì chỉ xem đã đọc đủ ngày

**Self-assessment (tự đánh giá bằng hành vi và kết quả)** hôm nay dùng bài mới trên dữ liệu đã quen. Bạn được tra tên hàm, nhưng nên tự viết thứ tự xử lý và giải thích vì sao chọn nó. Không cần thuộc chính xác mọi phương thức.

Ba bài kiểm tra: lọc và tính tổng; ghép đủ khách; chọn dòng mới nhất. Nếu mắc một mảng, có ngày quay lại rõ ràng: filter/groupBy ở 08–10, join ở 18–20, window ở 21–22. Dành buổi này lấp chỗ thiếu thay vì vội cài công nghệ mới.

## 2. Kết quả nào chứng minh đã có nền?

Bạn có thể tạo/đọc DataFrame, xem schema, giữ/lọc/tính cột, tổng hợp, xử lý NULL và trùng, ghép không nhân tiền, chọn dòng theo thứ tự, ghi/đọc file và kiểm tra chạy lại. Bạn cũng giải thích được sơ bộ khi Spark thực thi và dữ liệu được chia thế nào.

Đó là nền để học xử lý dữ liệu bằng Spark; chưa có nghĩa vận hành cluster hay triển khai hệ thống AI production. Kỹ năng sâu lên khi bạn làm dữ liệu lớn hơn và đo ở môi trường thật, với thời gian riêng.

## 3. Học tiếp theo lỗ hổng thực tế

Đọc docs/HOC_TIEP.md sau khi đã làm ba bài. Machine Learning và MLOps cần hiểu feature, nhãn, chia tập và đánh giá; RAG cần thêm nền model, API và truy xuất. Bản tổng hợp cũ được giữ để tra chủ đề, không ép bạn học tất cả trong 30 ngày đầu.

Nếu chưa xong ngày 30 theo lịch, vẫn ghi trung thực số bài đã tự làm. Tiến độ nên phản ánh điều bạn làm được, không chỉ số thư mục đã mở.

## Ví dụ có thể chạy nguyên file

Đoạn dưới là phần chính bên trong phiên Spark. [vi_du.py](vi_du.py) có đủ import, mở phiên, dữ liệu và stop để chạy nguyên file. Bảng orders đọc từ [orders.csv](../data/beginner/orders.csv) tám dòng, được giải thích ở ngày 06.

```python
completed = orders.filter(F.col("status") == "completed")
assert orders.count() == 8
assert completed.count() == 7
assert completed.agg(F.sum("amount")).first()[0] == 1100000
print("Ví dụ kiểm tra dữ liệu nền đã khớp. Ba bài cuối vẫn cần bạn tự viết.")
```

## Đọc từng phần của ví dụ

- Đây chỉ là kiểm tra dữ liệu cơ bản, không giải thay ba bài kiểm tra cuối.
- Assert không đo mức hiểu bài; bạn còn phải tự viết và giải thích.
- Cả ba bài dùng nguồn đã biết, nên không mất công học dataset mới.

## Kết quả để đối chiếu

Bài A: 3 đơn/750000. Bài B: 5 khách, C005=0, tổng 1100000. Bài C: O008/O005/O006/O007.

## Từ mới cần nhận ra hôm nay

- **Self-assessment (tự đánh giá bằng hành vi và kết quả)**.

Chỉ cần gắn từ với ví dụ trong bài. Chưa cần học thuộc cả [bảng thuật ngữ](../docs/THUAT_NGU.md).

## Ba câu kiểm tra hiểu bài

1. Có thể tra hàm mà vẫn tự làm được không?
2. Hoàn thành nền Spark có đồng nghĩa đã học MLOps/AI chưa?
3. Nên quay lại đâu nếu join làm tăng tiền?

<details>
<summary>Mở sau khi đã tự trả lời</summary>

1. Có, điều cần tự hiểu là bài toán, thứ tự và kiểm tra.
2. Chưa; các chặng đó học tiếp có điều kiện.
3. Ngày 18–20, đặc biệt kiểm tra khóa ngày 20.

</details>

**Dừng ở đây nếu vẫn chưa rõ đầu vào và kết quả; chưa cần mở ngày sau.** Khi đã hiểu, sang [thực hành](thuc_hanh.md).
