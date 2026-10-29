# Kiểm tra cập nhật ngày 29/10/2026

- Hoàn thiện bài làm ngày 01–08; cả 8 bài chạy qua `uv run --locked python scripts/run_day.py <ngày>` và đối chiếu đúng kết quả kỳ vọng. Các bảng đầu ra của ngày 04–08 đã được so từng dòng với dữ liệu bài tập.
- Cả 8 ví dụ ngày 01–08 chạy thành công qua `uv run python scripts/verify_examples.py --days 1 2 3 4 5 6 7 8`.
- Kiểm tra thêm cách chạy trực tiếp: `uv run python day-08/bai_lam.py`. Ngày 03 cũng chạy lại thành công trong shell mới.
- Môi trường: Python 3.11.15, PySpark 3.5.7, Java 17.0.19. `uv sync --locked` và `uv lock --check` thành công; cấu hình nền ở [pyproject.toml](../pyproject.toml), phiên bản chốt ở [uv.lock](../uv.lock).
- Xóa 180 file ghi chú: 150 ngày chính và 30 ngày tham khảo. Đã sửa các liên kết và bỏ yêu cầu file ghi chú trong hai bộ kiểm tra cấu trúc.
- Hai bộ kiểm tra repo chính/tham khảo đều qua; hash dữ liệu nguồn giữ nguyên. Lịch sử thay đổi bản tham khảo được ghi trong BAN_LUU.json.
- Log bài làm ở `artifacts/beginner/verification/day-01-08/`; log ví dụ ở `artifacts/full/verification/run-50d5c646f2/`. Các thư mục này được Git bỏ qua.

Đợt cập nhật này kiểm tra phạm vi ngày 01–08 và cấu trúc toàn repo; không chạy lại bộ test ML/MLOps/RAG. Báo cáo ngày 27/10 bên dưới là lịch sử của đợt trước, gồm cấu trúc file trước khi xóa ghi chú.

# Phạm vi kiểm tra trước commit ngày27/10/2026

[Lịch150 ngày](../LO_TRINH_DAY_DU.md)

## Cấu trúc và nội dung

- Đủ150 ngày theo điều kiện đầu vào xuôi; mỗi ngày có lý thuyết, thực hành, ví dụ, khung tự làm và nhật ký.
- Đối chiếu đủ150 ý thuộc30 phần tài liệu gốc bằng scripts/source_coverage.json và bảng Markdown.
- Cú pháp Python và code fence, liên kết local, hash/count/key của dữ liệu và các mốc tính tay đều qua bộ kiểm tra.
- Giữ nguyên179/180 file ngày01–30 so với trước khi nối khóa; README ngày30 chỉ thêm liên kết ngày31. Toàn bộ bài làm/ghi chú của30 ngày giữ nguyên.
- Bản lưu178 tệp vẫn đúng SHA-256, gồm bài làm và ghi chú ngày01 trước khi cấu trúc lại.

## Thực thi đã kiểm tra

- **145 ví dụ đã chạy thành công**. Delta ngày44/48 chạy ở JVM riêng với Delta3.3.2/JAR thực, gồm history/time travel và merge chạy lại.
- **21 unit/integration test qua**: metric/threshold, snapshot đủ thời gian quan sát, Spark so ba snapshot với tham chiếu Python, fixture tính tay, future/late event không gây leakage, API auth/input/model equivalence, candidate rejected chặn score, RAG ACL/chunk/metrics/RRF/tool schema.
- **API thật qua HTTP loopback**:100 request, concurrency2, warm-up10, error rate0. Đây chỉ là smoke/load check trên máy này, không là SLO production hay benchmark áp dụng cho máy khác. Server thử đã dừng sau kiểm tra.
- Hai lỗi ví dụ API ngày109–110 do suffix metadata thiếu dấu chấm đã sửa và chạy lại qua.
- Các ví dụ MLflow thực sự tạo/log/load/register model. Các ví dụ chỉ in/parse cấu hình Docker/Airflow/cluster vẫn được phân biệt rõ trong bài; không coi chúng là đã chạy dịch vụ đó.

## Những phần chưa được kiểm chứng runtime trong đợt này

Năm ví dụ cần model tải ngoài: ngày124(generator),129(embedding),132(dense retrieval),135(reranker),137(RAG generation). Cú pháp/interface/điều kiện đã kiểm tra; **chưa tải weights và chưa chấm chất lượng generation/semantic retrieval thật**. Chưa build Docker, chạy Airflow standalone hay Spark Standalone bằng Compose trong đợt này; chưa deploy cloud hoặc train LoRA.

Mỗi lab tương ứng có hướng dẫn chạy thật và tiêu chí. Người học phải thực hiện để nghiệm thu; fixture vector/ranking, mock output, AST parse hoặc file tồn tại không thay bước đó. Từ145 ví dụ qua không suy ra toàn bộ150 ví dụ hoặc mọi dịch vụ tích hợp đã được kiểm chứng.

## Môi trường và giới hạn

macOS Apple Silicon, Python3.11.15, Java17.0.19, PySpark3.5.7, local[2], bộ requirements của repo. Lượt batch local dùng4 shuffle partitions và tắt UI/console progress để log gọn. Runtime không được dùng để hứa tốc độ cluster.

Có3 deprecation warning từ Starlette/AnyIO và sklearn/SciPy trong bộ thư viện đã cài; không có test thất bại. Requirements cố định dependency trực tiếp, chưa là lock toàn bộ phụ thuộc gián tiếp.

Log local ở artifacts/full/verification và artifacts/full/load-tests, được Git bỏ qua. Repo chỉ đưa tài liệu/mã/fixture, không đưa model/cache/log hay credential vào commit.

## Chạy lại kiểm tra

```bash
python scripts/check_repo.py
python -m pytest tests -q
python scripts/verify_examples.py --include-delta
```

Khi đã tải đủ model, thêm --include-models. Để kiểm tra một nhóm vừa sửa: `python scripts/verify_examples.py --days 109 110`. Spark test cần Java và quyền mở cổng loopback trong môi trường chạy.

Những kiểm tra này không chấm mức hiểu bài hay tự đánh dấu bài làm của người học hoàn thành. Tiêu chí học vẫn là tự làm biến thể, giải thích kết quả và có bằng chứng đúng phạm vi.
