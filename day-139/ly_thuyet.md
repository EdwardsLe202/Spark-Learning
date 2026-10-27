# Ngày 139 — Trace request version usage và dữ liệu riêng tư

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “Trace request version usage và dữ liệu riêng tư”. Kết quả cần đạt: Truy được lỗi theo từng bước, không chứa credential hoặc context ngoài quyền.

## Từ mới gắn với bài này

- **Trace (dấu vết các bước)**.
- **Request ID (mã nối các sự kiện)**.
- **PII — Personally Identifiable Information (thông tin nhận diện cá nhân)**.

## Tình huống và cách hiểu

**Trace (dấu vết các bước)** nối retrieve, rerank, generation và validation trong một request. **Request ID (mã nối các sự kiện)** giúp tìm lỗi mà không phải ghi toàn nội dung người hỏi. **PII — Personally Identifiable Information (thông tin nhận diện cá nhân)** cần giới hạn lưu và quyền xem log.

Ghi prompt/model/index revision, chunk IDs, thời gian từng bước, token và lỗi. Một câu trả lời không có nguồn gốc version khó tái hiện sau reindex. Không log key hoặc context ngoài quyền.

Ví dụ trace keyword baseline ghi rõ không có model generation. Khi dùng rag_answer, trace chứa model revision/usage thực; đừng điền tên model thật vào một lần chạy chưa gọi model.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-139/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus, chunk_documents, keyword_search
import uuid,time
start = time.perf_counter()
ranked = keyword_search("Spark là gì?", chunk_documents(load_corpus()), role="public")
trace = {"request_id": uuid.uuid4().hex, "strategy": "keyword", "generation_model": None, "retrieved_ids": [c["chunk_id"] for c in ranked], "duration_seconds": time.perf_counter() - start, "status": "retrieval_only"}
write_json(out / "trace.json", trace)
print(trace)
```

## Đọc từng phần của ví dụ

Trace trung thực với đường chạy. Đo latency retrieval không giả thành latency end-to-end generation.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Truy được lỗi theo từng bước, không chứa credential hoặc context ngoài quyền.

## Ba câu kiểm tra hiểu bài

1. Trace có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: dấu vết các bước.
- Luồng chính: Trace trung thực với đường chạy. Đo latency retrieval không giả thành latency end-to-end generation.
- Đối chiếu tiêu chí: Truy được lỗi theo từng bước, không chứa credential hoặc context ngoài quyền. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 27 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
