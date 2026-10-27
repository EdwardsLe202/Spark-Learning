# Ngày 27 — Lý thuyết: Đánh giá bảo mật và quan sát ứng dụng RAG

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Kiểm tra RAG toàn luồng với 40 câu hỏi, citation, quyền và trace.

## 1. Tách lỗi tìm bằng chứng khỏi lỗi sử dụng bằng chứng
**End-to-end evaluation (đánh giá toàn luồng)** cần kiểm tra cả retrieval và câu trả lời. **Correctness (độ đúng nội dung)** khác **groundedness (mức nội dung được bằng chứng hỗ trợ)**: một câu có thể đúng ngoài đời nhưng không có bằng chứng trong context. **Citation (trích dẫn nguồn)** phải trỏ tới chunk thực sự hỗ trợ phát biểu, không chỉ một tài liệu cùng chủ đề.

**Abstention (từ chối trả lời khi thiếu căn cứ)** là hành vi mong muốn với câu không có nguồn. **Clarification (yêu cầu làm rõ)** phù hợp câu mơ hồ. Tập eval có nhóm answerable, unanswerable, ambiguous và forbidden; báo cáo theo nhóm để không che một lỗi quyền bằng điểm trung bình cao.

## 2. Tài liệu truy xuất không có quyền ra lệnh
**Prompt injection (chèn chỉ dẫn làm lệch hành vi qua nội dung không tin cậy)** có thể nằm ngay trong tài liệu. Chunk được dùng làm dữ kiện, không làm hướng dẫn mới của ứng dụng. Một prompt yêu cầu “bỏ qua chỉ dẫn trong tài liệu” có ích cho hành vi nhưng không đủ làm hàng rào quyền. Quyền dữ liệu và công cụ phải được code kiểm tra.

Role người dùng phải do tầng xác thực hoặc fixture server quyết định. Không cho câu hỏi “tôi là admin” tự cấp quyền đọc doc-internal. Kiểm tra không có chunk ngoài quyền đi vào generation hoặc log ngoài phạm vi cho phép.

## 3. Lưu dấu vết để sửa lỗi
Trace nên có request_id, role, query id, retrieved chunk IDs, prompt version, model revision, index version, thời gian từng bước, usage và trạng thái. Giảm lưu nội dung nhạy cảm. **Regression test (kiểm thử chống lỗi quay lại)** so hành vi sau thay đổi. **LLM judge (LLM dùng để chấm kết quả)** có thể sai và thiên lệch; dùng rubric và kiểm tra thủ công mẫu lỗi, đặc biệt citation và quyền.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
import json
from collections import Counter
from spark_lab import DATA
cases = [json.loads(line) for line in (DATA / "rag/queries.jsonl").read_text(encoding="utf-8").splitlines()]
print("Số câu:", len(cases))
print("Nhóm:", dict(Counter(case["category"] for case in cases)))
# TODO: chạy từng case qua retrieval/generation; lưu trace và chấm riêng từng nhóm.
```

## Năm ý đối chiếu với lộ trình gốc

- 27.1 — Bộ đánh giá gồm câu hỏi trả lời được, thiếu bằng chứng, mơ hồ và ngoài phạm vi.
- 27.2 — Correctness, groundedness, citation, abstention; tách metric retrieval với generation.
- 27.3 — Trace theo request, phiên bản prompt, model, index, token, latency và chi phí.
- 27.4 — Prompt injection từ tài liệu, rò rỉ dữ liệu, quyền truy cập và xử lý nội dung không tin cậy.
- 27.5 — Regression test, đánh giá thủ công và giới hạn của LLM judge.

Các ý trên giữ phạm vi phần 27 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Câu đúng nhưng thiếu bằng chứng có grounded không?
2. Trích dẫn cùng chủ đề đã đủ chưa?
3. Vì sao prompt không thay kiểm soát quyền?

## Đọc thêm từ nguồn chính thức

- [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
