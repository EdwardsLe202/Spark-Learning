# Ngày 11 — Thực hành

[Trang ngày](README.md) · [Lý thuyết](ly_thuyet.md) · [File làm bài](bai_lam.py)

## Đầu vào và chỗ làm

Đã xong ngày 02; môi trường nền `requirements.txt`.

Chạy từ **thư mục gốc repo**, sau khi kích hoạt môi trường ở [hướng dẫn cài đặt](../docs/CAI_DAT.md). Sửa `day-11/bai_lam.py`; có thể tạo thêm module, test hoặc notebook trong cùng ngày. Notebook cần dùng đúng interpreter và vẫn có lệnh tái chạy trong nhật ký. Ví dụ có sẵn minh họa khái niệm; các bước bên dưới là phần bạn tự hoàn thiện.

## Các bước thực hiện

1. Trước hết dùng tiny và ba khách hàng C001, C002, C003. Viết tay feature và nhãn tại cutoff 2025-02-01.
2. Hoàn thiện hàm nhận events, customers, cutoff và observed_until; từ chối tạo nhãn nếu chưa đủ 30 ngày tương lai. Tạo recency bằng datediff giữa ngày cutoff và ngày giao dịch gần nhất.
3. Thêm sự kiện tương lai giá trị rất lớn và một giao dịch lịch sử có ingested_at sau cutoff. Kiểm tra cả hai không làm đổi feature.
4. Chạy với events.csv và toàn bộ customers cho ba cutoff train/validation/test. Ghi ba thư mục Parquet riêng dưới artifacts/day-11, mỗi thư mục 120 dòng và khóa duy nhất.
5. Hoàn thành `projects/01-data-pipeline/README.md`: gắn code ngày 5–11, kiểm tra rerun, backfill, join và báo cáo chất lượng.

## Cách chạy

```bash
python scripts/run_day.py 11
```

Lưu đầu ra tự tạo ở `artifacts/day-11/` bằng `output_dir(11)`; thư mục này được Git bỏ qua. Ghi đường dẫn bằng chứng vào phần comment trong `bai_lam.py`. Nếu ngày sau cần artifact, giữ lại hoặc tái tạo bằng lệnh đã ghi. Không sửa `data/raw/` để làm đẹp kết quả; tạo bản thử ở artifacts.

## Kết quả cần đối chiếu

Tiny tại cutoff: C001 có 2 sự kiện, 300.000 VND, recency 12 ngày, churn=0; C002 có 1, 50.000, 17 ngày, churn=1; C003 có 0, 0, recency=NULL, churn=1. T004 chỉ ảnh hưởng nhãn. Ba snapshot đầy đủ tổng 360 dòng.

## Lỗi dễ gặp và cách điều tra

Tính tổng trên toàn lịch sử tương lai; loại khách hàng không hoạt động trước khi gán nhãn; dùng ngày cuối file làm bằng chứng đã quan sát đủ mà không có hợp đồng nguồn.

Khi kết quả khác kỳ vọng, thu nhỏ về fixture, in schema và các dòng liên quan rồi kiểm tra thứ tự lọc, kiểu, biên thời gian và khóa. Giữ lại kết quả sai cùng cách sửa để làm bằng chứng học tập.

## Bài mở rộng

Thêm nhiều snapshot và thiết kế temporal fold (nhóm đánh giá theo thời gian) có khoảng cách phù hợp; lưu cả thời điểm dữ liệu thực sự sẵn có.

## Tiêu chí hoàn thành

- [ ] Đã làm đủ các bước cốt lõi, có lệnh tái chạy và đầu ra thật.
- [ ] Đã đối chiếu kết quả trên, không chỉ thấy chương trình chạy không lỗi.
- [ ] Có ít nhất một biến thể hoặc ca lỗi để kiểm tra hiểu biết.
- [ ] Đã trả lời câu hỏi ở lý thuyết trong phần comment trong `bai_lam.py`.
- [ ] Phân biệt phần chạy thật, mô phỏng và phần mở rộng chưa làm.
