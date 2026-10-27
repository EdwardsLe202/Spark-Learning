# Ngày 138 — Bộ 40 câu và đánh giá generation riêng

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Bộ 40 câu và đánh giá generation riêng”. Kết quả cần đạt: Có đủ 40 output/trace và bảng chấm thật; lỗi generation/permission không bị loại khỏi mẫu số.

## Từ mới gắn với bài này

- **Correctness (độ đúng nội dung)**.
- **Answerability (khả năng trả lời bằng nguồn)**.
- **LLM judge (model dùng để chấm)**.

## Tình huống và cách hiểu

**Correctness (độ đúng nội dung)** và groundedness cần rubric khác retrieval. **Answerability (khả năng trả lời bằng nguồn)** phân biệt câu có đáp án, thiếu nguồn, mơ hồ và sai quyền. **LLM judge (model dùng để chấm)** có thể sai hoặc thiên lệch, không thay kiểm tra thủ công citation.

Bộ eval có 40 câu: 20 trả lời được, 8 thiếu bằng chứng, 6 mơ hồ, 6 ngoài quyền public. Không chỉ lấy điểm trung bình để che lỗi permission. Keywords là gợi ý chấm nội dung, không là bộ chấm đúng hoàn chỉnh.

CLI rag_eval chạy retrieval tự động và có nhánh generation thật, tạo cột chấm tay còn trống. Chỉ ghi điểm sau khi đọc kết quả và nguồn. Không dùng mock generation để báo chất lượng LLM.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-138/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import eval_queries
from collections import Counter
cases = eval_queries()
print(Counter(c["category"] for c in cases))
print(Counter(c["split"] for c in cases))
assert len(cases) == 40
write_json(out / "grading_rubric.json", {"correctness": "đối chiếu dữ kiện", "groundedness": "mỗi phát biểu có bằng chứng", "citation": "đúng đoạn hỗ trợ", "permission": "không có context sai quyền"})
```

## Đọc từng phần của ví dụ

Mẫu kiểm tra thiết kế eval; chạy/chấm thật bằng CLI và bảng thủ công là phần lab.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có đủ 40 output/trace và bảng chấm thật; lỗi generation/permission không bị loại khỏi mẫu số.

## Ba câu kiểm tra hiểu bài

1. Correctness có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: độ đúng nội dung.
- Luồng chính: Mẫu kiểm tra thiết kế eval; chạy/chấm thật bằng CLI và bảng thủ công là phần lab.
- Đối chiếu tiêu chí: Có đủ 40 output/trace và bảng chấm thật; lỗi generation/permission không bị loại khỏi mẫu số. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 27 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
