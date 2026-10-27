# Ngày 144 — Workflow cố định và agent loop có budget

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Workflow cố định và agent loop có budget”. Kết quả cần đạt: Loop dừng đúng budget, trace đầy đủ; chỉ chọn agent nếu có bằng chứng lợi ích.

## Từ mới gắn với bài này

- **Workflow (luồng bước định trước)**.
- **Agent loop (vòng model chọn bước tiếp)**.
- **Step budget (giới hạn số bước)**.

## Tình huống và cách hiểu

**Workflow (luồng bước định trước)** phù hợp câu hỏi luôn cần cùng vài bước. **Agent loop (vòng model chọn bước tiếp)** chỉ đáng dùng khi lựa chọn động giúp hoàn thành tác vụ. Nó thêm rủi ro lặp và chi phí.

**Step budget (giới hạn số bước)** đi cùng giới hạn token, thời gian và điều kiện dừng. Model xin lặp cùng tool không được mở vòng vô hạn. Khi hết budget, trả trạng thái chưa hoàn thành và trace.

Mẫu dùng proposal fixture để test bộ điều phối, không gọi đó là agent LLM thật. Lab nối generator thật đã học, validate từng proposal, dùng tool read-only và so cùng 10 tác vụ với workflow cố định.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-144/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import dispatch_tool
proposals = [{"name": "get_job_status", "arguments": {"job_id": "job-001"}}] * 10
trace = []
for step, proposal in enumerate(proposals[:3], 1):
    trace.append({"step": step, "result": dispatch_tool(proposal["name"], proposal["arguments"])})
print({"status": "budget_exhausted", "calls": len(trace), "trace": trace})
assert len(trace) == 3
```

## Đọc từng phần của ví dụ

Fixture lặp mười đề xuất nhưng bộ điều phối chỉ gọi ba lần. Chưa có model tự chọn hoặc đáp án cuối.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Loop dừng đúng budget, trace đầy đủ; chỉ chọn agent nếu có bằng chứng lợi ích.

## Ba câu kiểm tra hiểu bài

1. Workflow có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: luồng bước định trước.
- Luồng chính: Fixture lặp mười đề xuất nhưng bộ điều phối chỉ gọi ba lần. Chưa có model tự chọn hoặc đáp án cuối.
- Đối chiếu tiêu chí: Loop dừng đúng budget, trace đầy đủ; chỉ chọn agent nếu có bằng chứng lợi ích. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 28 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
