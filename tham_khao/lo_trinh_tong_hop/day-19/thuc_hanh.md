# Ngày 19 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường Python chuẩn, không cần cài thư viện ngoài.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-19/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Đọc workflow mẫu `.github/workflows/ci.yml`. Chạy kiểm tra tương đương ở local trước khi đẩy code.
2. Sau khi đã có test ngày 16, thêm job CI dùng Python 3.11, Java 17, cài requirements.txt và chạy pytest project. Chạy fixture nhỏ, không cần dataset riêng tư.
3. Điền release manifest bằng thông tin thật, lưu hai bản candidate và previous. Mô tả quality gate model và schema.
4. Thử phát hành local model candidate, rồi quay về model previous; xác nhận cùng fixture tạo dự đoán tương ứng version cũ.
5. Viết sơ đồ quyền cho nguồn chỉ đọc và thư mục prediction chỉ ghi. Nếu chọn cloud, lập kế hoạch và ngân sách riêng trước, không cần deploy trả phí để xong ngày này.

## Cách chạy

```bash
python scripts/run_day.py 19
```

Lưu đầu ra tự tạo ở `artifacts/day-19/` bằng `output_dir(19)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Workflow kiểm tra repo có sẵn; bạn mở rộng nó để chạy test nghiệp vụ. Có hai manifest thực, log rollback local và bảng quyền. Không ghi “đã deploy cloud” nếu chưa làm.

## Lỗi dễ gặp và cách điều tra

Đổi code nhưng quên version model; nhầm CI xanh với được phép phát hành; rollback artifact nhưng để schema mới không tương thích.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Build image gắn commit tag trong CI và thêm bước phê duyệt release tách biệt; thử bằng local registry hoặc artifact tải về, không bắt buộc cloud.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
