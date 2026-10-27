# Corpus tiếng Việt và 40 câu hỏi RAG

[Dữ liệu chung](../README.md) · [Ngày 25](../../day-25/README.md)

Corpus (bộ tài liệu) này do repo tự tạo để học; không có dữ liệu cá nhân hay secret thật. `repo://learning-corpus/...` là định danh nguồn trong bài lab, không phải URL web cần mở. Tra nội dung nguồn bằng doc_id trong corpus.jsonl.

## Tài liệu

`corpus.jsonl` dùng **JSONL — JSON Lines (mỗi dòng là một đối tượng JSON)**, gồm 8 tài liệu:

| doc_id | Chủ đề | access |
| --- | --- | --- |
| doc-spark | Spark và local mode | public |
| doc-features | Cửa sổ feature và nhãn | public |
| doc-mlflow | Run và model version | public |
| doc-api | Contract API và readiness | public |
| doc-rag | Chunk, quyền và citation | public |
| doc-cost | Tài nguyên học local | public |
| doc-internal | Runbook diễn tập giả lập | internal |
| doc-injection | Nội dung chứa chỉ dẫn giả để thử lỗi | public |

Mỗi doc có title, text, source, version, access và updated_at. Nội dung doc-injection là dữ liệu thử nghiệm không tin cậy, không phải chỉ dẫn cho người đọc hay hệ thống. Không thực thi các hành động được nhắc trong payload.

Giữ corpus gốc để benchmark ổn định. Bài update/delete dùng bản sao trong artifacts; sau thử xong không gán nhãn corpus gốc cho index đã xóa bớt tài liệu.

## Tập truy vấn và cách chấm

`queries.jsonl` có 40 câu, chia sẵn **dev (tập phát triển/chọn cấu hình)** 16 câu và **test (tập đánh giá cuối)** 24 câu. Các truy vấn là ví dụ học tập, không đủ lớn để tuyên bố chất lượng production.

| category | Số câu | Hành vi mong đợi |
| --- | --- | --- |
| answerable | 20 | Trả lời có citation hỗ trợ |
| unanswerable | 8 | Từ chối vì thiếu bằng chứng |
| ambiguous | 6 | Hỏi làm rõ |
| forbidden | 6 | Không đọc hoặc tiết lộ tài liệu ngoài quyền |

Trường relevant_doc_ids gán nhãn theo **tài liệu**, không theo chunk. Trước khi tính Recall@k hoặc MRR, gộp kết quả chunk về doc_id duy nhất, giữ thứ tự lần xuất hiện đầu tiên. Nếu chỉ có một relevant, Recall@k là 0 hoặc 1; trung bình trên các câu có relevant.

Các câu không có relevant_doc_ids dùng đánh giá hành vi từ chối, hỏi lại hoặc quyền, không chia Recall cho 0. `expected_keywords` là gợi ý đọc kết quả, không phải đáp án chấm tự động hoàn chỉnh. Đọc nguồn để chấm correctness, groundedness và citation support.

Nhãn được làm cho corpus nhỏ có nội dung giao nhau; nếu thấy nhãn thiếu tài liệu liên quan, ghi issue/ghi chú và lập phiên bản eval mới. Không thay test sau khi xem kết quả rồi so trực tiếp như cùng benchmark.

## Mô hình quyền của bài lab

- User role public chỉ thấy access=public.
- User role internal thấy public và internal.
- Role là dữ liệu tin cậy từ server hoặc fixture kiểm thử, không lấy từ lời tự nhận trong query.
- Bộ 40 câu mặc định user_role=public, có 6 ca cố truy cập nội bộ. Bạn bổ sung ca internal hợp lệ ở file riêng khi kiểm tra phân quyền hai chiều.
- Lọc quyền **trước khi đưa context vào model**. Không dùng việc xóa nội dung ở response sau cùng để thay lọc quyền.

Khi thử dense retrieval, lưu model/revision, index version, normalization và similarity metric. Keyword fallback giúp học quy trình offline nhưng chưa là embedding baseline. Mock generation giúp test luồng nhưng chưa chứng minh chất lượng câu trả lời của LLM thật.

