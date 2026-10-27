"""Ngày 26: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 26
"""
from spark_lab import ROOT, DATA, output_dir

def recall_at_k(ranked_doc_ids, relevant_doc_ids, k):
    relevant = set(relevant_doc_ids)
    if not relevant:
        return None  # Đánh giá câu không có đáp án bằng metric khác.
    return len(set(ranked_doc_ids[:k]) & relevant) / len(relevant)
print(recall_at_k(["doc-api", "doc-spark", "doc-rag"], ["doc-spark"], 2))
# TODO: thay danh sách mẫu bằng output retrieval trên corpus thật.

# Bài tự làm hôm nay:
# TODO Đọc queries.jsonl; chỉ dùng split=dev để chọn chunk size, top-k và cấu hình. Giữ split=test cho báo cáo cuối.
# TODO Tạo baseline dense ngày 25. Lọc access dựa trên user_role tin cậy ở server trước truy xuất, không tin role do prompt tự nhận.
# TODO Thêm một nhánh TF-IDF/BM25; hợp nhất bằng RRF hoặc thêm reranker thật. Không gọi một lần sort score cũ là reranking bằng model.
# TODO Tính Recall@1/@3 và MRR theo doc_id cho các câu có relevant hợp lệ; đo median/p95 latency và ghi lỗi. Tách nhóm unanswerable/ambiguous/forbidden.
# TODO Chọn cấu hình trên dev rồi đánh giá test; phân tích ít nhất 5 truy vấn sai hoặc khó bằng nguồn → chunk → embedding → retrieval → ranking.
