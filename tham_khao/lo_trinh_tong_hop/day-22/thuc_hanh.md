# Ngày 22 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

PyTorch (`torch==2.6.0`); có thể cài riêng hoặc dùng `requirements-ai.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-22/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Cài torch theo requirements-ai.txt hoặc cài riêng torch==2.6.0 nếu chỉ học ngày này; chạy ví dụ CPU.
2. Ghi shape, dtype và device của x, y, prediction. In loss ở epoch 0 và cuối để kiểm tra xu hướng giảm.
3. Chuyển dữ liệu sang TensorDataset/DataLoader, thử batch_size 1 và 4; ghi khác nhau về số bước cập nhật.
4. Lưu state_dict, tạo model mới, load bằng map_location="cpu", eval và no_grad. So dự đoán trên fixture bằng torch.allclose.
5. Viết 5–8 câu giải thích embedding → attention → Transformer; phân biệt điều đã chạy (Linear) với kiến trúc mới học lý thuyết.

## Cách chạy

```bash
python scripts/run_day.py 22
```

Lưu đầu ra tự tạo ở `artifacts/day-22/` bằng `output_dir(22)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Shape prediction [4,1]; loss cuối thấp hơn loss ban đầu. Có checkpoint và script load, dự đoán trước/sau load tương đương. Không đòi loss chính xác giống mọi thiết bị.

## Lỗi dễ gặp và cách điều tra

Quên zero_grad; nhãn [N] còn prediction [N,1]; nghĩ eval tắt autograd; chọn CUDA trên Mac.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Dùng pretrained model nhỏ có quyền sử dụng rõ ràng, đo tokenization và inference CPU; ghi model revision và chi phí bộ nhớ.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
