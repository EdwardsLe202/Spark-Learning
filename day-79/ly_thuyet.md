# Ngày 79 — Shard cho PyTorch và hai loại song song

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Shard cho PyTorch và hai loại song song”. Kết quả cần đạt: Train shards đọc lại 120 dòng; không gọi thao tác xuất file là distributed training.

## Từ mới gắn với bài này

- **Shard (phần dữ liệu chia sẵn)**.
- **Distributed training (huấn luyện phân tán một model)**.
- **Parallel experiments (nhiều thí nghiệm độc lập)**.

## Tình huống và cách hiểu

**Shard (phần dữ liệu chia sẵn)** giúp trainer đọc dần thay vì nạp hết lên driver. Spark có thể chuẩn bị các file, còn DataLoader hoặc thư viện khác đọc theo lô.

**Distributed training (huấn luyện phân tán một model)** phối hợp gradient/trạng thái giữa thiết bị. **Parallel experiments (nhiều thí nghiệm độc lập)** chạy nhiều cấu hình riêng; đó không phải cùng cơ chế. Chạy sklearn.fit trong một task không tự chia một model ra nhiều máy.

Hôm nay chỉ xuất feature thành vài phần và thiết kế contract. Không cần GPU. Ghi số dòng, schema, label và split trong manifest để trainer không vô tình trộn train/test.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-079/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
train = spark_snapshot(spark)
target = out / "train_shards"
train.repartition(2).write.mode("overwrite").parquet(str(target))
write_json(out / "manifest.json", {"split": "train", "rows": 120, "snapshot": "2025-02-01", "format": "parquet"})
print("Số part-file:", len(list(target.glob("part-*"))))
```

## Đọc từng phần của ví dụ

Chia file cho đọc dần, chưa train phân tán. Manifest giữ tập dữ liệu này thuộc train.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Train shards đọc lại 120 dòng; không gọi thao tác xuất file là distributed training.

## Ba câu kiểm tra hiểu bài

1. Shard có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: phần dữ liệu chia sẵn.
- Luồng chính: Chia file cho đọc dần, chưa train phân tán. Manifest giữ tập dữ liệu này thuộc train.
- Đối chiếu tiêu chí: Train shards đọc lại 120 dòng; không gọi thao tác xuất file là distributed training. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 14 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
