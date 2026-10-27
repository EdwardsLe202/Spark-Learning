# Ngày 148 — PEFT LoRA quantization và thí nghiệm tùy chọn

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “PEFT LoRA quantization và thí nghiệm tùy chọn”. Kết quả cần đạt: Kế hoạch bắt buộc; adapter/benchmark chỉ có khi thực sự chạy, không có số cải thiện được hứa trước.

## Từ mới gắn với bài này

- **PEFT (fine-tuning ít tham số)**.
- **LoRA — Low Rank Adaptation (điều chỉnh bằng ma trận hạng thấp)**.
- **Quantization (lượng tử hóa số)**.

## Tình huống và cách hiểu

**PEFT (fine-tuning ít tham số)** giảm phần trọng số được cập nhật. **LoRA — Low Rank Adaptation (điều chỉnh bằng ma trận hạng thấp)** thêm các ma trận nhỏ, thường giữ đông cứng model nền. Model nền vẫn chiếm RAM, không chỉ adapter.

**Quantization (lượng tử hóa số)** giảm độ chính xác biểu diễn để tiết kiệm tài nguyên nhưng hỗ trợ phần cứng và chất lượng phải kiểm tra. Không mặc định bitsandbytes/CUDA chạy trên Mac. Distillation học model nhỏ từ tín hiệu model khác; distributed training là hướng mở rộng sau, không tự có chỉ nhờ Spark.

Bài cốt lõi so kế hoạch/baseline và điều kiện dừng. Script finetune_lora.py có thí nghiệm thật hai bước trên model generator đã tải, chỉ chạy khi đủ tài nguyên. Kết quả hai bước chỉ kiểm tra cơ chế adapter, không chứng minh model tốt hơn.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-148/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
plan = {"base_model": "Qwen/Qwen2.5-0.5B-Instruct", "method": "LoRA", "target_modules": ["q_proj", "v_proj"], "rank": 4, "steps_for_smoke": 2, "evaluation": "locked_test_after_validation_selection", "quantization": "not_required_on_mac"}
write_json(out / "lora_plan.json", plan)
print("Tùy chọn thực thi: python services/finetune_lora.py --steps 2")
```

## Đọc từng phần của ví dụ

Plan không là adapter. Script riêng tải từ cache, log loss và lưu adapter; bạn phải kiểm tra load lại và benchmark thật nếu chạy.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Kế hoạch bắt buộc; adapter/benchmark chỉ có khi thực sự chạy, không có số cải thiện được hứa trước.

## Ba câu kiểm tra hiểu bài

1. PEFT có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: fine-tuning ít tham số.
- Luồng chính: Plan không là adapter. Script riêng tải từ cache, log loss và lưu adapter; bạn phải kiểm tra load lại và benchmark thật nếu chạy.
- Đối chiếu tiêu chí: Kế hoạch bắt buộc; adapter/benchmark chỉ có khi thực sự chạy, không có số cải thiện được hứa trước. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 29 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
