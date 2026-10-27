# Ngày 100 — Chạy Spark Standalone với worker thật

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Chạy Spark Standalone với worker thật”. Kết quả cần đạt: 8 đơn/1400000 từ Spark Standalone, UI có worker thực; không chỉ đổi nhãn appName.

## Từ mới gắn với bài này

- **Standalone cluster (cụm Spark tự quản)**.
- **Client / Cluster mode (driver phía gửi / trong cụm)**.

## Tình huống và cách hiểu

**Standalone cluster (cụm Spark tự quản)** có master quản lý tài nguyên và worker chạy executor. **Client / cluster mode (driver phía gửi / trong cụm)** chỉ vị trí driver, không phải tên ngôn ngữ.

Bài local nhiều container giúp thực hành đường dẫn chung, kết nối và phân biệt driver/executor. Nó vẫn là một máy vật lý, không chứng minh chịu lỗi nhiều máy. Với Python trên Standalone, không mặc định cluster deploy mode được hỗ trợ như mọi môi trường khác; lab dùng client mode.

Compose cluster riêng có image Java 17/PySpark 3.5.7. Script cluster_smoke.py không hard-code local[2], để master URL do spark-submit chọn. Đây là điểm khác với helper local của các ví dụ trước.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-100/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
print((ROOT / "services/spark.compose.yml").read_text())
print("Lab chạy spark-submit bên trong container master với --master spark://master:7077.")
print("Script:", ROOT / "services/cluster_smoke.py")
```

## Đọc từng phần của ví dụ

Script cluster riêng nhận master từ môi trường submit. Helper local không dùng để giả vờ chạy cluster.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

8 đơn/1400000 từ Spark Standalone, UI có worker thực; không chỉ đổi nhãn appName.

## Ba câu kiểm tra hiểu bài

1. Standalone cluster có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: cụm Spark tự quản.
- Luồng chính: Script cluster riêng nhận master từ môi trường submit. Helper local không dùng để giả vờ chạy cluster.
- Đối chiếu tiêu chí: 8 đơn/1400000 từ Spark Standalone, UI có worker thực; không chỉ đổi nhãn appName. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 19 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
