# Ngày 47 — Dedup và chọn phiên bản đã biết tại cutoff

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Dedup và chọn phiên bản đã biết tại cutoff”. Kết quả cần đạt: Cutoff ngày 2 thấy amount=100; ngày 4 thấy 200.

## Từ mới gắn với bài này

- **Point-in-time selection (chọn phiên bản đã có ở mốc chốt)**.
- **Tie-breaker (tiêu chí phụ để phân thứ tự)**.

## Tình huống và cách hiểu

Cùng event_id có thể được cập nhật nhiều lần. Trước khi tạo feature tại cutoff, chỉ giữ phiên bản đã đến trước cutoff rồi chọn bản mới nhất trong số đó. Nếu chọn bản mới nhất toàn bộ trước rồi lọc, bạn có thể mất bản cũ thực sự đã biết lúc đó.

**Point-in-time selection (chọn phiên bản đã có ở mốc chốt)** dùng available_ts < cutoff. **Tie-breaker (tiêu chí phụ để phân thứ tự)** cần quy tắc rõ khi hai phiên bản có cùng thời gian. Không dùng dropDuplicates để giả định nó sẽ giữ bản mới nhất.

Bài này tạo hai phiên bản E1: ngày 1 biết 100, ngày 3 mới biết 200. Tại ngày 2, feature phải thấy 100. Đây là ví dụ nhỏ để dùng lại trong test chống leakage.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-047/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
versions = spark.createDataFrame([("E1", "2025-01-01", 100), ("E1", "2025-01-03", 200)], "event_id string, available_date string, amount long")
known = versions.filter(F.col("available_date") < "2025-01-02")
window = Window.partitionBy("event_id").orderBy(F.col("available_date").desc(), F.col("amount").desc())
known.withColumn("rn", F.row_number().over(window)).filter("rn = 1").show()
```

## Đọc từng phần của ví dụ

Lọc thông tin được biết trước, sau đó mới đánh số phiên bản. Dữ liệu ngày 3 không có quyền thay quá khứ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Cutoff ngày 2 thấy amount=100; ngày 4 thấy 200.

## Ba câu kiểm tra hiểu bài

1. Point-in-time selection có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: chọn phiên bản đã có ở mốc chốt.
- Luồng chính: Lọc thông tin được biết trước, sau đó mới đánh số phiên bản. Dữ liệu ngày 3 không có quyền thay quá khứ.
- Đối chiếu tiêu chí: Cutoff ngày 2 thấy amount=100; ngày 4 thấy 200. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
