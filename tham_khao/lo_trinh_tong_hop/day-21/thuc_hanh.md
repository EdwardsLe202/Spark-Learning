# Ngày 21 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py) · [Nhật ký](ghi_chu.md)

## Đầu vào và chỗ làm

Môi trường `requirements-api.txt`; ngày 21 và 23 cần model sklearn đã lưu ở ngày 14.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-21/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Cài requirements-api.txt. Sửa bai_lam.py thành ứng dụng FastAPI; chạy bằng lệnh uvicorn ghi dưới phần “Cách chạy”.
2. Load artifacts/day-14/model.joblib một lần trong lifespan. Tạo /health, /ready và POST /predict theo contract năm feature ngày 14.
3. Chuyển đúng một request thành DataFrame pandas một dòng, gọi predict_proba, áp threshold đã chọn, trả model_version và request_id.
4. Dùng httpx/TestClient viết test: đúng input, thiếu spend, events âm, sai kiểu, category mới. So response score với gọi trực tiếp pipeline trên cùng input.
5. Thêm giới hạn số dòng mỗi request nếu hỗ trợ batch; log request_id, runtime, version và mã lỗi. Ghi cách dừng bằng Ctrl+C.

## Cách chạy

```bash
python scripts/run_day.py 21
# Sau khi có ứng dụng app trong bai_lam.py:
python -m uvicorn bai_lam:app --app-dir day-21 --host 127.0.0.1 --port 8000
```

Lưu đầu ra tự tạo ở `artifacts/day-21/` bằng `output_dir(21)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào `ghi_chu.md`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Có API dùng model thật đã lưu; /ready chỉ thành công khi model đã load. Lỗi cấu trúc trả 422, input hợp lệ có score trong [0,1], dự đoán khớp gọi trực tiếp.

## Lỗi dễ gặp và cách điều tra

Fit trong endpoint; return score giả nhưng gọi là model inference; async bao quanh CPU nặng; trả 200 khi request thất bại.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thêm API key local qua biến môi trường và test thiếu/sai key; không commit giá trị key vào repo.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong `ghi_chu.md`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
