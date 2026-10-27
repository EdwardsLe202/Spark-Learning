# Dự án 3 — RAG có eval và quyền

[Lịch đầy đủ](../../LO_TRINH_DAY_DU.md) · [Ngày nghiệm thu 145](../../day-145/README.md)

Dùng corpus/queries giả lập ở data/rag. Ingest và luồng trả lời tách biệt, role lấy từ tầng tin cậy. Tích lũy ngày 121–145: chunk/index, dense/hybrid/reranker, generation, eval/trace và tool workflow.

Keyword/TF-IDF là baseline từ vựng; vector cố định chỉ test API store. Mock/model proposal fixture chỉ kiểm tra phần mềm. Chúng chưa thay dense/generation/reranker thật ở những tiêu chí tương ứng.

## Tiêu chí nghiệm thu

- [ ] Mỗi chunk có doc_id/chunk_id/source/version/access/content_hash; trace ngược nguồn được.
- [ ] Ingest chạy lại không tăng ID; update/delete gỡ chunk cũ, có index/model compatibility check.
- [ ] Dense baseline bằng embedding thật, giữ resolved revision/norm/metric; so thêm hybrid hoặc reranker thật.
- [ ] Chọn trên dev, chấm test cuối; metric theo doc_id sau gộp chunk, không chia Recall cho nhóm không relevant.
- [ ] Generation bằng model thật, citation hỗ trợ nội dung, thiếu nguồn từ chối và mơ hồ hỏi lại.
- [ ] Chạy đủ40 ca: 20 answerable/8 thiếu nguồn/6 mơ hồ/6 forbidden; chấm tay correctness/groundedness/citation theo nhóm.
- [ ] ACL trước context, 0 context permission violation; query tự nhận admin không tăng quyền.
- [ ] Trace request/prompt/model/index revision/token/latency/lỗi, không lưu credential/context sai quyền.
- [ ] Thử injection, model timeout/index lỗi, bounded retry và đường phục hồi.
- [ ] Tool read-only có schema/allowlist/role/timeout và tối đa3 bước; so workflow với agent trên10 tác vụ.
- [ ] Phân tích ít nhất5 lỗi/ca khó và clean run có model/cache manifest rõ.

## Ca phải demo

1. Câu không có đáp án và câu mơ hồ.
2. Public hỏi doc-internal, internal hợp lệ ở fixture riêng.
3. Chỉ dẫn giả trong doc-injection không được chạy tool hoặc đổi role.
4. Sửa/xóa doc rồi đổi/rollback index tương thích embedding.
5. Tool unknown/args sai/timeout/lặp phải bị chặn hoặc dừng đúng budget.

## Nơi tự làm và ghi bằng chứng

Gom code của các ngày vào dự án hoặc liên kết tới module gốc. Không cần chép lặp mọi file. Đầu ra dùng artifacts/full và manifest riêng, không sửa source fixtures hoặc bản lưu.

| Hạng mục | Lệnh / code / version | Kết quả / log | Đã chạy hay mới thiết kế |
| --- | --- | --- | --- |
| Dữ liệu và cấu hình | ... | ... | ... |
| Tính đúng / chất lượng | ... | ... | ... |
| Test và ca lỗi | ... | ... | ... |
| Phục hồi / chạy lại | ... | ... | ... |
| Clean run | ... | ... | ... |

## Hướng dẫn cần hoàn thiện

- Điều kiện môi trường và phiên bản:
- Lệnh chạy từng bước:
- Nguồn/hash, model/prompt/index version:
- Expected output và cách đối chiếu:
- Ba lỗi thường gặp, kiểm tra và phục hồi:
- Phần chưa chạy, giới hạn tài nguyên và việc học tiếp:
