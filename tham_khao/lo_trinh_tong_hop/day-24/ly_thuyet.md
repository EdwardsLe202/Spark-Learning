# Ngày 24 — Lý thuyết: LLM prompting và đầu ra có cấu trúc

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Xây hợp đồng đầu ra, xử lý JSON lỗi và đánh giá prompt trên tập cố định.

## 1. Mô hình sinh văn bản có giới hạn
**LLM — Large Language Model (mô hình ngôn ngữ lớn)** sinh đầu ra theo ngữ cảnh, không phải kho dữ kiện luôn đúng. **Token (đơn vị văn bản do tokenizer chia)** không luôn bằng một từ; tiếng Việt cũng không có quy đổi cố định token trên từ. **Context window (giới hạn ngữ cảnh)** tính cả phần đầu vào và các giới hạn đầu ra theo model.

**Prompt template (mẫu lời nhắc)** giữ cấu trúc lặp lại; **system instruction (chỉ dẫn mức hệ thống)** mô tả nhiệm vụ; **few-shot example (ví dụ mẫu trong ngữ cảnh)** minh họa cách trả lời. Tách văn bản người dùng khỏi chỉ dẫn bằng cấu trúc rõ giúp model hiểu nhiệm vụ, nhưng không tự tạo ranh giới bảo mật chắc chắn.

## 2. Đúng JSON chưa chắc đúng nội dung
**Structured output (đầu ra có cấu trúc)** tuân theo schema giúp ứng dụng parse. **Schema validation (kiểm tra theo lược đồ)** bắt trường thiếu, sai kiểu hoặc sai miền giá trị; vẫn cần đối chiếu nội dung với nguồn. Ví dụ amount=999999 là số nguyên hợp lệ nhưng có thể sai dữ kiện.

Chốt biểu diễn thiếu bằng null, không bịa. **Bounded retry (thử lại có giới hạn)** chỉ thử số lần nhất định; nếu vẫn lỗi phải trả trạng thái rõ. Ghi timeout, lỗi parse, đầu ra bị từ chối, phiên bản prompt và usage thay vì chỉ giữ trường hợp đẹp.

## 3. Prompting, RAG và fine-tuning
Prompting đổi hướng dẫn trong request. **RAG — Retrieval-Augmented Generation (sinh câu trả lời có truy xuất tài liệu hỗ trợ)** đưa bằng chứng ngoài vào ngữ cảnh. **Fine-tuning (huấn luyện điều chỉnh tham số)** thay đổi trọng số model bằng dữ liệu bổ sung. Chúng xử lý các nhóm nhu cầu khác nhau. Bài học dùng adapter (lớp giao tiếp tách nhà cung cấp) để bạn có thể dùng model local hoặc API đã chọn, có hạn mức chi phí.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
from pydantic import BaseModel, ConfigDict, Field, ValidationError
class ExtractedOrder(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    order_id: str | None
    amount_vnd: int | None = Field(ge=0)
for text in ['{"order_id":"A01","amount_vnd":120000}', '{"order_id":"A01","amount_vnd":-3}', 'không phải JSON']:
    try:
        print(ExtractedOrder.model_validate_json(text))
    except ValidationError as exc:
        print("INVALID", exc.error_count())
# Đây là kiểm thử parser bằng đầu ra giả lập, chưa đánh giá một LLM.
```

## Năm ý đối chiếu với lộ trình gốc

- 24.1 — Token, context window, sinh văn bản, tham số lấy mẫu và giới hạn đầu ra.
- 24.2 — System instruction, prompt template, few shot và tách dữ liệu khỏi chỉ dẫn.
- 24.3 — Structured output, schema validation, retry có giới hạn và xử lý từ chối hoặc lỗi.
- 24.4 — Embedding, similarity; phân biệt prompting, RAG và fine tuning.
- 24.5 — Chi phí, rate limit, timeout; tạo tập ví dụ để so sánh prompt.

Các ý trên giữ phạm vi phần 24 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. Token có luôn bằng một từ không?
2. Schema phát hiện được số tiền bịa không?
3. Khi nào nên truy xuất tài liệu thay vì chỉ sửa prompt?

## Đọc thêm từ nguồn chính thức

- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
