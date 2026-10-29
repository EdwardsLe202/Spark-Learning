# Ngày 29 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Môi trường Python chuẩn, không cần cài thư viện ngoài.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-29/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Chọn một lỗi thật từ báo cáo ngày 27. Phân loại lỗi tài liệu, retrieval, context, định dạng hoặc hành vi model.
2. Viết 1 trang so sánh ba hướng: sửa dữ liệu/retrieval, sửa prompt, fine-tune. Nêu bằng chứng ủng hộ quyết định và chi phí.
3. Thiết kế ít nhất 20 ví dụ instruction/input/output có nguồn, tách train và validation theo nhóm; test giữ nguyên và không dùng để tạo ví dụ train.
4. Điền experiment_plan.json: model/revision dự kiến, baseline, metric, mục tiêu, giới hạn RAM/thời gian, điều kiện dừng và cách rollback adapter.
5. Nếu đủ máy, train adapter LoRA cho model nhỏ phù hợp phần cứng; giữ checkpoint, so với baseline trên test đã khóa. Nếu không train, ghi “thiết kế thí nghiệm, chưa chạy fine-tuning”.

## Cách chạy

```bash
python scripts/run_day.py 29
```

Lưu đầu ra tự tạo ở `artifacts/day-29/` bằng `output_dir(29)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Bản quyết định gắn với lỗi đã đo, dataset có nguồn và kế hoạch đánh giá. Chỉ có báo cáo benchmark nếu đã thực sự train; không tự tạo con số cải thiện.

## Lỗi dễ gặp và cách điều tra

Fine-tune để chữa thiếu tài liệu; adapter nhỏ được coi là không cần RAM model nền; test bị dùng tạo train; Mac được giả định hỗ trợ mọi kỹ thuật CUDA.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Đo footprint của model nền và adapter riêng; tìm một kỹ thuật tối ưu inference phù hợp runtime đã thực sự sử dụng.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
