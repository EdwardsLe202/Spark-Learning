# Ngày 29 — Lý thuyết: Fine tuning và tối ưu mô hình nâng cao

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md) · [Thuật ngữ](../docs/THUAT_NGU.md)

Mục tiêu: Viết quyết định có cần fine-tune và thiết kế thí nghiệm không nhiễm test.

## 1. Sửa đúng tầng gây lỗi
Fine-tuning điều chỉnh tham số dựa trên ví dụ huấn luyện. Nếu retrieval không tìm được tài liệu, thường cần sửa parser, chunk hoặc tìm kiếm trước. Nếu dữ kiện cập nhật thường xuyên, RAG giúp thay nguồn mà không train lại mỗi lần. Nếu model không theo định dạng hay phong cách ổn định dù prompt tốt, fine-tuning có thể là một hướng cần thử bằng số liệu.

**Training data contamination (nhiễm dữ liệu đánh giá vào huấn luyện)** xảy ra khi dùng câu test hoặc đáp án test để tạo dữ liệu train. Dedup cần xét cả bản gần giống; chia theo tài liệu hoặc nhóm chủ đề khi phù hợp, không chỉ xáo dòng. Cần có quyền dùng dữ liệu và ghi nguồn.

## 2. Các kỹ thuật chính
**Full fine-tuning (điều chỉnh toàn bộ trọng số)** tốn bộ nhớ cho trọng số, gradient và trạng thái optimizer. **PEFT — Parameter-Efficient Fine-Tuning (điều chỉnh với ít tham số được học)** giảm phần cần cập nhật. **LoRA — Low-Rank Adaptation (điều chỉnh bằng ma trận hạng thấp)** thêm các ma trận nhỏ trong khi thường giữ đông cứng trọng số nền. Adapter nhỏ không có nghĩa model nền không còn chiếm bộ nhớ.

**Quantization (lượng tử hóa)** giảm độ chính xác biểu diễn số để giảm tài nguyên, có thể ảnh hưởng chất lượng và hỗ trợ phần cứng. **Distillation (chưng cất kiến thức sang mô hình khác)** dùng tín hiệu từ model lớn để học model nhỏ. Các kỹ thuật này cần đánh giá với baseline; không chỉ nhìn dung lượng giảm.

## 3. Thí nghiệm phải có quyết định dừng
Ghi lỗi mục tiêu, dataset version, baseline prompt/RAG, tiêu chí cải thiện, giới hạn thời gian và bộ nhớ. Giữ test khóa trước khi train; chọn checkpoint trên validation. Chấm cả chất lượng, latency và mức dùng tài nguyên. Bài cốt lõi ngày này là bản quyết định kỹ thuật và thiết kế dataset; train adapter là bài mở rộng theo tài nguyên, không cần thuê GPU để hoàn thành lộ trình 30 ngày.

## Ví dụ nhỏ để đọc và chạy

Ví dụ Python nằm sẵn trong `bai_lam.py`; xem điều kiện thư viện ở README của ngày.

```python
import json
from spark_lab import output_dir
plan = {"observed_error": "DIEN_LOI_DA_DO", "hypothesis": "DIEN_GIA_THUYET",
        "baseline": "prompt-v1/index-v1", "train_source": [],
        "validation_rule": "DIEN_QUY_TAC", "test_locked": True,
        "budget": {"paid_api": 0, "max_train_minutes": 30}}
(output_dir(29) / "experiment_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
print("Điền kế hoạch bằng kết quả lỗi đã quan sát ở ngày 27.")
```

## Năm ý đối chiếu với lộ trình gốc

- 29.1 — Chọn giữa cải thiện dữ liệu, prompt, retrieval và fine tuning.
- 29.2 — Dataset hướng dẫn, quyền sử dụng, dedup, train validation test và contamination.
- 29.3 — Full fine tuning, PEFT, LoRA và quantization ở mức khái niệm.
- 29.4 — Chi phí train, checkpoint, metric và so sánh với baseline giữ nguyên.
- 29.5 — Distillation, distributed training và inference engine ở mức định hướng học tiếp.

Các ý trên giữ phạm vi phần 29 của tài liệu gốc. Phần giải thích và lab là vòng học đầu trong 30 ngày; công nghệ nâng cao được triển khai sâu ở bài mở rộng.

## Câu hỏi tự kiểm tra

1. LoRA giảm phần nào của huấn luyện?
2. Quantization có bảo đảm không đổi chất lượng không?
3. Khi nào fine-tune chưa giải quyết đúng nguyên nhân?

## Đọc thêm từ nguồn chính thức

- [Hugging Face LoRA](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora)

Ưu tiên tài liệu đúng phiên bản đã cài. Mục [nguồn học](../docs/NGUON_HOC.md) ghi bộ phiên bản và phạm vi tham khảo.
