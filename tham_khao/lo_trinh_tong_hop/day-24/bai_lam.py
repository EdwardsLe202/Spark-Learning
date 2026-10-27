"""Ngày 24: ví dụ khởi động; đọc thuc_hanh.md rồi hoàn thiện TODO.
Chạy từ repo: python scripts/run_day.py 24
"""
from spark_lab import ROOT, DATA, output_dir

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

# Bài tự làm hôm nay:
# TODO Cài requirements-api.txt nếu chưa có. Chạy parser mẫu; giữ trường thiếu/null theo quy tắc rõ ràng.
# TODO Tạo 10 đoạn tiếng Việt có đơn hàng: đủ dữ kiện, thiếu tiền, nhiều mã, tiền mơ hồ và câu chứa chỉ dẫn gây nhiễu. Tự gán nhãn trước.
# TODO Viết hai prompt cùng schema và giới hạn đầu ra; yêu cầu null khi không có bằng chứng. Version prompt thành v1 và v2.
# TODO Viết hàm generate(prompt, text) tách khỏi validator. Trước hết thử đầu ra giả lập để kiểm tra lỗi; sau đó dùng một model local nhỏ hoặc API đã chọn để đo nội dung thật.
# TODO So cùng 10 mẫu, ghi schema pass rate, field accuracy, lỗi, latency và usage nếu có. Giới hạn retry tối đa 2, lưu trạng thái cuối.
