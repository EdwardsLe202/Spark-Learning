# Ngày 101 — Cloud object storage IAM và ngân sách

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Cloud object storage IAM và ngân sách”. Kết quả cần đạt: Có thiết kế quyền/chi phí; chỉ ghi deployed cloud khi có bằng chứng thực thi.

## Từ mới gắn với bài này

- **IAM — Identity and Access Management (quản lý danh tính và quyền)**.
- **Service account (danh tính ứng dụng)**.
- **Quota (hạn mức tài nguyên)**.

## Tình huống và cách hiểu

**IAM — Identity and Access Management (quản lý danh tính và quyền)** xác định ai được đọc nguồn/ghi đích. **Service account (danh tính ứng dụng)** không nên dùng quyền chủ tài khoản. **Quota (hạn mức tài nguyên)** và giới hạn chi phí phải có trước khi thử cloud trả phí.

Chọn một môi trường triển khai thực hành là đủ; ngày 100 đã có Standalone local. Cloud ở đây là thiết kế và nhánh triển khai tùy tài khoản, không tự tiêu tiền. Không ghi đã deploy cloud nếu chỉ có JSON policy.

Mẫu policy minh họa job đọc một prefix và ghi một prefix khác. Bucket là tên ví dụ cần thay, không phải tài nguyên đã tạo. Lab có kiểm tra denied action khi bạn thật sự dùng cloud và có budget rõ.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-101/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
policy = {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::course-example/raw/*"}, {"Effect": "Allow", "Action": ["s3:PutObject"], "Resource": "arn:aws:s3:::course-example/predictions/*"}]}
write_json(out / "iam_policy_template.json", policy)
print("Policy template, chưa tạo bucket hoặc cấp quyền thật.")
```

## Đọc từng phần của ví dụ

Template chỉ dùng object action nên không cấp quyền list bucket. Nếu job cần list, bổ sung quyền và prefix condition có lý do.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có thiết kế quyền/chi phí; chỉ ghi deployed cloud khi có bằng chứng thực thi.

## Ba câu kiểm tra hiểu bài

1. IAM — Identity and Access Management có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: quản lý danh tính và quyền.
- Luồng chính: Template chỉ dùng object action nên không cấp quyền list bucket. Nếu job cần list, bổ sung quyền và prefix condition có lý do.
- Đối chiếu tiêu chí: Có thiết kế quyền/chi phí; chỉ ghi deployed cloud khi có bằng chứng thực thi. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 19 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
