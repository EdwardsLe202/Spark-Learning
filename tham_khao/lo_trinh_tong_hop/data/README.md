# Dữ liệu dùng xuyên suốt

[Lộ trình](../README.md)

Tất cả dữ liệu đi kèm là **synthetic data (dữ liệu giả lập)** do repo tạo để học, không có thông tin khách hàng thật. Bạn có thể dùng chúng cho các bài và portfolio, đồng thời ghi rõ nguồn giả lập.

## Các file

| File | Nội dung | Mục đích |
| --- | --- | --- |
| `raw/customers.csv` | 120 khách hàng, C001–C120 | Bảng gốc để giữ cả người không giao dịch |
| `raw/events.csv` | 6.529 sự kiện, từ 2025-01-01 đến hết 2025-07-31 | Feature, nhãn, train và score |
| `raw/events_tiny.csv` | 4 sự kiện có kết quả tính tay | SQL, join và test chống leakage |
| `raw/events_dirty.csv` | 8 dòng có lỗi/trùng | Làm sạch, quarantine và dedup |
| `raw/manifest.json` | Seed, số dòng, mốc quan sát và SHA-256 | Định danh dữ liệu và kiểm tra tái lập |
| `rag/` | 8 tài liệu tự tạo, 40 truy vấn có nhãn | Chunking, retrieval, eval và quyền |

`events.csv` dùng cơ chế xác suất đơn giản theo khách hàng và tháng; điểm số trên dữ liệu này không đại diện hiệu quả kinh doanh thật. Số sự kiện tái tạo bằng generator hiện tại là 6.529; manifest là nơi đối chiếu nếu bạn chủ động đổi generator.

## Data dictionary (từ điển dữ liệu)

| Cột | Kiểu logic | Ý nghĩa và quy tắc |
| --- | --- | --- |
| `customer_id` | string | Khóa khách hàng, duy nhất trong customers; không thiếu ở event hợp lệ |
| `region` | string | HN, HCM hoặc DN trong corpus khách hàng ban đầu |
| `plan` | string | basic hoặc pro |
| `signup_date` | date | Ngày bắt đầu tham gia; tất cả trước snapshot đầu |
| `event_id` | string | Khóa sự kiện sau xử lý trùng |
| `event_time` | timestamp UTC | Lúc giao dịch xảy ra |
| `ingested_at` | timestamp UTC | Lúc nguồn ghi nhận bản ghi; dùng xác định dữ liệu đã sẵn có |
| `amount` | long, VND | Số tiền nguyên, không âm; dữ liệu CSV lúc đọc ban đầu là chuỗi |
| `event_type` | string | purchase trong fixture này |

CSV cố ý đọc cột sự kiện dưới dạng chuỗi. Người học tự parse, tách lỗi và kiểm tra kiểu. Với sự kiện nhiều phiên bản, ngày 5 giữ bản ingested_at mới nhất; với feature tại một cutoff chỉ được chọn phiên bản sẵn có trước cutoff. Nếu ingest có lịch sử sửa đổi, phải áp điều kiện thời gian trước khi chọn phiên bản mới nhất cho snapshot.

## Quy ước thời gian, feature và nhãn

Tất cả snapshot là UTC lúc 00:00. Ví dụ `2025-02-01` nghĩa là `2025-02-01T00:00:00Z`.

- Feature: event_time trong **[cutoff − 30 ngày, cutoff)** và ingested_at **< cutoff**.
- Nhãn churn: **1** nếu không có purchase hợp lệ trong **[cutoff, cutoff + 30 ngày)**, ngược lại **0**.
- Chỉ tạo nhãn khi observed_until_exclusive **>= cutoff + 30 ngày**. Manifest bảo đảm đã quan sát tới `2025-08-01T00:00:00Z`; đây là hợp đồng của nguồn giả lập, không suy ra chỉ từ max event_time.
- `events_30d`: số sự kiện; `spend_30d`: tổng VND; không có sự kiện thì cả hai bằng 0.
- `recency_days`: số ngày lịch UTC từ ngày giao dịch lịch sử gần nhất trong cửa sổ tới ngày cutoff; không có giao dịch thì NULL. Đây là recency trong cửa sổ, không phải recency trọn đời.
- Khóa snapshot: `(customer_id, snapshot_date)`; nhãn chưa đủ cửa sổ phải bị chặn hoặc để trạng thái chưa có nhãn, không mặc định churn=1.

| Tập | Cutoff | Feature window | Label window |
| --- | --- | --- | --- |
| Train | 2025-02-01 | [2025-01-02, 2025-02-01) | [2025-02-01, 2025-03-03) |
| Validation | 2025-04-01 | [2025-03-02, 2025-04-01) | [2025-04-01, 2025-05-01) |
| Test | 2025-06-01 | [2025-05-02, 2025-06-01) | [2025-06-01, 2025-07-01) |
| Scoring | 2025-07-01 | [2025-06-01, 2025-07-01) | Không cần nhãn khi dự đoán |

Một khách hàng có thể có ở nhiều kỳ vì mục tiêu là dự đoán tương lai cho khách hàng hiện có. Bài toán người dùng hoàn toàn mới cần chiến lược chia theo entity khác. Không dùng test để chọn feature, cấu hình hay threshold.

## Kết quả chuẩn của fixture nhỏ

Tiny tổng 1.250.000 VND. T004 có 900.000 VND ngày 2025-02-05, là tương lai đối với cutoff 2025-02-01.

| Khách hàng | events_30d | spend_30d | recency_days | churn |
| --- | --- | --- | --- | --- |
| C001 | 2 | 300000 | 12 | 0 |
| C002 | 1 | 50000 | 17 | 1 |
| C003 | 0 | 0 | NULL | 1 |

Bảng trên chỉ lọc ba khách hàng để tính tay. Với toàn bộ customers và tiny vẫn phải tạo 120 dòng feature, gồm khách hàng không giao dịch.

Dirty: D003 thiếu customer, D004 thời gian sai, D005 số âm, D006 customer không tồn tại, D007 amount không parse được. D002 có hai phiên bản, giữ bản 70.000 VND tới sau. Đối soát: **8 đầu vào = 5 lỗi + 1 bản cũ + 2 sạch**, tổng sạch 170.000 VND.

## Tạo lại và bảo quản

Chỉ chạy lệnh sau khi muốn khôi phục fixture gốc; nó ghi lại các file CSV/manifest do generator quản lý:

```bash
python scripts/generate_data.py
```

Giữ nguồn gốc bất biến khi làm lab. Tạo dữ liệu lỗi mới, nguồn đến muộn và kết quả thử dưới `artifacts/day-XX/`. Nếu thay generator, lưu version code và manifest mới; không tiếp tục dùng kết quả tính tay cũ một cách mặc định.

