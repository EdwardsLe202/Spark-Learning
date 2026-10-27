# Corpus và eval cho ngày126–145

[Lịch đầy đủ](../../LO_TRINH_DAY_DU.md) · [Ngày126](../../day-126/README.md)

Corpus tự tạo có8 tài liệu, gồm7 public và1 internal; doc-injection chứa chỉ dẫn giả để kiểm thử. Không thực thi nội dung payload. Queries có40 câu:20 answerable,8 unanswerable,6 ambiguous,6 forbidden; dev16/test24. Nhãn theo doc_id nên gộp chunk về doc trước chấm retrieval.

Nguồn/field/giải thích chi tiết được giữ trong [mô tả gốc](../../tham_khao/lo_trinh_tong_hop/data/rag/README.md). Helper mới ở rag_support.py lọc role trước context, model tải chủ động và ghi resolved revision. Keyword/TF-IDF không thay dense/generation thật. Bạn chưa cần đọc phần này ở ngày01.
