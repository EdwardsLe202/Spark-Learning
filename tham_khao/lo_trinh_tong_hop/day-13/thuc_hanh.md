# Ngày 13 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-13/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chạy ví dụ, tính tay ba metric rồi đối chiếu.
2. Dùng dữ liệu ngày 11 và pipeline ngày 12, so baseline luôn đoán lớp đa số với regParam=0.01 và 0.1. Giữ nguyên split.
3. Dùng BinaryClassificationEvaluator với areaUnderPR; ghi cả confusion matrix tại threshold 0.3, 0.5, 0.7 trên validation. Lấy probability lớp 1 bằng vector_to_array nếu cần.
4. Chọn cấu hình/ngưỡng theo chi phí FP và FN bạn tự nêu. Ghi quyết định trước khi chạy test một lần.
5. Lưu bảng số lần fit, runtime, metric toàn bộ và metric theo region; ghi nhóm thiếu mẫu.

## Cách chạy

```bash
python scripts/run_day.py 13
```

Lưu đầu ra tự tạo ở `artifacts/day-13/` bằng `output_dir(13)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Ví dụ: precision=0.6, recall=0.8, accuracy=0.89. Có bảng baseline và hai cấu hình, lý do chọn threshold, báo cáo test tách khỏi bảng lựa chọn.

## Lỗi dễ gặp và cách điều tra

Dùng test để chọn ngưỡng; so metric khác định nghĩa; random fold làm lọt thời gian; coi xác suất model là đã được hiệu chỉnh chắc chắn.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Vẽ precision–recall theo ngưỡng và phân tích chính sách chỉ được liên hệ top 10 khách hàng mỗi kỳ.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
