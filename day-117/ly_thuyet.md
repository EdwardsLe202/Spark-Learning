# Ngày 117 — Đo latency throughput và percentile

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Đo latency throughput và percentile”. Kết quả cần đạt: Có báo cáo đo thật tách số minh họa; không khẳng định một ngưỡng chung cho mọi máy.

## Từ mới gắn với bài này

- **Latency (độ trễ mỗi request)**.
- **Throughput (số request mỗi đơn vị thời gian)**.
- **p95 (phân vị độ trễ 95 phần trăm)**.

## Tình huống và cách hiểu

**Latency (độ trễ mỗi request)** khác **throughput (số request mỗi đơn vị thời gian)**. **p95 (phân vị độ trễ 95 phần trăm)** cần số mẫu đủ và cách tính rõ; 20 request không hỗ trợ kết luận tail latency chắc chắn.

Warm-up tách khởi tạo khỏi trạng thái ổn định. Ghi cả request lỗi và timeout; bỏ lỗi khỏi báo cáo có thể làm dịch vụ trông tốt giả. Throughput tính theo wall time toàn lượt, không lấy tổng latency cộng lại làm thời gian.

Mẫu tính phân vị từ một danh sách thời gian giả định để học công thức. Lab dùng services/load_test.py vào API thật với input cố định, concurrency 1/2/4 và so score/version. Không dùng số mẫu minh họa như kết quả benchmark máy bạn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-117/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import numpy as np
sample_ms = [10, 12, 11, 14, 13, 30, 15, 12, 11, 16]
print({"p50": float(np.percentile(sample_ms, 50)), "p95": float(np.percentile(sample_ms, 95)), "n": len(sample_ms), "source": "illustrative_numbers"})
```

## Đọc từng phần của ví dụ

Percentile nội suy tùy thuật toán; ghi numpy percentile và nguồn số minh họa. Chưa có HTTP request ở ví dụ này.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có báo cáo đo thật tách số minh họa; không khẳng định một ngưỡng chung cho mọi máy.

## Ba câu kiểm tra hiểu bài

1. Latency có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: độ trễ mỗi request.
- Luồng chính: Percentile nội suy tùy thuật toán; ghi numpy percentile và nguồn số minh họa. Chưa có HTTP request ở ví dụ này.
- Đối chiếu tiêu chí: Có báo cáo đo thật tách số minh họa; không khẳng định một ngưỡng chung cho mọi máy. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 23 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
