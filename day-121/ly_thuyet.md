# Ngày 121 — Token context window và giới hạn sinh

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Token context window và giới hạn sinh”. Kết quả cần đạt: Có budget và token count thật; không quy ước một từ bằng một token.

## Từ mới gắn với bài này

- **Token (đơn vị văn bản của tokenizer)**.
- **Context window (giới hạn ngữ cảnh)**.
- **Sampling (cách chọn token kế tiếp)**.

## Tình huống và cách hiểu

**Token (đơn vị văn bản của tokenizer)** không luôn là một từ; tiếng Việt không có tỷ lệ token/từ cố định. **Context window (giới hạn ngữ cảnh)** và giới hạn đầu ra phụ thuộc model. Tính cả chỉ dẫn, câu hỏi, bằng chứng và phần sinh.

**Sampling (cách chọn token kế tiếp)** ảnh hưởng tính ngẫu nhiên, không bảo đảm đúng dữ kiện. Do_sample=false giúp giảm một nguồn ngẫu nhiên trong lab nhưng chưa bảo đảm mọi phần cứng cho từng ký tự giống nhau.

Mẫu chỉ tính budget giả định để hiểu cộng trừ; lab phải dùng tokenizer thật đã tải ngày 116. Không dùng len(text) như số token khi báo chi phí hoặc giới hạn model.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-121/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
budget = {"limit": 2048, "instruction_tokens": 150, "question_tokens": 80, "context_tokens": 1200, "max_output_tokens": 256}
print("Tổng dự kiến:", sum(v for k, v in budget.items() if k != "limit"))
assert sum(v for k, v in budget.items() if k != "limit") <= budget["limit"]
print("Các số là ví dụ budget; đo token thật bằng tokenizer trong lab.")
```

## Đọc từng phần của ví dụ

Limit là ngân sách lab, không tuyên bố context window tối đa của Qwen. Token count giả định được ghi rõ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có budget và token count thật; không quy ước một từ bằng một token.

## Ba câu kiểm tra hiểu bài

1. Token có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: đơn vị văn bản của tokenizer.
- Luồng chính: Limit là ngân sách lab, không tuyên bố context window tối đa của Qwen. Token count giả định được ghi rõ.
- Đối chiếu tiêu chí: Có budget và token count thật; không quy ước một từ bằng một token. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 24 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
