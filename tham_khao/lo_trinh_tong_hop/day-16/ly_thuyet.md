# Ngày 16 — Lý thuyết: Cấu trúc project kiểm thử và chất lượng code

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Tách logic khỏi I/O và viết test phát hiện join sai, rò rỉ thời gian và trùng khóa.

## 1. Tách phần tính với phần giao tiếp
**Module (đơn vị mã nguồn Python)** chứa chức năng có thể import. **CLI — Command-Line Interface (giao diện dòng lệnh)** nhận ngày, nguồn và đích thay vì sửa hằng số mỗi lần chạy. **Configuration (cấu hình)** mô tả lựa chọn môi trường; logic nghiệp vụ nên nhận cấu hình rõ ràng.

Hàm `build_features(events, customers, cutoff)` trả DataFrame sẽ dễ kiểm thử hơn hàm vừa đọc file, tính, ghi và gửi thông báo. Tách **I/O — Input/Output (đọc ghi với bên ngoài)** khỏi biến đổi. Giữ hành vi đầu ra và chỉ chuyển code ngày cũ sau khi đối chiếu kết quả.

## 2. Test nên bắt lỗi có hậu quả
**Unit test (kiểm thử một đơn vị logic)** dùng fixture nhỏ để kiểm tra feature. **Integration test (kiểm thử các thành phần kết hợp)** đi xuyên đọc file → tính → ghi → đọc lại. **Fixture (dữ liệu hoặc thiết lập dùng cho kiểm thử)** cần có biên thời gian và dòng lỗi, không chỉ các dòng đẹp.

**Data contract (hợp đồng dữ liệu)** gồm kiểu cột, khóa, tính thiếu và ý nghĩa. Test schema đúng không phát hiện join nhân dòng; cần kiểm tra số dòng, khóa duy nhất và tổng tiền. Test chống leakage phải chèn sự kiện sau cutoff và chứng minh feature không đổi. Đây là hành vi độc lập, có ích hơn việc chép công thức của hàm vào test.

## 3. Lỗi phải nhìn thấy được
**Logging (ghi sự kiện hoạt động)** nên có ngày dữ liệu, bước, runtime và số dòng. **Exception (ngoại lệ)** biểu thị lỗi; **exit code (mã kết thúc chương trình)** khác 0 cho scheduler biết thất bại. Không nuốt mọi lỗi rồi in “xong”. Secret nằm ngoài Git; dữ liệu giả lập nhỏ có thể lưu trong repo để người khác chạy test.

## Ví dụ nhỏ để đọc và chạy

Ví dụ dùng `spark`, `F` và các hàm đọc dữ liệu do file khởi động thiết lập. Chạy bằng runner ở bài thực hành; không dán riêng đoạn này vào terminal shell.

```python
from pyspark.sql import Window
# Fixture cố ý có khóa trùng: kiểm tra này phải phát hiện lỗi.
df = spark.createDataFrame([("C001", 1), ("C001", 2)], "customer_id string, value int")
duplicates = df.groupBy("customer_id").count().filter("count > 1")
print("Khóa bị trùng:", duplicates.count())
# TODO: biến kiểm tra thành hàm validate_unique(df, keys) và viết pytest cho nó.
```

## Năm ý đối chiếu với lộ trình gốc

- 16.1 — Git, nhánh, commit, package, CLI và tách logic khỏi thao tác đọc ghi.
- 16.2 — Cấu hình theo môi trường, logging, exception và mã thoát.
- 16.3 — Unit test cho feature; integration test cho đọc ghi, train và predict.
- 16.4 — Kiểm tra schema, unique key, NULL, timestamp, leakage và data contract.
- 16.5 — Kiểm tra dependency, lint, kiểm thử nhanh trước khi chạy pipeline lớn.

Các ý trên giữ phạm vi phần 16 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Test nào bắt join nhân tiền?
2. Vì sao tách hàm thuần biến đổi khỏi đọc ghi?
3. Mã kết thúc khác 0 giúp scheduler gì?

## Đọc thêm từ nguồn chính thức

- [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
