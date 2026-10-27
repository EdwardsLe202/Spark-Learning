"""Ngày 30: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 30
"""
from spark_lab import ROOT, DATA, output_dir

from spark_lab import ROOT
for project in ["01-data-pipeline", "02-mlops", "03-rag"]:
    readme = ROOT / "projects" / project / "README.md"
    print(project, "->", readme)
# TODO: điền bảng nghiệm thu và liên kết tới code/log/test thực của từng dự án.

# Bài tự làm hôm nay:
# TODO Đối chiếu ba README dự án, điền đường dẫn bằng chứng cho từng tiêu chí. Sửa lỗi về thời gian, khóa và quyền trước khi thêm công nghệ.
# TODO Tạo môi trường mới theo docs/CAI_DAT.md, dùng output path mới. Chạy data → features → train/load → score → API và ingest → retrieve → answer/eval theo phạm vi đã hoàn thành.
# TODO Demo một file lỗi, một backfill, một candidate bị từ chối, một rollback, câu hỏi không có nguồn và tài liệu ngoài quyền.
# TODO Viết data dictionary, model card, release manifest, runbook và báo cáo retrieval/generation. Chỉ gắn số liệu đo thật, ghi máy và dữ liệu.
# TODO Chuẩn bị demo 10 phút: 2 phút kiến trúc, 3 phút tính đúng, 2 phút MLOps/API, 2 phút RAG, 1 phút giới hạn. Ghi 5 việc học tiếp theo bằng lỗ hổng thực tế.
