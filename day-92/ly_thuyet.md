# Ngày 92 — Chạy Airflow TaskFlow trong môi trường riêng

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Chạy Airflow TaskFlow trong môi trường riêng”. Kết quả cần đạt: Có log/UI run DAG thật, output và interpreter đúng; không chỉ parse file.

## Từ mới gắn với bài này

- **TaskFlow (API tạo task từ hàm)**.
- **Scheduler (bộ lập lịch thực thi)**.

## Tình huống và cách hiểu

**TaskFlow (API tạo task từ hàm)** của Airflow 3.0 dùng dag/task decorator. **Scheduler (bộ lập lịch thực thi)** quyết định task đủ điều kiện chạy. Airflow là môi trường riêng, không cài đè constraints lên môi trường ML.

DAG mẫu gọi Python của venv ML qua COURSE_PYTHON. Worker không tự có PySpark/sklearn chỉ vì terminal đang học đã cài. Đường dẫn repo phải sẵn có nơi task chạy; local standalone và cluster executor có điều kiện khác nhau.

Mẫu Python hôm nay chỉ kiểm tra file DAG tồn tại/parse được. Lab bắt buộc bật Airflow standalone, nạp DAG và chạy task thật để nghiệm thu. Cài đặt, biến môi trường và cách dừng có trong hướng dẫn nâng cao.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-092/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
import ast
path = ROOT / "services/airflow/dags/churn_pipeline.py"
ast.parse(path.read_text())
print("DAG nguồn:", path)
print("Chưa chạy Airflow. Thực hiện lab theo docs/CAI_DAT_NANG_CAO.md.")
```

## Đọc từng phần của ví dụ

AST chỉ xác nhận cú pháp Python, không chứng minh Airflow import hoặc task thực thi được.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có log/UI run DAG thật, output và interpreter đúng; không chỉ parse file.

## Ba câu kiểm tra hiểu bài

1. TaskFlow có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: API tạo task từ hàm.
- Luồng chính: AST chỉ xác nhận cú pháp Python, không chứng minh Airflow import hoặc task thực thi được.
- Đối chiếu tiêu chí: Có log/UI run DAG thật, output và interpreter đúng; không chỉ parse file. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 17 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
