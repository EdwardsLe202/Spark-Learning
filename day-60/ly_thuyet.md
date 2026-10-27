# Ngày 60 — Nghiệm thu dự án 1 dữ liệu và feature

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Nghiệm thu dự án 1 dữ liệu và feature”. Kết quả cần đạt: Ba snapshot, tổng 360 dòng, khóa duy nhất; có bằng chứng tính đúng và phục hồi.

## Từ mới gắn với bài này

- **Data lineage (nguồn gốc các bước tạo dữ liệu)**.
- **Acceptance test (kiểm tra nghiệm thu)**.

## Tình huống và cách hiểu

**Data lineage (nguồn gốc các bước tạo dữ liệu)** nối snapshot với nguồn, code và quy tắc thời gian. **Acceptance test (kiểm tra nghiệm thu)** chứng minh đầu ra đáp ứng yêu cầu, không chỉ chạy không lỗi.

Dự án 1 kết hợp làm sạch, khóa, join, incremental và feature. Ngày này tập trung tạo ba snapshot có data dictionary và lệnh tái chạy. Dùng reference để so nhưng bài làm cần dùng code bạn đã tự triển khai ở các ngày trước.

Các ca phải có gồm timestamp sai, khóa trùng, sự kiện tương lai, dữ liệu đến muộn và chạy lại cùng ngày. Báo cả vùng lỗi và phạm vi bị ghi lại. Nếu thiếu một ca, ghi chưa đạt và quay về ngày liên quan.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-060/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
for day in ["2025-02-01", "2025-04-01", "2025-06-01"]:
    frame = build_features_spark(spark, day)
    target = out / ("snapshot_date=" + day)
    frame.write.mode("overwrite").parquet(str(target))
    loaded = spark.read.parquet(str(target))
    assert loaded.count() == 120
    print(day, loaded.count())
write_json(out / "manifest.json", {"source_hash": data_hash(), "snapshots": ["2025-02-01", "2025-04-01", "2025-06-01"]})
```

## Đọc từng phần của ví dụ

Mỗi đích snapshot độc lập, đọc lại sau ghi. Manifest lưu hash nguồn nhưng không tự sao lưu dữ liệu.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Ba snapshot, tổng 360 dòng, khóa duy nhất; có bằng chứng tính đúng và phục hồi.

## Ba câu kiểm tra hiểu bài

1. Data lineage có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: nguồn gốc các bước tạo dữ liệu.
- Luồng chính: Mỗi đích snapshot độc lập, đọc lại sau ghi. Manifest lưu hash nguồn nhưng không tự sao lưu dữ liệu.
- Đối chiếu tiêu chí: Ba snapshot, tổng 360 dòng, khóa duy nhất; có bằng chứng tính đúng và phục hồi. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 11 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
