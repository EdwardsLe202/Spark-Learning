# Ngày 58 — Tạo nhãn churn khi đủ quan sát

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Tạo nhãn churn khi đủ quan sát”. Kết quả cần đạt: Cutoff 2025-07-15 bị từ chối; nhãn tiny đúng 0/1/1.

## Từ mới gắn với bài này

- **Churn (không hoạt động theo định nghĩa)**.
- **Censoring (chưa quan sát đủ kết quả)**.

## Tình huống và cách hiểu

**Churn (không hoạt động theo định nghĩa)** trong bài bằng 1 nếu không có purchase trong 30 ngày sau cutoff. **Censoring (chưa quan sát đủ kết quả)** xảy ra khi nguồn kết thúc trước cửa sổ nhãn. Không thấy giao dịch trong nguồn thiếu chưa chứng minh khách churn.

Manifest quy định observed_until_exclusive=2025-08-01 UTC. Chỉ gán nhãn nếu cutoff+30 ngày không vượt mốc đó. Nhãn không có feature_time; nó mô tả tương lai dùng cho học và đánh giá sau khi đủ quan sát.

Ví dụ dùng hàm Spark đã thêm nhãn. Thử cutoff không đủ cửa sổ phải báo lỗi. Dữ liệu đầy đủ có 120 khách và cả hai lớp; ghi số lượng thực tế thay vì bịa tỷ lệ churn đẹp.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-058/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
labeled = build_features_spark(spark, "2025-02-01")
labeled.groupBy("label").count().show()
try:
    build_features_spark(spark, "2025-07-15")
except ValueError as error:
    print("Đã chặn nhãn chưa đủ quan sát:", error)
```

## Đọc từng phần của ví dụ

Hàm kiểm tra khoảng quan sát trước khi tạo nhãn. Cutoff tháng 7 này cần thấy giữa tháng 8 nhưng nguồn chưa đủ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Cutoff 2025-07-15 bị từ chối; nhãn tiny đúng 0/1/1.

## Ba câu kiểm tra hiểu bài

1. Churn có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: không hoạt động theo định nghĩa.
- Luồng chính: Hàm kiểm tra khoảng quan sát trước khi tạo nhãn. Cutoff tháng 7 này cần thấy giữa tháng 8 nhưng nguồn chưa đủ.
- Đối chiếu tiêu chí: Cutoff 2025-07-15 bị từ chối; nhãn tiny đúng 0/1/1. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 11 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
