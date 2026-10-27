# Ngày 128 — ID content hash version và xóa tài liệu

[Trang ngày](README.md) · [Thực hành](thuc_hanh.md)

## Mục tiêu nhỏ

Học đúng kỹ năng “ID content hash version và xóa tài liệu”. Kết quả cần đạt: Rerun không nhân ID; thêm/sửa/xóa có kiểm tra tập chunk hoạt động.

## Từ mới gắn với bài này

- **Document ID / Chunk ID (mã tài liệu / đoạn)**.
- **Content hash (mã băm nội dung)**.
- **Reindex (tạo lại chỉ mục)**.

## Tình huống và cách hiểu

**Document ID / chunk ID (mã tài liệu / đoạn)** giúp upsert và truy nguồn. **Content hash (mã băm nội dung)** phát hiện thay đổi, không tự lưu lịch sử. Khi doc đổi số đoạn, phải xóa chunk cũ không còn hoạt động.

**Reindex (tạo lại chỉ mục)** cần version corpus/chunker/model. Chỉ thêm chunk mới mà không gỡ bản cũ có thể truy xuất nội dung đã bị xóa. Một index rebuild từ corpus hiện hành là cách đơn giản, rõ ràng cho dữ liệu nhỏ.

Mẫu kiểm tra chạy chunk hai lần có cùng ID. Lab sửa/xóa trên bản sao trong artifacts, giữ corpus gốc để benchmark. Không thay test labels theo bản index đã xóa bớt rồi vẫn gọi cùng benchmark.

## Ví dụ có thể chạy nguyên file

[vi_du.py](vi_du.py) có đủ import, khởi tạo và kết thúc tài nguyên cần thiết. Đoạn dưới là phần đang học, không dán riêng vào shell.

`out` là đích riêng `artifacts/full/day-128/example`; bài làm dùng thư mục exercise bên cạnh. `ROOT/DATA/FULL` là đường dẫn repo/dữ liệu/đầu ra. Các helper chuẩn bị snapshot/model chỉ chạy khi được gọi, không train hoặc tải model lúc import.

```python
from rag_support import load_corpus, chunk_documents
corpus = load_corpus()
a, b = chunk_documents(corpus), chunk_documents(corpus)
assert [c["chunk_id"] for c in a] == [c["chunk_id"] for c in b]
kept = chunk_documents([d for d in corpus if d["doc_id"] != "doc-spark"])
assert not any(c["doc_id"] == "doc-spark" for c in kept)
write_json(out / "chunks.json", a)
print(len(a), "chunk ID ổn định; bản thử xóa doc không còn chunk của doc đó.")
```

## Đọc từng phần của ví dụ

Bản thử rebuild từ tập doc hiện hành. Chưa gọi API vector store, nên nghiệm thu xóa khỏi store làm ngày 130.

Nếu thấy helper chưa rõ, mở [course_support.py](../course_support.py) hoặc [rag_support.py](../rag_support.py) để đọc đầu vào/đầu ra. Đây là mã tham chiếu; bài yêu cầu tự viết logic thì chỉ gọi helper chưa đủ để hoàn thành.

## Kết quả để đối chiếu

Rerun không nhân ID; thêm/sửa/xóa có kiểm tra tập chunk hoạt động.

## Ba câu kiểm tra hiểu bài

1. Document ID / Chunk ID có nghĩa gì trong đúng dữ liệu của ví dụ?
2. Đầu vào, bước xử lý chính và đầu ra là gì? Chỉ vào dòng code tương ứng.
3. Ví dụ đã kiểm chứng điều gì, còn bước nào trong lab cần chạy thật hoặc điều tra thêm?

<details>
<summary>Gợi ý sau khi bạn tự trả lời</summary>

- Từ đầu tiên: mã tài liệu / đoạn.
- Luồng chính: Bản thử rebuild từ tập doc hiện hành. Chưa gọi API vector store, nên nghiệm thu xóa khỏi store làm ngày 130.
- Đối chiếu tiêu chí: Rerun không nhân ID; thêm/sửa/xóa có kiểm tra tập chunk hoạt động. Chú ý phần lý thuyết đã phân biệt fixture/mô phỏng/kiểm tra cấu hình với lab tích hợp.

</details>

Tra API đúng phiên bản ở [nguồn học](../docs/NGUON_HOC.md). Phần 25 của lộ trình gốc được nối tại bài này; xem [bảng đối chiếu từng ý](../docs/DOI_CHIEU_LO_TRINH_GOC.md).
