# Ngày 84 — Integration test cho dữ liệu và model

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Integration test cho dữ liệu và model”. Kết quả cần đạt: Nhánh sklearn tham chiếu score 120 dòng, rerun không nhân khóa; có integration test độc lập artifact.

## Từ mới gắn với bài này

- **Integration test (kiểm thử các thành phần kết hợp)**.
- **tmp_path (thư mục tạm riêng của test)**.

## Tình huống và cách hiểu

**Integration test (kiểm thử các thành phần kết hợp)** đi qua đọc dữ liệu, tính, ghi và đọc lại. **tmp_path (thư mục tạm riêng của test)** giúp không ghi đè bài làm hoặc dùng lại artifact cũ ngoài ý muốn.

Một test đơn vị groupBy đúng chưa chứng minh path ngày đúng hay model load được. Kiểm tra rerun, schema và số dòng sau đọc lại. Spark fixture cần stop trong teardown để không để nhiều JVM sống sau test.

Bài mẫu đi qua train/evaluate/score bằng CLI tham chiếu với version riêng. Lab thu nhỏ nguồn hoặc dùng tiny để test nhanh; full integration có thể chạy ít thường xuyên hơn test logic. Phân biệt test fail do code với thiếu runtime/dependency.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-084/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from services.pipeline import run_step
version = "integration-demo"
for step in ["validate", "features", "train", "evaluate", "score"]:
    result = run_step(step, version=version)
    print(step, result.get("rows", result.get("accepted", "done")))
run_step("score", version=version)
print("Rerun cùng snapshot/version ghi thay đúng đích.")
```

## Đọc từng phần của ví dụ

Thứ tự phụ thuộc được giữ; score chỉ chạy khi evaluation accepted. Mẫu dùng artifact demo riêng, không sửa artifact bài làm.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Nhánh sklearn tham chiếu score 120 dòng, rerun không nhân khóa; có integration test độc lập artifact.

## Ba câu kiểm tra hiểu bài

1. Integration test có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: kiểm thử các thành phần kết hợp.
- Luồng chính: Thứ tự phụ thuộc được giữ; score chỉ chạy khi evaluation accepted. Mẫu dùng artifact demo riêng, không sửa artifact bài làm.
- Đối chiếu tiêu chí: Nhánh sklearn tham chiếu score 120 dòng, rerun không nhân khóa; có integration test độc lập artifact. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 16 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
