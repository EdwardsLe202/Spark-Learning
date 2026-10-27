# Dự án 3 — Ứng dụng RAG có đánh giá

[Các dự án](../README.md) · [Ngày 25](../../day-25/README.md) · [Ngày 30](../../day-30/README.md)

Xây pipeline ingest tách khỏi luồng online: xác thực/quyền → retrieve → chọn context → generate → kiểm tra và trích dẫn. Dùng corpus tự tạo cùng 40 truy vấn ở [data/rag](../../data/rag/README.md).

## Tiêu chí cốt lõi

- [ ] Chunk có doc_id, chunk_id, source, version, access, content_hash.
- [ ] Ingest lại không nhân bản; sửa/xóa doc làm chunk cũ mất hiệu lực.
- [ ] Dense retrieval dùng embedding thật, ghi model/revision/metric/normalization.
- [ ] So dense với hybrid hoặc reranker trên cùng dev; chọn rồi mới chấm test.
- [ ] Retrieval metric theo doc_id, không lẫn nhãn doc với kết quả chunk.
- [ ] Có câu trả lời từ model thật kèm citation hỗ trợ nội dung; khi thiếu bằng chứng phải từ chối hoặc yêu cầu làm rõ.
- [ ] Chạy đủ 40 câu, tách nhóm answerable, unanswerable, ambiguous và forbidden.
- [ ] Quyền được áp dụng trước context; permission violations bằng 0.
- [ ] Trace có request_id, prompt/model/index version, các bước, lỗi và latency.
- [ ] Thử prompt injection, model timeout và index lỗi, có giới hạn retry.
- [ ] Phân tích ít nhất 5 lỗi hoặc ca khó bằng bằng chứng nguồn/retrieval/generation.

Keyword search, output trích nguyên văn và mock giúp kiểm thử phần mềm nhưng **chưa hoàn thành** các tiêu chí dense/generation bằng model thật. Ghi rõ trạng thái thay vì tự chấm điểm chất lượng LLM trên đầu ra giả lập. Model local nhỏ là một lựa chọn nếu không dùng API trả phí.

## Tool workflow ngày 28

- [ ] Chỉ cho phép search_docs và get_job_status của dữ liệu giả lập.
- [ ] Validator chặn tham số sai và tên công cụ lạ.
- [ ] Có tối đa 3 bước, timeout và retry hữu hạn.
- [ ] Không dùng eval/exec/shell cho đề xuất model.
- [ ] So workflow cố định với loop bằng tác vụ có nhãn.

## Bảng nghiệm thu của bạn

| Hạng mục | Cấu hình / version | Bằng chứng và kết quả |
| --- | --- | --- |
| Corpus/chunk/index | ... | ... |
| Embedding | ... | ... |
| Dense baseline | ... | ... |
| Hybrid/reranker | ... | ... |
| Generation / prompt | ... | ... |
| 40 eval và nhóm quyền | ... | ... |
| Trace / latency / lỗi | ... | ... |
| Update/delete và rollback index | ... | ... |

## Lệnh và runbook

```bash
# Điền lệnh ingest, retrieve, generate và evaluate thực tế.
```

- Cách chọn và cố định model revision: ...
- Cách xóa tài liệu và xác nhận hết chunk: ...
- Khi index không tương thích embedding: ...
- Khi model timeout hoặc không có bằng chứng: ...
- Phần model thật / mock / chưa làm: ...

