"""Ngày 25: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 25
"""
from spark_lab import ROOT, DATA, output_dir

import hashlib
import json
from spark_lab import DATA
corpus = [json.loads(line) for line in (DATA / "rag/corpus.jsonl").read_text(encoding="utf-8").splitlines()]
chunks = []
for doc in corpus:
    digest = hashlib.sha256(doc["text"].encode()).hexdigest()
    chunks.append({**doc, "chunk_id": f'{doc["doc_id"]}:{doc["version"]}:000', "content_hash": digest})
print("Tài liệu:", len(corpus), "chunk ban đầu:", len(chunks))
# TODO: tách theo đoạn, lưu index và loại chunk cũ khi sửa/xóa tài liệu.

# Bài tự làm hôm nay:
# TODO Đọc data/rag/README.md và corpus.jsonl. Tách theo đoạn, thử chunk size khoảng 200–400 ký tự cho corpus nhỏ; ghi đây là ký tự, không gọi là token.
# TODO Tạo ID ổn định theo doc_id, version và vị trí chunk, kèm content_hash. Chạy ingest hai lần và kiểm tra số ID duy nhất không đổi.
# TODO Tính embedding bằng model hỗ trợ tiếng Việt (gợi ý paraphrase-multilingual-MiniLM-L12-v2), ghi revision thực và chuẩn hóa nếu dùng cosine. Tải model lần đầu cần mạng và dung lượng local, không cần API trả phí.
# TODO Lưu vector và metadata cùng manifest; kiểm tra model/index tương thích trước truy xuất. Có thể dùng Qdrant local thay file, không bắt buộc khởi động server.
# TODO Sửa một doc và xóa một doc trên bản sao corpus trong artifacts. Reindex và kiểm tra chunk cũ không còn truy xuất được; giữ corpus gốc cho benchmark.
