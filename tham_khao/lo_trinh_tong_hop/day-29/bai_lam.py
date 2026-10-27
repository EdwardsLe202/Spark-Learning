"""Ngày 29: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 29
"""
from spark_lab import ROOT, DATA, output_dir

import json
from spark_lab import output_dir
plan = {"observed_error": "DIEN_LOI_DA_DO", "hypothesis": "DIEN_GIA_THUYET",
        "baseline": "prompt-v1/index-v1", "train_source": [],
        "validation_rule": "DIEN_QUY_TAC", "test_locked": True,
        "budget": {"paid_api": 0, "max_train_minutes": 30}}
(output_dir(29) / "experiment_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
print("Điền kế hoạch bằng kết quả lỗi đã quan sát ở ngày 27.")

# Bài tự làm hôm nay:
# TODO Chọn một lỗi thật từ báo cáo ngày 27. Phân loại lỗi tài liệu, retrieval, context, định dạng hoặc hành vi model.
# TODO Viết 1 trang so sánh ba hướng: sửa dữ liệu/retrieval, sửa prompt, fine-tune. Nêu bằng chứng ủng hộ quyết định và chi phí.
# TODO Thiết kế ít nhất 20 ví dụ instruction/input/output có nguồn, tách train và validation theo nhóm; test giữ nguyên và không dùng để tạo ví dụ train.
# TODO Điền experiment_plan.json: model/revision dự kiến, baseline, metric, mục tiêu, giới hạn RAM/thời gian, điều kiện dừng và cách rollback adapter.
# TODO Nếu đủ máy, train adapter LoRA cho model nhỏ phù hợp phần cứng; giữ checkpoint, so với baseline trên test đã khóa. Nếu không train, ghi “thiết kế thí nghiệm, chưa chạy fine-tuning”.
