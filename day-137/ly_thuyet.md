# Ngày 137 — Ghép context sinh trả lời và kiểm tra citation

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Ghép context sinh trả lời và kiểm tra citation”. Kết quả cần đạt: Có output model thật/trace; câu không hỗ trợ phải từ chối hoặc được ghi lỗi, không che bằng keyword hit.

## Từ mới gắn với bài này

- **Groundedness (mức câu được bằng chứng hỗ trợ)**.
- **Citation (trích dẫn nguồn)**.
- **Abstention (từ chối khi thiếu bằng chứng)**.

## Tình huống và cách hiểu

**Groundedness (mức câu được bằng chứng hỗ trợ)** khác việc câu nghe hợp lý. **Citation (trích dẫn nguồn)** phải hỗ trợ phát biểu cụ thể, không chỉ cùng chủ đề. **Abstention (từ chối khi thiếu bằng chứng)** là hành vi mong muốn khi corpus không đủ.

Context chỉ gồm chunk đã qua quyền và version. Adapter generator nhận dữ liệu cùng chỉ dẫn cố định, rồi parser chặn JSON/citation ngoài tập. Việc citation ID tồn tại chưa chứng minh nội dung được hỗ trợ; cần đọc nguồn hoặc rubric để chấm.

Helper rag_answer dùng dense thật và model local thật. Nếu output sai schema, trả generation_error; không biến lỗi thành câu trả lời giả rồi tính đúng. Ngưỡng similarity là cấu hình cần chọn trên dev, không có một số chung bảo đảm không hallucinate.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-137/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import rag_answer
result = rag_answer("local[2] là hai máy hay hai luồng?", role="public", k=3)
write_json(out / "answer.json", result)
print(result)
```

## Đọc từng phần của ví dụ

Rag_answer lấy bằng chứng, gọi generator và kiểm tra cấu trúc/citation. Status error được giữ khi model nhỏ không tuân thủ.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Có output model thật/trace; câu không hỗ trợ phải từ chối hoặc được ghi lỗi, không che bằng keyword hit.

## Ba câu kiểm tra hiểu bài

1. Groundedness có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mức câu được bằng chứng hỗ trợ.
- Luồng chính: Rag_answer lấy bằng chứng, gọi generator và kiểm tra cấu trúc/citation. Status error được giữ khi model nhỏ không tuân thủ.
- Đối chiếu tiêu chí: Có output model thật/trace; câu không hỗ trợ phải từ chối hoặc được ghi lỗi, không che bằng keyword hit. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 27 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
