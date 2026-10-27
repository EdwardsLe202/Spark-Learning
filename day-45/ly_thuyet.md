# Ngày 45 — Ôn Spark nâng cao và báo cáo hiệu năng

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Ôn Spark nâng cao và báo cáo hiệu năng”. Kết quả cần đạt: Mọi trial tổng 1100000; có báo cáo trước/sau bằng số thật.

## Từ mới gắn với bài này

- **Benchmark (thử nghiệm đo có điều kiện)**.
- **Equivalence (tính tương đương kết quả)**.

## Tình huống và cách hiểu

**Benchmark (thử nghiệm đo có điều kiện)** cần cố định nguồn, code và cấu hình để giải thích thay đổi. **Equivalence (tính tương đương kết quả)** nghĩa là hai cách xử lý cho cùng giá trị theo khóa và sai số đã chốt, không nhất thiết cùng thứ tự dòng hay cùng tên file.

Chọn một thay đổi như broadcast bảng nhỏ, giữ baseline và đo ba lần sau warm-up. Báo cả kết quả không nhanh hơn. Với nguồn nhỏ, chi phí khởi động có thể lấn thời gian tính; đó là giới hạn cần ghi.

Đây là buổi hoàn thiện phần Spark của dự án: plan, UI, số dòng, tổng tiền và mô tả phần cứng. Không thêm năm kỹ thuật cùng lúc rồi quy cải thiện cho một kỹ thuật.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-045/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. `spark` là phiên đã mở và `orders` là tám đơn ở khóa nền; F/Window là API đã học. Các helper sự kiện/feature có code trong course_support.py.

```python
from time import perf_counter
records = []
for i in range(3):
    start = perf_counter()
    result = orders.filter(F.col("status") == "completed").groupBy("customer_id").agg(F.sum("amount").alias("total"))
    rows = result.orderBy("customer_id").collect()
    records.append({"trial": i + 1, "seconds": perf_counter() - start, "total": sum(r.total for r in rows)})
write_json(out / "baseline.json", records)
print(records)
```

## Đọc từng phần của ví dụ

Collect chỉ bảng tổng bốn khách, action nằm trong khoảng đo. JSON lưu cả ba lần, không lấy riêng lần tốt nhất.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Mọi trial tổng 1100000; có báo cáo trước/sau bằng số thật.

## Ba câu kiểm tra hiểu bài

1. Benchmark có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: thử nghiệm đo có điều kiện.
- Luồng chính: Collect chỉ bảng tổng bốn khách, action nằm trong khoảng đo. JSON lưu cả ba lần, không lấy riêng lần tốt nhất.
- Đối chiếu tiêu chí: Mọi trial tổng 1100000; có báo cáo trước/sau bằng số thật. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 09 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
