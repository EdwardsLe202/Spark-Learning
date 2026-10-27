# Ngày 39 — AQE và đo kế hoạch sau thực thi

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “AQE và đo kế hoạch sau thực thi”. Kết quả cần đạt: Hai nhánh cùng tổng 1400000, cấu hình được khôi phục.

## Từ mới gắn với bài này

- **AQE — Adaptive Query Execution (điều chỉnh kế hoạch khi chạy)**.

## Tình huống và cách hiểu

**AQE — Adaptive Query Execution (điều chỉnh kế hoạch khi chạy)** dùng thông tin runtime để thay một số lựa chọn, chẳng hạn gộp partition sau shuffle. Vì vậy số phần cuối có thể khác cấu hình spark.sql.shuffle.partitions.

Bật/tắt AQE là một thí nghiệm có kiểm soát, không phải cách sửa mọi truy vấn chậm. Khi so, giữ dữ liệu và action giống nhau. Explain trước action có thể chưa là kế hoạch cuối; quan sát sau khi truy vấn đã chạy và UI để hiểu điều gì đổi.

Bảng nhỏ thường chịu chi phí khởi động và lập lịch. Bạn cần chứng minh kết quả không đổi trước khi thảo luận vài phần giây khác nhau. Ghi lại giá trị cấu hình cũ và khôi phục ở cuối.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-039/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
old = spark.conf.get("spark.sql.adaptive.enabled")
try:
    for enabled in ["false", "true"]:
        spark.conf.set("spark.sql.adaptive.enabled", enabled)
        result = orders.groupBy("customer_id").agg(F.sum("amount").alias("total"))
        result.collect()  # chỉ 4 dòng kết quả
        print("AQE:", enabled)
        result.explain("formatted")
finally:
    spark.conf.set("spark.sql.adaptive.enabled", old)
```

## Đọc từng phần của ví dụ

Chỉ collect kết quả bốn khách. finally trả cấu hình về giá trị ban đầu.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Hai nhánh cùng tổng 1400000, cấu hình được khôi phục.

## Ba câu kiểm tra hiểu bài

1. AQE — Adaptive Query Execution có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: điều chỉnh kế hoạch khi chạy.
- Luồng chính: Chỉ collect kết quả bốn khách. finally trả cấu hình về giá trị ban đầu.
- Đối chiếu tiêu chí: Hai nhánh cùng tổng 1400000, cấu hình được khôi phục. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 09 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
