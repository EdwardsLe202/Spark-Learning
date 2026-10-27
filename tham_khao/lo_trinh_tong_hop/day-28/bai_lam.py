"""Ngày 28: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 28
"""
from spark_lab import ROOT, DATA, output_dir

from pydantic import BaseModel, ConfigDict, Field
class StatusArgs(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    job_id: str = Field(pattern=r"^job-[0-9]{3}$")
STATUSES = {"job-001": "succeeded", "job-002": "failed"}
def get_job_status(args):
    parsed = StatusArgs.model_validate(args)
    return {"job_id": parsed.job_id, "status": STATUSES.get(parsed.job_id, "not_found")}
print(get_job_status({"job_id": "job-001"}))
# TODO: dispatcher theo allowlist, kiểm tra quyền, timeout và tối đa 3 bước.

# Bài tự làm hôm nay:
# TODO Chạy công cụ giả lập và thử job_id không đúng mẫu, trường thừa, job không tồn tại; ghi rõ loại lỗi.
# TODO Tạo dispatcher chỉ cho search_docs và get_job_status. Thử đề xuất công cụ delete_file và kiểm tra bị từ chối trước khi chạy.
# TODO Xây workflow cố định: xác định câu hỏi → truy xuất tài liệu được phép → lấy trạng thái nếu cần → trả lời có nguồn. Giữ request_id xuyên suốt.
# TODO Thêm loop mô phỏng tối đa 3 bước, tổng timeout và retry tối đa 1 với lỗi tạm thời. Test model đề xuất cùng công cụ mãi vẫn phải dừng.
# TODO So 10 tác vụ giữa workflow và loop: đúng đáp án, đúng công cụ, số bước, latency và lỗi quyền. Dùng kết quả để chọn cách đơn giản phù hợp.
