"""Ngày 27: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 27
"""
from spark_lab import ROOT, DATA, output_dir

import json
from collections import Counter
from spark_lab import DATA
cases = [json.loads(line) for line in (DATA / "rag/queries.jsonl").read_text(encoding="utf-8").splitlines()]
print("Số câu:", len(cases))
print("Nhóm:", dict(Counter(case["category"] for case in cases)))
# TODO: chạy từng case qua retrieval/generation; lưu trace và chấm riêng từng nhóm.

# Bài tự làm hôm nay:
# TODO Giữ cố định 40 câu có sẵn; không sửa test để làm đẹp kết quả. Bổ sung câu mới ở file riêng nếu tìm ra thiếu sót.
# TODO Chạy retrieval rồi generation qua adapter ngày 24. Nếu mới dùng mock/extractive output, báo cáo phần generation chưa được đánh giá bằng LLM thật.
# TODO Đối chiếu expected_behavior và expected_keywords như gợi ý, sau đó chấm tay nội dung và citation; không xem có keyword là chắc đúng.
# TODO Thử doc-injection và câu hỏi tự nhận admin. Kiểm tra doc-internal không tới context của user_role=public, kể cả khi score cao nhất.
# TODO Lưu JSONL trace và bảng metric: retrieval, answer correctness, groundedness, citation support, abstention, permission violations, latency. Điều tra mọi lỗi quyền trước khi chốt.
