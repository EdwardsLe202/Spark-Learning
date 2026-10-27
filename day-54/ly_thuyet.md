# Ngày 54 — Cửa sổ streaming và output mode

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Cửa sổ streaming và output mode”. Kết quả cần đạt: Hai cửa sổ có tổng 3 và 3; stream chỉ nghiệm thu sau khi đã quan sát đóng cửa sổ.

## Từ mới gắn với bài này

- **Append / Update / Complete (ghi dòng hoàn tất / cập nhật / toàn kết quả)**.

## Tình huống và cách hiểu

Cửa sổ thời gian gom sự kiện theo khoảng như [10:00,10:05). Nó khác cửa sổ theo vị trí dòng đã học. Khi có dữ liệu trễ, tổng có thể còn thay đổi và state phải được giữ cho tới giới hạn đã chọn.

**Append / update / complete (ghi dòng hoàn tất / cập nhật / toàn kết quả)** mô tả cách query xuất kết quả, không đồng nghĩa ba mode ghi file batch. Sink và phép toán chỉ hỗ trợ một số tổ hợp; Parquet file sink không tự nhận mọi update aggregation.

Bài bắt đầu với kết quả batch để tính tay các cửa sổ, rồi chuyển sang query watermark ngày 53. Memory sink có thể dùng quan sát nhưng không dùng chứng minh phục hồi bền vững. Luôn kiểm tra matrix hỗ trợ trong tài liệu đúng Spark 3.5.7.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-054/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
df = spark.createDataFrame([("2025-01-01T10:00:00Z", 1), ("2025-01-01T10:04:00Z", 2), ("2025-01-01T10:05:00Z", 3)], "time string, value long").withColumn("ts", F.to_timestamp("time"))
df.groupBy(F.window("ts", "5 minutes")).agg(F.sum("value").alias("total")).orderBy("window").show(truncate=False)
```

## Đọc từng phần của ví dụ

10:05 thuộc cửa sổ kế tiếp vì biên phải loại trừ. Tổng batch là mốc đối chiếu trước khi thử stream.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Hai cửa sổ có tổng 3 và 3; stream chỉ nghiệm thu sau khi đã quan sát đóng cửa sổ.

## Ba câu kiểm tra hiểu bài

1. Append / Update / Complete có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: ghi dòng hoàn tất / cập nhật / toàn kết quả.
- Luồng chính: 10:05 thuộc cửa sổ kế tiếp vì biên phải loại trừ. Tổng batch là mốc đối chiếu trước khi thử stream.
- Đối chiếu tiêu chí: Hai cửa sổ có tổng 3 và 3; stream chỉ nghiệm thu sau khi đã quan sát đóng cửa sổ. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 10 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
