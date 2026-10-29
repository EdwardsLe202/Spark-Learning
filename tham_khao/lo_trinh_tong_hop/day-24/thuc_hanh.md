# Ngày 24 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Môi trường `requirements-api.txt`; ngày 21 và 23 cần model sklearn đã lưu ở ngày 14.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-24/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Cài requirements-api.txt nếu chưa có. Chạy parser mẫu; giữ trường thiếu/null theo quy tắc rõ ràng.
2. Tạo 10 đoạn tiếng Việt có đơn hàng: đủ dữ kiện, thiếu tiền, nhiều mã, tiền mơ hồ và câu chứa chỉ dẫn gây nhiễu. Tự gán nhãn trước.
3. Viết hai prompt cùng schema và giới hạn đầu ra; yêu cầu null khi không có bằng chứng. Version prompt thành v1 và v2.
4. Viết hàm generate(prompt, text) tách khỏi validator. Trước hết thử đầu ra giả lập để kiểm tra lỗi; sau đó dùng một model local nhỏ hoặc API đã chọn để đo nội dung thật.
5. So cùng 10 mẫu, ghi schema pass rate, field accuracy, lỗi, latency và usage nếu có. Giới hạn retry tối đa 2, lưu trạng thái cuối.

## Cách chạy

```bash
python scripts/run_day.py 24
```

Lưu đầu ra tự tạo ở `artifacts/day-24/` bằng `output_dir(24)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Parser nhận mẫu đầu và chặn hai mẫu sau. Có bảng nhãn và so hai prompt; tách kết quả mock với model thật. Không gọi tỷ lệ parse thành công là độ chính xác nội dung.

## Lỗi dễ gặp và cách điều tra

Json hợp lệ được coi là đúng; cố retry tới khi có đáp án; model bịa giá trị trường thiếu; so hai prompt trên hai tập khác nhau.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thêm bộ test ngoài miền và một lớp kiểm tra số tiền trả về phải có bằng chứng cụ thể trong văn bản nguồn.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
