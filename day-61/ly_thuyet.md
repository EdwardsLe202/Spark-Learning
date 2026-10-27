# Ngày 61 — Từ bảng feature đến bài toán dự đoán

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Từ bảng feature đến bài toán dự đoán”. Kết quả cần đạt: 120 dòng train, feature không chứa customer_id/label; định nghĩa bài toán rõ.

## Từ mới gắn với bài này

- **Feature (biến đầu vào)**.
- **Label / Target (nhãn mục tiêu)**.
- **Classification (phân loại)**.

## Tình huống và cách hiểu

**Feature (biến đầu vào)** là thông tin được phép biết khi ra quyết định; **label / target (nhãn mục tiêu)** là điều muốn dự đoán. **Classification (phân loại)** trong bài churn có hai lớp 0/1. Dự đoán số tiền là regression, không dùng cùng ý nghĩa nhãn.

Từ snapshot ngày 60, tách năm feature và label. Mã khách/snapshot là metadata để truy vết, không tự cho vào model như một biến số. Định nghĩa nhãn phải giữ cùng cách qua train và serving.

Chưa cần train model hôm nay. Hãy giải thích một dòng, một feature có thể dùng trước cutoff, và một cột tương lai phải loại. Nhìn thống kê nhãn để biết lớp nào ít; dữ liệu giả lập không đại diện tỷ lệ churn ngoài đời.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-061/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
train = snapshot_pd()
print(train[FEATURES + ["label"]].head(3).to_string(index=False))
print("Số nhãn:", train["label"].value_counts().to_dict())
assert "customer_id" not in FEATURES
assert "label" not in FEATURES
```

## Đọc từng phần của ví dụ

FEATURES là danh sách contract, không lấy mọi cột tự động. Kiểm tra hai cột không được lẫn vào đầu vào.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

120 dòng train, feature không chứa customer_id/label; định nghĩa bài toán rõ.

## Ba câu kiểm tra hiểu bài

1. Feature có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: biến đầu vào.
- Luồng chính: FEATURES là danh sách contract, không lấy mọi cột tự động. Kiểm tra hai cột không được lẫn vào đầu vào.
- Đối chiếu tiêu chí: 120 dòng train, feature không chứa customer_id/label; định nghĩa bài toán rõ. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 11 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
