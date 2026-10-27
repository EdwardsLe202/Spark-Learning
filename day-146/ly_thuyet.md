# Ngày 146 — Quyết định fine-tune hay sửa retrieval

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Quyết định fine-tune hay sửa retrieval”. Kết quả cần đạt: Có quyết định 1 trang gắn lỗi đã đo; không bắt buộc thuê GPU.

## Từ mới gắn với bài này

- **Fine-tuning (điều chỉnh tham số bằng dữ liệu)**.
- **Root cause (nguyên nhân gốc)**.
- **Baseline comparison (so với mốc ban đầu)**.

## Tình huống và cách hiểu

**Fine-tuning (điều chỉnh tham số bằng dữ liệu)** không thay thế nguồn đúng hoặc phân quyền. Nếu tài liệu chưa được retrieve, cần sửa parser/chunk/search trước. Nếu dữ kiện cập nhật thường xuyên, RAG thường giúp cập nhật nguồn trực tiếp hơn.

**Root cause (nguyên nhân gốc)** phải có bằng chứng từ eval/trace. **Baseline comparison (so với mốc ban đầu)** dùng cùng bộ test đã khóa để biết việc train thêm có ích không. Định dạng/giọng điệu lặp lại có thể là mục tiêu thử fine-tune sau khi prompt đã được đo.

Mẫu chỉ tạo form quyết định, không tự kết luận cần train. Bài cốt lõi là lựa chọn có lý do; phần chạy LoRA ngày 148 là mở rộng theo tài nguyên như tài liệu gốc.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-146/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
decision = {"observed_error_id": None, "root_cause": None, "options": ["fix_data_or_retrieval", "change_prompt", "fine_tune"], "chosen": None, "evidence": [], "budget_minutes": 30, "paid_budget": 0}
write_json(out / "decision_template.json", decision)
print("Điền bằng lỗi thật từ dự án RAG, không chọn fine-tune mặc định.")
```

## Đọc từng phần của ví dụ

Giá trị None là chỗ bạn phải quyết định bằng bằng chứng, không phải kết quả kỹ thuật đã chốt.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có quyết định 1 trang gắn lỗi đã đo; không bắt buộc thuê GPU.

## Ba câu kiểm tra hiểu bài

1. Fine-tuning có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: điều chỉnh tham số bằng dữ liệu.
- Luồng chính: Giá trị None là chỗ bạn phải quyết định bằng bằng chứng, không phải kết quả kỹ thuật đã chốt.
- Đối chiếu tiêu chí: Có quyết định 1 trang gắn lỗi đã đo; không bắt buộc thuê GPU. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 29 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
